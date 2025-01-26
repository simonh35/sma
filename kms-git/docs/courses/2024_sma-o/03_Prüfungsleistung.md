---
title: 03_Prüfungsleistung
author: skr
type: course-work
publish: true
tags: 
source: 
dependencies: "[[2024_sma-o]]"
date_created: 2025-01-02
---
---
# Aufgabenbeschreibung: Entwicklung eines lokal betriebenen, AI-basierten Wissensmanagementsystems (KMS)

## Ziel der Prüfungsleistung
Die Studierenden sollen ein lokal betriebenes, AI-basiertes Wissensmanagementsystem (KMS) entwickeln, das verschiedene Open-Source-Komponenten integriert, um wissenschaftliche Informationen effizient zu verwalten, zu durchsuchen und zu analysieren. Das System soll vollständig lokal betrieben werden, um Datenschutz und Kontrolle zu gewährleisten, und die Prinzipien wissenschaftlichen Arbeitens (z. B. Quellenangaben) einhalten.

Das KMS soll folgende Kernfunktionen bieten:
1. **Verwaltung und Auswertung von wissenschaftlichen PDFs** (über Zotero).
2. **Erstellung und Verwaltung persönlicher Notizen** (über Obsidian).
3. **Durchsuchbarkeit und Analyse der Daten** (über eine Vektorendatenbank und eine Verarbeitungsinstanz).
4. **Interaktion mit einem Chatbot**, der Informationen aus den gespeicherten Datenquellen (Zotero und Obsidian) sowie bei Bedarf aus dem Internet bereitstellt und dabei stets die Quellen angibt.

---

## Erweiterte Komponentenliste
Neben den in der Aufgabenstellung genannten Hauptkomponenten sind folgende zusätzliche Komponenten und Technologien notwendig, um die technische Umsetzung zu gewährleisten:

1. **n8n (Workflow-Automatisierung):**
   - Zur Automatisierung von Datenflüssen zwischen den verschiedenen Komponenten (z. B. Zotero, Obsidian, Vektorendatenbank, Chatbot).

2. **Python-Umgebung:**
   - Für die Verarbeitung und Tokenisierung von Daten aus Zotero und Obsidian.

3. **Vektorendatenbank (z. B. Weaviate, Milvus oder Chroma):**
   - Zum Speichern und schnellen Abrufen von tokenisierten Daten.

4. **LLM (Large Language Model):**
   - Ein lokal betriebenes Open-Source-Modell (z. B. GPT4All, LLaMA 2, oder ähnliche), das für die Verarbeitung und Beantwortung von Anfragen verwendet wird.

5. **Datenparser:**
   - Tools oder Skripte, um Daten aus Zotero (z. B. Metadaten, Annotationen) und Obsidian (z. B. Markdown-Dateien) zu extrahieren und zu verarbeiten.

6. **Datenbank für Metadaten (z. B. SQLite oder PostgreSQL):**
   - Zum Speichern von Metadaten aus Zotero und Obsidian, die nicht in der Vektorendatenbank abgelegt werden.

7. **Benutzeroberfläche für den Chatbot:**
   - Eine einfache Web- oder Desktop-Oberfläche, über die der Chatbot genutzt werden kann (z. B. Streamlit, Gradio oder eine n8n-Integration).

8. **Validierungs- und Debugging-Tools:**
   - Tools wie Logs und Debugging-Funktionen in n8n, um Fehler zu identifizieren und zu beheben.

---

## Aufgabenstellung
Die Studierenden sollen die folgenden Schritte umsetzen, um das KMS zu entwickeln:

### **1. Einrichtung der lokalen Entwicklungsumgebung**
- **Zweck:** Bereitstellung einer stabilen Basis für die Entwicklung und den Betrieb des KMS.
- **Voraussetzungen:**
  - Frisch installierte Betriebssystemumgebung (z. B. Linux oder Windows).
  - Installierte Software: Docker, Git, Python (inkl. Pip), Node.js.
- **Aufgaben:**
  1. Installieren und konfigurieren Sie Docker, um die verschiedenen Komponenten in Containern zu betreiben.
  2. Richten Sie n8n lokal ein, um Workflows zu automatisieren.
  3. Installieren Sie eine Python-Umgebung für die Datenverarbeitung.

---

### **2. Einrichtung und Konfiguration von Zotero**
- **Zweck:** Verwaltung und Annotation wissenschaftlicher PDFs.
- **Voraussetzungen:**
  - Zotero-Installation (lokal).
  - Zotero-Connector für den Browser.
- **Aufgaben:**
  1. Installieren Sie Zotero und richten Sie eine lokale Datenbank ein.
  2. Fügen Sie einige Beispiel-PDFs hinzu und testen Sie die Annotationen.
  3. Exportieren Sie Metadaten und Annotationen über die Zotero-API oder ein Plugin (z. B. Better BibTeX).

