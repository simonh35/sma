---
title: Script - pdf_to_markdown
author: skr
type: script
publish: false
tags: 
source: 
dependencies: 
date_created: 2024-11-28
---
---
# Technisches Konzept

# Schritt-für-Schritt Implementierungsanleitung

## Ziel

Diese Anleitung führt Sie durch die Entwicklung einer Anwendung, die PDF-Dokumente in Markdown umwandelt. Sie ist für Benutzer ohne Entwicklungserfahrung konzipiert und verwendet ein MacBook mit M3-Chip.

## 1. Voraussetzungen

### 1.1 Software-Anforderungen

Bevor Sie mit der Entwicklung beginnen, müssen Sie sicherstellen, dass die folgenden Software-Anforderungen erfüllt sind:

**Python 3.11+**  
Python ist die Programmiersprache, die wir verwenden werden. Sie können die neueste Version von Python von der offiziellen Website herunterladen: [Python Download](https://www.python.org/downloads/).

**Homebrew**  
Homebrew ist ein Paketmanager für macOS, der die Installation von Software erleichtert. Um Homebrew zu installieren, öffnen Sie das Terminal (Sie finden es unter Anwendungen > Dienstprogramme > Terminal) und geben Sie den folgenden Befehl ein:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Tesseract OCR**  
Tesseract ist ein Tool zur Texterkennung, das wir benötigen, um Text aus Bildern in PDFs zu extrahieren. Installieren Sie es mit Homebrew:
```
brew install tesseract
```

### 1.2 Terminal öffnen

Um die folgenden Schritte auszuführen, müssen Sie das Terminal öffnen. Suchen Sie nach "Terminal" in Spotlight (Cmd + Leertaste) und öffnen Sie es.

## 2. Projekt einrichten

### 2.1 Verzeichnisstruktur erstellen

**Neues Verzeichnis erstellen:**  
Erstellen Sie einen neuen Ordner für Ihr Projekt mit dem folgenden Befehl im Terminal:
```
mkdir -p /Users/skr/neomint-research/pdf_to_markdown cd /Users/skr/neomint-research/pdf_to_markdown
```

**Unterverzeichnisse erstellen:**  
Erstellen Sie die benötigten Unterverzeichnisse:
```
mkdir src tests docs
```

### 2.2 Virtuelle Umgebung einrichten

Eine virtuelle Umgebung hilft Ihnen, die benötigten Bibliotheken zu installieren, ohne andere Projekte zu beeinflussen.

**Virtuelle Umgebung erstellen:**  
Geben Sie im Terminal den folgenden Befehl ein:
```
python3 -m venv venv
```

**Virtuelle Umgebung aktivieren:**  
Aktivieren Sie die virtuelle Umgebung mit:

```
source venv/bin/activate
```

Sie sollten jetzt sehen, dass der Name Ihrer virtuellen Umgebung (z.B. `(venv)`) vor der Eingabeaufforderung steht.

## 3. Erforderliche Bibliotheken installieren

Installieren Sie die benötigten Python-Bibliotheken, indem Sie den folgenden Befehl im Terminal eingeben:
```
pip install pdfminer.six pdf2image pytesseract pandas pytest
```

## 4. Implementierung der Anwendung

### 4.1 Quellcode erstellen

**Erstellen Sie die Hauptdatei:**  
Erstellen Sie eine Datei namens `main.py` im `src`-Verzeichnis:

```
touch src/main.py
```

**Öffnen Sie die Datei in einem Texteditor:**  
Sie können einen einfachen Texteditor wie TextEdit verwenden oder einen Code-Editor wie Visual Studio Code installieren.

-**Fügen Sie den folgenden Code in `main.py` ein:**
```
import logging  
from pdf_handler import PDFHandler  
from content_processor import ContentProcessor  
from error_handler import ErrorHandler  

def main(pdf_path: str):  
    """Main function to convert PDF to Markdown."""  
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
    error_handler = ErrorHandler()  

    try:  
        pdf_handler = PDFHandler(pdf_path)  
        content = pdf_handler.extract_content()  

        processor = ContentProcessor()  
        processed_images = processor.process_images(content['images'])  
        processed_text = processor.process_text(content['text'])  

        # Hier kann die Markdown-Konvertierung implementiert werden  
        print("Processed Text:", processed_text)  
        print("Processed Images:", processed_images)  

    except Exception as e:  
        error_handler.handle_exception(e)  

if __name__ == "__main__":  
    # Beispiel-PDF-Pfad  
    pdf_path = "/path/to/test.pdf"  
    main(pdf_path)    
```

### 4.2 Weitere Dateien erstellen

Um die Anwendung vollständig zu machen, müssen Sie auch die anderen Module erstellen. Hier sind einige grundlegende Beispiele für die Struktur:

#### **Handler erstellen**  
Erstellen Sie einen Ordner für Handler und die Datei `pdf_handler.py`:

```
mkdir src/handlers touch src/handlers/pdf_handler.py
```

Fügen Sie den folgenden Code in `pdf_handler.py` ein:

```
#!/usr/bin/env python3    
# -*- coding: utf-8 -*-    

"""    
PDF Handler Module    
----    
Handles PDF file operations including text and image extraction.    
"""    

from typing import Dict, List, Union, Optional    
from pathlib import Path    
import logging    

from pdfminer.high_level import extract_text    
from pdf2image import convert_from_path    
import pytesseract    
from PIL import Image    

class PDFHandler:    
    """    
    Handles PDF file operations including text and image extraction.    
    """    

    def __init__(self, file_path: str):    
        """    
        Initialize PDFHandler with file path.    

        Args:    
            file_path (str): Path to the PDF file    

        Raises:    
            FileNotFoundError: If the PDF file doesn't exist    
            ValueError: If the file is not a PDF    
        """    
        self.file_path = Path(file_path)    
        self._validate_file()    
        self.logger = logging.getLogger(__name__)    

    def _validate_file(self) -> None:    
        """    
        Validate the PDF file existence and format.    

        Raises:    
            FileNotFoundError: If the PDF file doesn't exist    
            ValueError: If the file is not a PDF    
        """    
        if not self.file_path.exists():    
            raise FileNotFoundError(f"PDF-Datei nicht gefunden: {self.file_path}")    

        if self.file_path.suffix.lower() != '.pdf':    
            raise ValueError(f"Datei ist keine PDF-Datei: {self.file_path}")    

    def extract_content(self) -> Dict[str, Union[str, List[Dict[str, Any]]]]:    
        """    
        Extract both text and images from the PDF file.    

        Returns:    
            Dict containing extracted text and images    
        """    
        try:    
            self.logger.info(f"Extrahiere Inhalt aus: {self.file_path}")    
            text = self.extract_text()    
            images = self.extract_images()    

            return {    
                'text': text,    
                'images': images,    
                'tables': []  # Placeholder for future table extraction    
            }    
        except Exception as e:    
            self.logger.error(f"Fehler bei der Extraktion: {str(e)}")    
            raise    

    def extract_text(self) -> str:    
        """    
        Extract text content from the PDF file.    

        Returns:    
            str: Extracted text content    

        Raises:    
            Exception: If text extraction fails    
        """    
        try:    
            self.logger.info("Extrahiere Text...")    
            text = extract_text(str(self.file_path))    
            if not text:    
                self.logger.warning("Kein Text gefunden")    
                return ""    
            return text.strip()    
        except Exception as e:    
            self.logger.error(f"Fehler bei der Textextraktion: {str(e)}")    
            raise    

    def extract_images(self) -> List[Dict[str, Any]]:    
        """    
        Extract and process images from the PDF file.    

        Returns:    
            List[Dict[str, Any]]: List of image dictionaries containing extracted data    

        Raises:    
            Exception: If image extraction fails    
        """    
        try:    
            self.logger.info("Extrahiere Bilder...")    
            pages = convert_from_path(str(self.file_path))    
            images = []    

            for i, page in enumerate(pages, 1):    
                self.logger.debug(f"Verarbeite Seite {i}/{len(pages)}")    
                try:    
                    # Extrahiere Text aus dem Bild  
                    text = pytesseract.image_to_string(    
                        page,    
                        lang='deu+eng',  # Unterstützung für Deutsch und Englisch    
                        config='--psm 3'  # Automatische Seitensegmentierung    
                    )    

                    # Erstelle ein Dictionary mit Bildinformationen  
                    if text.strip():    
                        image_info = {  
                            'id': i,  
                            'text': text.strip(),  
                            'format': 'unknown',  # Optional: Format des Bildes  
                            'size': page.size,    # Optional: Größe des Bildes  
                            'dpi': 72,            # Standard-DPI  
                            'page_number': i  
                        }  
                        images.append(image_info)  

                except Exception as e:    
                    self.logger.warning(f"Fehler bei OCR auf Seite {i}: {str(e)}")    
                    continue    

            return images    
        except Exception as e:    
            self.logger.error(f"Fehler bei der Bildextraktion: {str(e)}")    
            raise    

    def get_metadata(self) -> Optional[Dict]:    
        """    
        Extract metadata from the PDF file (placeholder for future implementation).    

        Returns:    
            Optional[Dict]: PDF metadata or None if extraction fails    
        """    
        # TODO: Implement metadata extraction    
        return None    


if __name__ == "__main__":    
    # Setup logging for standalone testing    
    logging.basicConfig(    
        level=logging.INFO,    
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'    
    )    

    # Example usage and testing    
    try:    
        # Replace with an actual PDF path for testing    
        test_pdf = "/path/to/test.pdf"    
        handler = PDFHandler(test_pdf)    
        content = handler.extract_content()    
        print("Extracted Text:", content['text'][:200] + "..." if content['text'] else "No text found")    
        print("Number of images processed:", len(content['images']))    
    except Exception as e:    
        logging.error(f"Test failed: {str(e)}")    
```

#### **Processor erstellen**  
Erstellen Sie einen Ordner für Processor und die Datei `content_processor.py`:

```
mkdir src/processors touch src/processors/content_processor.py
```

Fügen Sie den folgenden Code in `content_processor.py` ein:
```
from typing import List, Dict, Any, Optional  
import logging  

class ContentProcessor:  
    """Processes extracted content from PDF files."""  

    def __init__(self):  
        self.logger = logging.getLogger(__name__)  

    def process_images(self, images: List[Dict[str, Any]]) -> List[Dict[str, Any]]:  
        """Process images extracted from the PDF.  

        Args:  
            images (List[Dict[str, Any]]): List of image dictionaries.  

        Returns:  
            List[Dict[str, Any]]: List of processed image dictionaries.  
        """  
        self.logger.info("Verarbeite Bilder...")  
        if not isinstance(images, list):  
            self.logger.error("Images must be provided as a list")  
            raise TypeError("Images must be provided as a list")  

        processed_images = []  

        for img in images:  
            try:  
                if not isinstance(img, dict):  
                    self.logger.error("Image must be provided as a dictionary")  
                    raise TypeError("Image must be provided as a dictionary")  

                processed_img = self._process_single_image(img)  
                if processed_img:  
                    processed_images.append(processed_img)  
            except Exception as e:  
                self.logger.warning(f"Fehler bei der Bildverarbeitung: {str(e)}")  
                continue  

        return processed_images  

    def _process_single_image(self, image: Dict[str, Any]) -> Optional[Dict[str, Any]]:  
        """Process a single image.  

        Args:  
            image (Dict[str, Any]): Image dictionary.  

        Returns:  
            Optional[Dict[str, Any]]: Processed image dictionary or None.  
        """  
        # Hier kann die Bildverarbeitung implementiert werden  
        return image  # Placeholder für die Bildverarbeitung  

    def process_text(self, text: str) -> str:  
        """Process extracted text.  

        Args:  
            text (str): Extracted text.  

        Returns:  
            str: Processed text.  
        """  
        self.logger.info("Verarbeite Text...")  
        # Hier kann die Textverarbeitung implementiert werden  
        return text  # Placeholder für die Textverarbeitung  

    def process_tables(self, tables: List[Dict[str, Any]]) -> List[Dict[str, Any]]:  
        """Process extracted tables.  

        Args:  
            tables (List[Dict[str, Any]]): List of table dictionaries.  

        Returns:  
            List[Dict[str, Any]]: List of processed table dictionaries.  
        """  
        self.logger.info("Verarbeite Tabellen...")  
        # Hier kann die Tabellenverarbeitung implementiert werden  
        return tables  # Placeholder für die Tabellenverarbeitung  
```

#### **Converter erstellen**  
Erstellen Sie einen Ordner für Converter und die Datei `markdown_converter.py`:
```
mkdir src/converters touch src/converters/markdown_converter.py
```

Fügen Sie den folgenden Code in `markdown_converter.py` ein:
```
from typing import List, Dict  

class MarkdownConverter:  
    """Converts extracted content to Markdown format."""  

    def convert_text(self, text: str) -> str:  
        """Convert text to Markdown format.  

        Args:  
            text (str): Text to convert.  

        Returns:  
            str: Converted Markdown text.  
        """  
        # Hier kann die Textkonvertierung implementiert werden  
        return text  # Placeholder für die Textkonvertierung  

    def convert_images(self, images: List[Dict[str, Any]]) -> str:  
        """Convert images to Markdown format.  

        Args:  
            images (List[Dict[str, Any]]): List of image dictionaries.  

        Returns:  
            str: Markdown formatted images.  
        """  
        markdown_images = []  
        for img in images:  
            if 'text' in img:  
                markdown_images.append(f"![Image {img['id']}]({img['text']})")  # Beispiel für die Markdown-Darstellung  
        return "\n".join(markdown_images)  

    def convert_tables(self, tables: List[Dict[str, Any]]) -> str:  
        """Convert tables to Markdown format.  

        Args:  
            tables (List[Dict[str, Any]]): List of table dictionaries.  

        Returns:  
            str: Markdown formatted tables.  
        """  
        # Hier kann die Tabellenkonvertierung implementiert werden  
        return ""  # Placeholder für die Tabellenkonvertierung  
```

#### **Validator erstellen**  
Erstellen Sie einen Ordner für Validator und die Datei `validation_engine.py`:

```
mkdir src/validators touch src/validators/validation_engine.py
```
Fügen Sie den folgenden Code in `validation_engine.py` ein:
```
#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  

"""  
Validation Engine für PDF zu Markdown Konverter  
Überprüft die Qualität und Vollständigkeit der Konvertierung.  
"""  

from typing import Optional, Dict, Any  
import difflib  
import re  

class ValidationEngine:  
    """  
    Engine zur Validierung der Konvertierung von PDF zu Markdown.  
    Führt verschiedene Prüfungen durch, um die Qualität der Konvertierung sicherzustellen.  
    """  

    def __init__(self, similarity_threshold: float = 0.8):  
        """  
        Initialisiert die ValidationEngine.  

        Args:  
            similarity_threshold: Schwellenwert für die Ähnlichkeit (0.0 bis 1.0)  
        """  
        self.similarity_threshold = similarity_threshold  

    def validate(self, original: str, converted: str, metadata: Optional[Dict[str, Any]] = None) -> bool:  
        """  
        Führt die Validierung der konvertierten Inhalte durch.  

        Args:  
            original: Originaltext aus dem PDF  
            converted: Konvertierter Markdown-Text  
            metadata: Optional - Zusätzliche Metadaten für erweiterte Validierung  

        Returns:  
            bool: True wenn die Validierung erfolgreich war, sonst False  
        """  
        if not original or not converted:  
            return False  

        # Grundlegende Textbereinigung  
        original_clean = self._clean_text(original)  
        converted_clean = self._clean_text(converted)  

        # Führe verschiedene Validierungen durch  
        validations = [  
            self._validate_content_similarity(original_clean, converted_clean),  
            self._validate_structure(converted),  
            self._validate_length(original_clean, converted_clean)  
        ]  

        # Wenn metadata vorhanden ist, führe zusätzliche Validierungen durch  
        if metadata:  
            validations.append(self._validate_metadata(converted, metadata))  

        # Validierung ist erfolgreich, wenn alle Prüfungen bestanden wurden  
        return all(validations)  

    def _clean_text(self, text: str) -> str:  
        """  
        Bereinigt den Text für den Vergleich.  

        Args:  
            text: Zu bereinigender Text  

        Returns:  
            str: Bereinigter Text  
        """  
        # Entferne Whitespace und vereinheitliche Zeilenumbrüche  
        text = re.sub(r'\s+', ' ', text)  
        # Entferne Markdown-Formatierung für den Vergleich  
        text = re.sub(r'[#*_`~$$()]', '', text)  
        return text.strip().lower()  

    def _validate_content_similarity(self, original: str, converted: str) -> bool:  
        """  
        Überprüft die Ähnlichkeit zwischen Original und konvertiertem Text.  

        Args:  
            original: Bereinigter Originaltext  
            converted: Bereinigter konvertierter Text  

        Returns:  
            bool: True wenn die Texte ausreichend ähnlich sind  
        """  
        # Berechne Ähnlichkeit mit SequenceMatcher  
        similarity = difflib.SequenceMatcher(None, original, converted).ratio()  
        return similarity >= self.similarity_threshold  

    def _validate_structure(self, converted: str) -> bool:  
        """  
        Überprüft die Markdown-Struktur auf Gültigkeit.  

        Args:  
            converted: Konvertierter Markdown-Text  

        Returns:  
            bool: True wenn die Struktur gültig ist  
        """  
        # Überprüfe grundlegende Markdown-Syntax  
        valid_headings = all(re.match(r'^#{1,6}\s', line)   
                           for line in converted.split('\n')   
                           if line.startswith('#'))  

        # Überprüfe geschlossene Markdown-Elemente  
        balanced_elements = self._check_balanced_elements(converted)  

        return valid_headings and balanced_elements  

    def _validate_length(self, original: str, converted: str) -> bool:  
        """  
        Überprüft, ob die Länge des konvertierten Texts plausibel ist.  

        Args:  
            original: Bereinigter Originaltext  
            converted: Bereinigter konvertierter Text  

        Returns:  
            bool: True wenn die Länge plausibel ist  
        """  
        # Erlaubte Abweichung in Prozent  
        max_length_difference = 0.3  

        original_length = len(original)  
        converted_length = len(converted)  

        if original_length == 0:  
            return False  

        length_ratio = abs(converted_length - original_length) / original_length  
        return length_ratio <= max_length_difference  

    def _validate_metadata(self, converted: str, metadata: Dict[str, Any]) -> bool:  
        """  
        Überprüft, ob wichtige Metadaten im konvertierten Text vorhanden sind.  

        Args:  
            converted: Konvertierter Markdown-Text  
            metadata: Metadaten aus dem Original  

        Returns:  
            bool: True wenn alle erforderlichen Metadaten vorhanden sind  
        """  
        if not metadata:  
            return True  

        # Überprüfe ob Titel vorhanden ist (falls in Metadaten angegeben)  
        if 'title' in metadata:  
            title = metadata['title']  
            if title and not re.search(rf'\b{re.escape(title)}\b', converted, re.IGNORECASE):  
                return False  

        return True  

    def _check_balanced_elements(self, text: str) -> bool:  
        """  
        Überprüft, ob Markdown-Elemente korrekt geschlossen sind.  

        Args:  
            text: Zu überprüfender Text  

        Returns:  
            bool: True wenn alle Elemente korrekt geschlossen sind  
        """  
        # Überprüfe Paare von Markdown-Elementen  
        pairs = {  
            '`': '`',  
            '**': '**',  
            '*': '*',  
            '_': '_',  
            '[': ']'  
        }  

        stack = []  

        for line in text.split('\n'):  
            for i, char in enumerate(line):  
                if char in pairs.keys():  
                    stack.append(char)  
                elif char in pairs.values():  
                    if not stack:  
                        return False  
                    if pairs[stack[-1]] != char:  
                        return False  
                    stack.pop()  

        return len(stack) == 0  
