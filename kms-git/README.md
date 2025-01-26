---
title: README KMS-Repository
author: skr
type: readme
publish: true
tags: 
source: https://github.com/mint-research/kms-git
dependencies: 
date_created: 2024-11-28
---

# README: Knowledge Management System (KMS) Repository  

## Einführung  

Willkommen! Dieses Repository bildet die Arbeitsumgebung für die konzeptionelle Entwicklung eines KI-basierten Knowledge Management Systems (KMS) im akademischen Kontext. Es enthält alle notwendigen Dateien, Konfigurationen und Plugins, um ein effektives Arbeiten mit Obsidian zu ermöglichen.  

---  

## Getting Started  

### Grundlegende Nutzung  
Alle Dateien in diesem Repository sind im Markdown-Format und können mit jedem Markdown-Editor geöffnet und bearbeitet werden. Für die vollständige Nutzung der Funktionen wird jedoch empfohlen, den Ordner als Vault in **Obsidian** zu öffnen.  

### Einrichtung in Obsidian  
1. **Vault öffnen**: Öffnen Sie den Ordner in Obsidian.  
2. **Vertrauen aktivieren**: Wählen Sie beim ersten Öffnen die Option **"Dem Entwickler vertrauen"**, um die Konfiguration und Community-Plugins automatisch zu aktivieren.  
3. **Manuelle Plugin-Installation**: Falls Sie die Plugins später installieren möchten, aktivieren Sie die Community-Plugins in Obsidian und installieren Sie die folgenden Pakete:  

