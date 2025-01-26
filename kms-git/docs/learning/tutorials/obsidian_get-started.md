---
title: Obsidian - Get Started Tutorial
author: skr
type: tutorial
publish: true
tags: 
source: 
dependencies: "[[tutorials]]"
date_created: 2024-11-28
---
---
```ad-tldr
title: TL;DR
Dieses Tutorial bietet eine umfassende Schritt-für-Schritt-Anleitung zur Installation, Konfiguration und Nutzung von Obsidian, einer leistungsstarken Notizverwaltungssoftware. Es deckt alles ab – von den Systemvoraussetzungen und der Installation bis hin zur Navigation, den Kernfunktionen wie Markdown-Syntax, internen Verknüpfungen und Community-Plugins. Zusätzlich werden grundlegende Workflows zur Organisation und Suche sowie Maßnahmen zur Fehlerbehebung und Wartung detailliert beschrieben. Der Benutzer erhält so einen klaren Leitfaden, um Obsidian schnell und effektiv in seinen Workflow zu integrieren und die Software optimal zu nutzen.

```
---
# Einführung

Dieses Tutorial führt Sie durch die Installation, Konfiguration und Nutzung von Obsidian, einer mächtigen Notizverwaltungssoftware, beginnend mit einem sauberen Betriebssystem. Es richtet sich an Nutzer ohne spezifisches Vorwissen über Obsidian, die aber ein grundlegendes Verständnis von IT-Konzepten besitzen.

# Im Detail

## 0. Systemvoraussetzungen & Vorbereitung

### Zweck
Sicherstellen, dass Ihr System die Anforderungen für die Nutzung von Obsidian erfüllt und alle notwendigen Voraussetzungen erfüllt sind.

### Voraussetzungen
- **Betriebssystem**: Windows 10/11, macOS 11+ oder eine aktuelle Linux-Distribution.
- **Speicherplatz**: Mindestens 150 MB freier Speicherplatz.
- **Internetverbindung**: Zum Herunterladen der Installationsdatei.
- **Berechtigungen**: Administratorrechte zur Installation von Software.

### Durchführung

1. **Prüfen des Betriebssystems**:
   - **Aktion**: Öffnen Sie die Systeminformationen Ihres Computers.
     - **Windows**: `Windows-Taste` > `Systeminformationen`.
     - **macOS**: Apple-Menü > `Über diesen Mac`.
     - **Linux**: Terminal öffnen und `uname -a` ausführen.
   - **Erwartetes Ergebnis**: Betriebssystemdetails sind sichtbar.
   - **Validierung**: Stellen Sie sicher, dass die Mindestanforderungen erfüllt sind.

2. **Bereitstellen von Speicherplatz**:
   - **Aktion**: Überprüfen Sie den verfügbaren Speicherplatz.
     - **Windows/macOS**: `Dateiexplorer` > Eigenschaften der Festplatte.
     - **Linux**: Terminal-Befehl `df -h`.
   - **Erwartetes Ergebnis**: Mindestens 150 MB verfügbarer Speicherplatz.

3. **Überprüfen der Internetverbindung**:
   - **Aktion**: Testen Sie die Verbindung, indem Sie `speedtest.net` aufrufen.
   - **Erwartetes Ergebnis**: Stabile Verbindung mit mindestens 1 Mbps.

### Fehlerbehebung
- **Problem**: Betriebssystem wird nicht unterstützt.
  - **Ursache**: Veraltetes System.
  - **Lösung**: Aktualisieren Sie Ihr Betriebssystem gemäß den Anweisungen des Herstellers.
- **Problem**: Zu wenig Speicherplatz.
  - **Ursache**: Unnötige Dateien blockieren Speicher.
  - **Lösung**: Löschen Sie unnötige Dateien oder verschieben Sie Daten auf externe Speicher.

---

## 1. Download & Verifizierung

### Zweck
Herunterladen der Obsidian-Installationsdatei und Verifizierung ihrer Authentizität.

### Voraussetzungen
- **Internetverbindung**.
- **Ein Browser**, z. B. Chrome, Firefox, oder Safari.

### Durchführung