```


#### **ErrorHandler und Logger erstellen**  
Erstellen Sie die entsprechenden Dateien in `src/handlers`:
```
touch src/handlers/error_handler.py 
touch src/handlers/logger.py
```

Fügen Sie in `error_handler.py` den folgenden Code ein:

```
import logging  

class ErrorHandler:  
    """Centralized error handling for the application."""  

    def __init__(self):  
        self.logger = logging.getLogger(__name__)  

    def log_error(self, message: str):  
        """Log an error message.  

        Args:  
            message (str): Error message to log.  
        """  
        self.logger.error(message)  

    def log_warning(self, message: str):  
        """Log a warning message.  

        Args:  
            message (str): Warning message to log.  
        """  
        self.logger.warning(message)  

    def handle_exception(self, e: Exception):  
        """Handle exceptions and log them.  

        Args:  
            e (Exception): Exception to handle.  
        """  
        self.log_error(f"An error occurred: {str(e)}")  
```

Und in `logger.py`:
```
import logging  

def setup_logger(name: str, log_file: str, level=logging.INFO):  
    """Setup a logger with the specified name and log file.  

    Args:  
        name (str): Name of the logger.  
        log_file (str): Log file path.  
        level (int): Logging level.  
    """  
    handler = logging.FileHandler(log_file)          
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))  

    logger = logging.getLogger(name)  
    logger.setLevel(level)  
    logger.addHandler(handler)  

    return logger   