| **Name** | **Autor** | **Version** | **Beschreibung** |  
|----------|-----------|-------------|-------------------|  
| [**Outliner**](https://obsidian.md/plugins?id=obsidian-outliner) [⬇️](obsidian://SP-install?id=obsidian-outliner&enable=true) | [Viacheslav Slinko](https://github.com/vslinko) | 4.8.1 | Arbeiten Sie mit Listen wie in Workflowy. |  
| [**Templater**](https://obsidian.md/plugins?id=templater-obsidian) [⬇️](obsidian://SP-install?id=templater-obsidian&enable=true) | [SilentVoid](https://github.com/SilentVoid13) | 2.9.1 | Erstellung und Nutzung von Vorlagen. |  
| [**Calendar**](https://obsidian.md/plugins?id=calendar) [⬇️](obsidian://SP-install?id=calendar&enable=true) | [Liam Cain](https://github.com/liamcain/) | 1.5.10 | Kalenderansicht für tägliche Notizen. |  
| [**Dataview**](https://obsidian.md/plugins?id=dataview) [⬇️](obsidian://SP-install?id=dataview&enable=true) | [Michael Brenan](https://github.com/blacksmithgu) | 0.5.67 | Komplexe Datenansichten für datenorientierte Nutzer. |  
| [**Share my plugin list**](https://obsidian.md/plugins?id=share-my-plugin-list) [⬇️](obsidian://SP-install?id=share-my-plugin-list&enable=true) | [Benature](https://github.com/Benature) | 0.3.3 | Teilen Sie die aktivierten Plugins in Listen-/Tabellenformat. |  
| [**Advanced Tables**](https://obsidian.md/plugins?id=table-editor-obsidian) [⬇️](obsidian://SP-install?id=table-editor-obsidian&enable=true) | [Tony Grosinger](https://grosinger.net) | 0.22.1 | Verbesserte Tabellenbearbeitung und -navigation. |  
| [**Custom Frames**](https://obsidian.md/plugins?id=obsidian-custom-frames) [⬇️](obsidian://SP-install?id=obsidian-custom-frames&enable=true) | [Ellpeck](https://ellpeck.de) | 2.4.7 | Web-Apps in Obsidian-Panels integrieren. |  
| [**Custom File Explorer sorting**](https://obsidian.md/plugins?id=custom-sort) [⬇️](obsidian://SP-install?id=custom-sort&enable=true) | [SebastianMC](https://github.com/SebastianMC) | 2.1.14 | Manuelle und automatische Sortierung im Datei-Explorer. |  
| [**Style Settings**](https://obsidian.md/plugins?id=obsidian-style-settings) [⬇️](obsidian://SP-install?id=obsidian-style-settings&enable=true) | [mgmeyers](https://github.com/mgmeyers/obsidian-style-settings) | 1.0.9 | Anpassung von Themes und Plugins. |  
| [**Surfing**](https://obsidian.md/plugins?id=surfing) [⬇️](obsidian://SP-install?id=surfing&enable=true) | [Boninall & Windily-cloud](https://github.com/Quorafind) | 0.9.14 | Surfen im Internet innerhalb von Obsidian. |  
| [**Folder notes**](https://obsidian.md/plugins?id=folder-notes) [⬇️](obsidian://SP-install?id=folder-notes&enable=true) | [Lost Paul](https://github.com/LostPaul) | 1.7.32 | Erstellen von Notizen innerhalb von Ordnern. |  
| [**Admonition**](https://obsidian.md/plugins?id=obsidian-admonition) [⬇️](obsidian://SP-install?id=obsidian-admonition&enable=true) | - | 10.3.2 | Erweiterte Callouts für Obsidian. |  
| [**Waypoint**](https://obsidian.md/plugins?id=waypoint) [⬇️](obsidian://SP-install?id=waypoint&enable=true) | [Idrees Hassan](https://idreesinc.com) | 2.1.0 | Dynamische Inhaltskarten in Obsidian erstellen. |  

---  

## Struktur-Guide  

Die Struktur des Repositories ist optimiert für die Entwicklung eines lokal betriebenen, Open-Source-fokussierten, KI-basierten Knowledge Management Systems. Um sicherzustellen, dass jede Information nur einmal gespeichert wird, wird die folgende Struktur verwendet:  

### **[[docs]]**: Statische Informationen  
Diese Kategorie enthält alle statischen Inhalte, die als Referenz und Anleitung für die Nutzung des Systems dienen. Sie ist darauf ausgelegt, Wissen zu bewahren und den Benutzern eine solide Grundlage zu bieten.  

- **knowledge**:   
  - **Inhalt**: Sammlung von Wissensressourcen, die als Bibliothek für Informationen und Referenzen dient.  
  - **Nutzung**: Benutzer können auf diese Ressourcen zugreifen, um sich über relevante Themen zu informieren und bestehendes Wissen zu vertiefen.  

- **courses**:  
  - **Inhalt**: Aufgaben und Projekte, die Studierende im Rahmen ihrer Studienarbeiten erarbeiten sollen.  
  - **Nutzung**: Diese Sektion bietet eine strukturierte Übersicht über die zu bearbeitenden Aufgaben, die den Studierenden helfen, ihre Lernziele zu erreichen und den Fortschritt zu verfolgen.  

- **learning**:   
  - **Inhalt**: Guides und Tutorials, die Anleitungen und Schulungsmaterialien für die Nutzung des Systems bereitstellen.  
  - **Nutzung**: Diese Materialien helfen neuen Benutzern, sich schnell einzuarbeiten, und bieten fortgeschrittenen Benutzern tiefere Einblicke in spezifische Funktionen.  

- **processes**:   
  - **Inhalt**: Dokumentation der Abläufe zur Erstellung neuer Artefakte innerhalb des KMS, einschließlich der Schritte und Verantwortlichkeiten.  
  - **Nutzung**: Diese Informationen sind entscheidend für die Konsistenz und Effizienz bei der Erstellung neuer Inhalte und helfen, die Qualität der Ergebnisse zu sichern.  

- **products**:   
  - **Inhalt**: One-Pager, die eine Übersicht über verschiedene Softwareprodukte bieten, die im Kontext des KMS relevant sind.  
  - **Nutzung**: Benutzer können diese One-Pager nutzen, um schnell Informationen über Softwarelösungen zu erhalten, die in ihre Arbeitsabläufe integriert werden können.  

### **[[lookup]]**: Dynamische Informationen und Daten  
Diese Kategorie enthält dynamische Inhalte, die regelmäßig aktualisiert werden und für die Interaktion mit dem System und die Generierung von Inhalten entscheidend sind.  

- **contexts**:   
  - **Inhalt**: Definitionen spezifischer Kontexte, die als Eingaben für Prompts verwendet werden, um die Relevanz und Genauigkeit der generierten Inhalte zu erhöhen.  
  - **Nutzung**: Benutzer können diese Kontextdefinitionen verwenden, um präzisere und kontextbezogene Antworten von KI-gestützten Systemen zu erhalten.  

- **formats**:   
  - **Inhalt**: Vorgaben für die Struktur und das Layout von Ausgaben, um Konsistenz und Klarheit in den Ergebnissen zu gewährleisten.  
  - **Nutzung**: Diese Vorgaben helfen Benutzern, Inhalte in einem einheitlichen Format zu erstellen, was die Lesbarkeit und Verständlichkeit verbessert.  

- **templates**:   
  - **Inhalt**: Vorlagen, die in Obsidian verwendet werden können, um die Erstellung neuer Inhalte zu erleichtern und zu standardisieren.  
  - **Nutzung**: Benutzer können diese Vorlagen anpassen, um schnell neue Notizen zu erstellen, die den gewünschten Standards entsprechen.  

- **value-sheets**:   
  - **Inhalt**: Skalen-Definitionen zur Bewertung von Eigenschaften und Merkmalen, die eine objektive Analyse und Vergleichbarkeit ermöglichen.  
  - **Nutzung**: Diese Sheets unterstützen Benutzer dabei, verschiedene Optionen oder Eigenschaften systematisch zu bewerten und Entscheidungen zu treffen.  

- **workflows**:   
  - **Inhalt**: Detaillierte Beschreibungen spezifischer Umsetzungsprozesse, die die Schritte zur Durchführung von Aufgaben innerhalb des KMS festlegen.  
  - **Nutzung**: Benutzer können diese Workflows als Leitfaden verwenden, um sicherzustellen, dass alle Schritte ordnungsgemäß befolgt werden und die gewünschten Ergebnisse erzielt werden.  

### **[[workspace]]**: Temporäre Arbeitsdaten  
Diese Kategorie ist für die Verwaltung von temporären und in Bearbeitung befindlichen Daten gedacht. Sie ermöglicht eine flexible und dynamische Arbeitsweise.  

- **drafts**:   
  - **Inhalt**: Entwürfe von Inhalten, die sich derzeit in Bearbeitung befinden und noch nicht finalisiert sind.  
  - **Nutzung**: Benutzer können hier an ihren Entwürfen arbeiten, Feedback einholen und diese später in die endgültige Struktur integrieren.  

- **inbox**:   
  - **Inhalt**: Ablage für neu angelegte Notizen, die noch kategorisiert oder bearbeitet werden müssen.  
  - **Nutzung**: Diese Funktion hilft Benutzern, neue Ideen und Informationen schnell zu erfassen, bevor sie in die entsprechende Struktur eingeordnet werden.  

- **temp**:   
  - **Inhalt**: Ordner für chaotische Datenhaltung, der vorübergehende Dateien und Informationen enthält, die nicht in die Hauptstruktur integriert sind.  
  - **Nutzung**: Benutzer können diesen Ordner nutzen, um vorübergehende Notizen oder Daten zu speichern, die später sortiert oder gelöscht werden können.  

---  

## Hinweise für SMA-O WS 2024-2025  

Dieses Repository wird auch im Rahmen der Prüfungsleistung für den Kurs **SMA-O WS 2024-2025** verwendet. Weitere Informationen finden Sie hier: [[00_get-started]].  

---  

Vielen Dank für die Nutzung dieses Repositories!  