1. **Herunterladen der Installationsdatei**:
   - **Aktion**: Besuchen Sie die [offizielle Obsidian-Website](https://obsidian.md).
   - **Aktion**: Klicken Sie auf den Button `Download`.
     - **Windows**: `.exe`-Datei.
     - **macOS**: `.dmg`-Datei.
     - **Linux**: `.AppImage` oder über Paketmanager.
   - **Erwartetes Ergebnis**: Die Installationsdatei wird im Download-Ordner gespeichert.
   - **Validierung**: Prüfen Sie den Dateinamen und die Dateigröße (ca. 75 MB).

2. **Verifizieren der Datei**:
   - **Aktion**: Laden Sie die Prüfsumme von der Obsidian-Website herunter.
   - **Aktion**: Führen Sie ein Verifizierungs-Tool aus:
     - **Windows**: Nutzen Sie `CertUtil` im Terminal: `CertUtil -hashfile [Dateipfad] SHA256`.
     - **macOS/Linux**: Terminal-Befehl `shasum -a 256 [Dateipfad]`.
   - **Erwartetes Ergebnis**: Die berechnete Prüfsumme stimmt mit der auf der Website bereitgestellten überein.

### Fehlerbehebung
- **Problem**: Prüfsumme stimmt nicht überein.
  - **Ursache**: Beschädigte Datei.
  - **Lösung**: Laden Sie die Datei erneut herunter.

---

## 2. Installation & Grundkonfiguration

### Zweck
Installieren von Obsidian und Einrichten der grundlegenden Konfiguration.

### Voraussetzungen
- **Heruntergeladene und verifizierte Installationsdatei**.

### Durchführung

1. **Installation starten**:
   - **Aktion**: Doppelklicken Sie auf die Installationsdatei.
     - **Windows**: `ObsidianSetup.exe`.
     - **macOS**: Ziehen Sie das Obsidian-Icon in den `Applications`-Ordner.
     - **Linux**: Führen Sie die `.AppImage`-Datei aus oder nutzen Sie den Paketmanager.
   - **Erwartetes Ergebnis**: Der Installationsassistent startet.

2. **Installationsanweisungen folgen**:
   - **Aktion**: Akzeptieren Sie die Lizenzvereinbarung und wählen Sie den Installationspfad.
   - **Erwartetes Ergebnis**: Obsidian wird erfolgreich installiert.
   - **Validierung**: Starten Sie die Anwendung über das Startmenü (Windows) oder den Finder (macOS).

3. **Erste Konfiguration**:
   - **Aktion**: Beim ersten Start wird ein neuer „Vault“ erstellt.
     - **Name**: Geben Sie „MeinErsterVault“ ein.
     - **Speicherort**: Wählen Sie einen Ordner, z. B. `Dokumente/ObsidianVaults`.
   - **Erwartetes Ergebnis**: Ein neuer Vault wird erstellt und geöffnet.

### Fehlerbehebung
- **Problem**: Installation schlägt fehl.
  - **Ursache**: Fehlende Administratorrechte.
  - **Lösung**: Führen Sie die Datei als Administrator aus.
- **Problem**: Anwendung startet nicht.
  - **Ursache**: Veraltete Systemkomponenten.
  - **Lösung**: Aktualisieren Sie Ihr Betriebssystem.

---
## 3. Erste Schritte & Navigation

### Zweck
Verstehen der Benutzeroberfläche und der grundlegenden Navigation in Obsidian.

### Voraussetzungen
- Erfolgreiche Installation und Erstellung eines Vaults.

### Durchführung

1. **Obsidian starten**:
   - **Aktion**: Öffnen Sie Obsidian über das Startmenü (Windows) oder den Finder (macOS).
   - **Erwartetes Ergebnis**: Obsidian öffnet Ihren zuletzt verwendeten Vault.

2. **Hauptoberfläche verstehen**:
   - **Aktion**: Erkunden Sie die wichtigsten Bereiche:
     - **Seitenleiste**: Zugriff auf Dateien, Suchfunktion und Plugins.
     - **Hauptbereich**: Bearbeitung und Anzeige von Notizen.
     - **Statusleiste**: Zeigt den aktuellen Modus (Bearbeiten oder Vorschau).
   - **Erwartetes Ergebnis**: Sie erkennen die Funktion jedes Bereichs.
   - **Validierung**: Bewegen Sie den Mauszeiger über die Symbole; ein Tooltip beschreibt die Funktion.

3. **Erstellen einer ersten Notiz**:
   - **Aktion**: Klicken Sie oben links auf das Symbol `+` (Neue Notiz).
   - **Aktion**: Geben Sie „Meine Erste Notiz“ als Titel ein.
   - **Aktion**: Schreiben Sie einen Text, z. B. „Das ist mein erster Eintrag in Obsidian.“
   - **Erwartetes Ergebnis**: Die Notiz wird automatisch im Vault gespeichert.
   - **Validierung**: Überprüfen Sie den Dateinamen im Dateibrowser der Seitenleiste.

4. **Verknüpfungen erstellen**:
   - **Aktion**: Schreiben Sie `[[Verknüpfte Notiz]]` in den Text und speichern Sie.
   - **Aktion**: Klicken Sie auf den Link; Obsidian erstellt automatisch eine neue Notiz.
   - **Erwartetes Ergebnis**: Die neue Notiz wird im Hauptbereich geöffnet.
   - **Validierung**: Überprüfen Sie, ob „Verknüpfte Notiz“ im Dateibrowser erscheint.

### Fehlerbehebung

- **Problem**: Änderungen werden nicht gespeichert.
  - **Ursache**: Schreibrechte im Vault-Ordner fehlen.
  - **Lösung**: Überprüfen und ändern Sie die Zugriffsrechte des Vault-Ordners.
- **Problem**: Links funktionieren nicht.
  - **Ursache**: Falsche Syntax.
  - **Lösung**: Überprüfen Sie, ob der Text innerhalb von `[[ ]]` korrekt geschrieben wurde.

---

## 4. Kernfunktionen

### Zweck
Erlernen der zentralen Funktionen von Obsidian, wie Verknüpfungen, Markdown-Syntax und Plugins.

### Voraussetzungen
- Basiskenntnisse der Navigation.

### Durchführung

#### 4.1 Verknüpfte Notizen

1. **Erstellen interner Links**:
   - **Aktion**: Schreiben Sie in einer Notiz `[[Name der Notiz]]`.
   - **Erwartetes Ergebnis**: Ein klickbarer Link erscheint.
   - **Validierung**: Klicken Sie auf den Link, um die Zielnotiz zu öffnen.

2. **Anzeige verlinkter Notizen**:
   - **Aktion**: Öffnen Sie die Seitenleiste und aktivieren Sie das **Backlink-Panel**.
   - **Erwartetes Ergebnis**: Alle Notizen, die auf die aktuelle verlinken, werden angezeigt.

#### 4.2 Markdown-Syntax

1. **Formatierungen**:
   - **Aktion**: Nutzen Sie folgende Markdown-Befehle:
     - **Fett**: `**Text**`
     - **Kursiv**: `*Text*`
     - **Überschrift**: `# Überschrift`
   - **Erwartetes Ergebnis**: Vorschau zeigt die formatierten Inhalte korrekt.
   - **Validierung**: Wechseln Sie zwischen Bearbeitungs- und Vorschau-Modus.

2. **Erstellen von Listen**:
   - **Aktion**: Schreiben Sie:
     ```markdown
     - Punkt 1
     - Punkt 2
         - Unterpunkt
     ```
   - **Erwartetes Ergebnis**: Eine hierarchische Liste erscheint in der Vorschau.

#### 4.3 Plugins

1. **Aktivieren von Plugins**:
   - **Aktion**: Öffnen Sie `Einstellungen` > `Core Plugins`.
   - **Aktion**: Aktivieren Sie das Plugin `Tag-Pane`.
   - **Erwartetes Ergebnis**: Ein neues Panel für Tags erscheint in der Seitenleiste.
   - **Validierung**: Erstellen Sie eine Notiz mit `#BeispielTag` und überprüfen Sie, ob der Tag im Panel sichtbar ist.

### Fehlerbehebung

- **Problem**: Markdown wird nicht korrekt angezeigt.
  - **Ursache**: Fehlerhafte Syntax.
  - **Lösung**: Vergleichen Sie Ihre Eingabe mit der Markdown-Dokumentation.

---

## 5. Basis-Workflows

### Zweck
Erlernen grundlegender Arbeitsabläufe, z. B. Notizen organisieren und Suchfunktionen nutzen.

### Voraussetzungen
- Verständnis der Kernfunktionen.

### Durchführung

#### 5.1 Organisieren von Notizen

1. **Ordner erstellen**:
   - **Aktion**: Rechtsklick im Dateibrowser > `Neuer Ordner`.
   - **Aktion**: Benennen Sie den Ordner, z. B. „Projekte“.
   - **Erwartetes Ergebnis**: Ein neuer Ordner erscheint im Vault.
   - **Validierung**: Ziehen Sie bestehende Notizen in den Ordner und prüfen Sie die neue Struktur.

2. **Tags verwenden**:
   - **Aktion**: Fügen Sie `#TagName` in einer Notiz hinzu.
   - **Aktion**: Öffnen Sie das Tag-Panel, um alle Notizen mit diesem Tag anzuzeigen.
   - **Erwartetes Ergebnis**: Die Notiz erscheint unter dem Tag im Panel.

#### 5.2 Suchfunktion

1. **Durchsuchen des Vaults**:
   - **Aktion**: Nutzen Sie die Suchleiste (Tastenkombination `Ctrl+F` oder `Cmd+F`).
   - **Aktion**: Geben Sie „Erste Notiz“ ein.
   - **Erwartetes Ergebnis**: Alle Notizen mit diesem Text erscheinen in der Ergebnisliste.

### Fehlerbehebung

- **Problem**: Tags werden nicht erkannt.
  - **Ursache**: Falsche Syntax (`#` fehlt).
  - **Lösung**: Prüfen und korrigieren Sie den Tag.

---

## 6. Troubleshooting & Wartung

### Zweck
Behebung typischer Fehler und Pflege Ihres Vaults.

### Voraussetzungen
- Mindestens ein funktionierender Vault.

### Durchführung

#### 6.1 Backups erstellen

1. **Manuelles Backup**:
   - **Aktion**: Kopieren Sie den Vault-Ordner auf ein externes Laufwerk.
   - **Erwartetes Ergebnis**: Eine exakte Kopie des Vaults wird gespeichert.
   - **Validierung**: Öffnen Sie die Kopie in Obsidian, um die Funktionsfähigkeit zu testen.

2. **Automatisierte Backups**:
   - **Aktion**: Nutzen Sie Tools wie `Dropbox` oder `OneDrive`.
   - **Aktion**: Synchronisieren Sie den Vault-Ordner mit dem Dienst.
   - **Erwartetes Ergebnis**: Änderungen werden automatisch gesichert.

#### 6.2 Behebung von Performance-Problemen

1. **Plugins deaktivieren**:
   - **Aktion**: Öffnen Sie `Einstellungen` > `Core Plugins` und deaktivieren Sie unnötige Plugins.
   - **Erwartetes Ergebnis**: Die Geschwindigkeit von Obsidian verbessert sich.
   - **Validierung**: Testen Sie das Laden und Bearbeiten von Notizen.

2. **Vault optimieren**:
   - **Aktion**: Entfernen Sie überflüssige Dateien aus dem Vault.
   - **Aktion**: Nutzen Sie die Option `Rebuild Index` in den Einstellungen.
   - **Erwartetes Ergebnis**: Der Vault reagiert schneller auf Eingaben.

### Fehlerbehebung

- **Problem**: Vault wird nicht geladen.
  - **Ursache**: Beschädigte Konfigurationsdatei.
  - **Lösung**: Erstellen Sie einen neuen Vault und kopieren Sie die Notizen.

## Obsidian Community Plugins

Community-Plugins in Obsidian erweitern die Funktionalität der Anwendung erheblich, indem sie von der Nutzer-Community entwickelte Features integrieren. Diese Plugins ermöglichen es, Obsidian individuell anzupassen und den eigenen Workflow zu optimieren.

---

### Installation von Community-Plugins

#### Voraussetzungen
- Obsidian ist installiert und einsatzbereit.
- Internetverbindung zum Herunterladen der Plugins.

#### Durchführung

1. **Community-Plugins aktivieren**:
   - Öffnen Sie die **Einstellungen** in Obsidian.
   - Navigieren Sie zum Abschnitt **Community-Plugins**.
   - Deaktivieren Sie den **Eingeschränkten Modus**, um die Installation von Community-Plugins zu ermöglichen.

2. **Plugins durchsuchen und installieren**:
   - Klicken Sie auf **"Durchsuchen"**, um den Plugin-Browser zu öffnen.
   - Verwenden Sie die Suchfunktion, um nach spezifischen Plugins zu suchen, oder stöbern Sie durch die verfügbaren Plugins.
   - Wählen Sie ein gewünschtes Plugin aus und klicken Sie auf **"Installieren"**.
   - Nach der Installation klicken Sie auf **"Aktivieren"**, um das Plugin zu nutzen.

---

### Beliebte Community-Plugins

#### 1. Dataview
- **Funktion**: Ermöglicht die Erstellung von dynamischen Ansichten und Abfragen innerhalb Ihrer Notizen, ähnlich einer Datenbankfunktion.
- **Nützlich für**: Datenbankähnliche Abfragen, z. B. Aufgabenlisten oder Projektübersichten.

#### 2. Templater

- **Funktion**: Bietet erweiterte Vorlagenfunktionen mit Unterstützung für Skripte, um wiederkehrende Inhalte effizienter zu erstellen.
- **Nützlich für**: Automatisierung von wiederkehrenden Notizinhalten.

#### 3. Calendar

- **Funktion**: Fügt einen Kalender in die Seitenleiste ein, der die Navigation und Organisation von täglichen Notizen erleichtert.
- **Nützlich für**: Strukturierte Tages- und Wochenplanung.

# Weiterführende Quellen