```

## 5. Anwendung testen

### 5.1 Testen der Anwendung

1. **PDF-Datei vorbereiten:**  
    Stellen Sie sicher, dass Sie eine PDF-Datei haben, die Sie konvertieren möchten. Legen Sie diese Datei im Hauptverzeichnis Ihres Projekts ab.
    
2. **Anwendung ausführen:**  
    Geben Sie im Terminal den folgenden Befehl ein, um die Anwendung auszuführen:

```
python src/main.py input.pdf output.md --verbose
```

Ersetzen Sie `/Users/skr/neomint-research/pdf_to_markdown/path/to/your/input.pdf` durch den Pfad zu Ihrer PDF-Datei und `/Users/skr/neomint-research/pdf_to_markdown/path/to/your/output.md` durch den gewünschten Pfad für die Markdown-Ausgabedatei.

### 5.2 Überprüfen der Ausgabe

Öffnen Sie die generierte Markdown-Datei mit einem Texteditor, um sicherzustellen, dass die Konvertierung erfolgreich war.

## 6. Fehlerbehebung

Falls Sie auf Probleme stoßen:

- **Überprüfen Sie die Fehlermeldungen im Terminal.** Diese geben Ihnen Hinweise darauf, was schiefgelaufen ist.
- **Stellen Sie sicher, dass alle Bibliotheken korrekt installiert sind.** Führen Sie den Installationsbefehl erneut aus, wenn nötig.
- **Überprüfen Sie den Pfad zu Ihrer PDF-Datei.** Stellen Sie sicher, dass die Datei existiert und der Pfad korrekt ist.

## 7. Nächste Schritte

- **Erweiterungen:** Sie können die Anwendung erweitern, indem Sie zusätzliche Funktionen hinzufügen, wie z.B. die Verarbeitung von Tabellen oder die Verbesserung der Fehlerbehandlung.
- **Dokumentation:** Erstellen Sie eine Dokumentation für Ihre Anwendung, um anderen Benutzern zu helfen, sie zu verwenden.