---

### **3. Einrichtung und Konfiguration von Obsidian**
- **Zweck:** Erstellung und Verwaltung persönlicher Notizen.
- **Voraussetzungen:**
  - Lokale Installation von Obsidian.
- **Aufgaben:**
  1. Installieren Sie Obsidian und richten Sie einen lokalen Vault ein.
  2. Erstellen Sie einige Beispiel-Notizen im Markdown-Format.
  3. Testen Sie die Verknüpfung von Notizen (z. B. Backlinks) und exportieren Sie die Daten.

---

### **4. Einrichtung der Vektorendatenbank**
- **Zweck:** Speicherung und schneller Abruf von tokenisierten Daten.
- **Voraussetzungen:**
  - Installation einer Open-Source-Vektorendatenbank (z. B. Weaviate, Milvus oder Chroma).
- **Aufgaben:**
  1. Installieren und konfigurieren Sie die Vektorendatenbank.
  2. Entwickeln Sie ein Skript, das Daten aus Zotero und Obsidian tokenisiert und in die Vektorendatenbank speichert.
  3. Testen Sie die Suchfunktion der Vektorendatenbank.

---

### **5. Entwicklung der Verarbeitungsinstanz**
- **Zweck:** Verarbeitung und Durchsuchbarkeit der Daten aus Zotero und Obsidian.
- **Voraussetzungen:**
  - Python-Umgebung mit NLP-Bibliotheken (z. B. spaCy, Hugging Face Transformers).
- **Aufgaben:**
  1. Entwickeln Sie ein Skript, das Daten aus Zotero und Obsidian extrahiert, tokenisiert und in die Vektorendatenbank speichert.
  2. Implementieren Sie eine Suchfunktion, die die Vektorendatenbank abfragt und Ergebnisse zurückgibt.

---

### **6. Entwicklung des Chatbots**
- **Zweck:** Interaktion mit dem Benutzer und Bereitstellung von Informationen aus Zotero, Obsidian und dem Internet.
- **Voraussetzungen:**
  - Lokales LLM (z. B. GPT4All oder LLaMA 2).
  - Benutzeroberfläche (z. B. Streamlit oder Gradio).
- **Aufgaben:**
  1. Integrieren Sie das LLM in die Verarbeitungsinstanz.
  2. Entwickeln Sie eine Benutzeroberfläche für den Chatbot.
  3. Implementieren Sie eine Logik, die Antworten priorisiert:
     - Zuerst Zotero-Daten.
     - Dann Obsidian-Daten.
     - Falls keine Antwort gefunden wird, Daten aus dem Internet.
  4. Stellen Sie sicher, dass der Chatbot bei jeder Antwort die Quelle angibt.

---

### **7. Automatisierung mit n8n**
- **Zweck:** Automatisierung der Datenflüsse zwischen den Komponenten.
- **Voraussetzungen:**
  - Lokale n8n-Instanz.
- **Aufgaben:**
  1. Erstellen Sie Workflows, um Daten aus Zotero und Obsidian regelmäßig zu synchronisieren.
  2. Automatisieren Sie die Tokenisierung und Speicherung in der Vektorendatenbank.
  3. Testen Sie die Workflows und beheben Sie mögliche Fehler.

---

### **8. Validierung und Dokumentation**
- **Zweck:** Sicherstellen, dass das System korrekt funktioniert und die Ergebnisse reproduzierbar sind.
- **Aufgaben:**
  1. Testen Sie das KMS mit Beispiel-Daten.
  2. Dokumentieren Sie die Installation, Konfiguration und Nutzung des Systems.
  3. Beschreiben Sie typische Fehler und deren Lösungen.

---

## Erwartetes Ergebnis
Am Ende der Prüfungsleistung soll ein funktionierendes, lokal betriebenes Wissensmanagementsystem vorliegen, das folgende Anforderungen erfüllt:
1. PDFs können in Zotero verwaltet und durchsucht werden.
2. Persönliche Notizen können in Obsidian erstellt und durchsucht werden.
3. Alle Daten sind in einer Vektorendatenbank gespeichert und durchsuchbar.
4. Ein Chatbot ermöglicht die Interaktion mit den gespeicherten Daten und gibt stets die Quellen an.
5. Das System ist vollständig lokal betrieben und verwendet ausschließlich Open-Source-Komponenten.

---

## Bewertungskriterien
1. **Funktionalität:** Erfüllt das KMS die beschriebenen Anforderungen?
2. **Technische Umsetzung:** Wurden die Komponenten korrekt integriert und automatisiert?
3. **Dokumentation:** Ist die Installation und Nutzung des Systems klar und verständlich dokumentiert?
4. **Fehlerbehebung:** Wurden typische Probleme identifiziert und Lösungen bereitgestellt?
5. **Wissenschaftliche Integrität:** Gibt der Chatbot die Quellen korrekt an?