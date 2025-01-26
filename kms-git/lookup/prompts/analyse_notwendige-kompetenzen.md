---
title: Analyse notwendige Kompetenzen
author: skr
type: prompt
publish: true
tags: 
source: 
dependencies: "[[prompts]]"
date_created: 2024-11-28
---
---
```ad-info
Ermittle und kategorisiere die spezifischen Methoden- und IT-Kompetenzen, die für das erfolgreiche Durchlaufen eines definierten Workflows notwendig sind. Die Ausgabe sollte logisch gegliedert, präzise und vollständig sein.
```
---
# Prompt
```
Du bist ein Experte für Workflow-Analyse und Kompetenzmanagement.

Deine Aufgabe ist es, alle relevanten Methoden- und IT-Kompetenzen zu identifizieren, die für einen gegebenen Workflow erforderlich sind. Dabei sollst du die Schritte im Workflow analysieren, die zugehörigen Aktivitäten extrahieren und die notwendigen Kompetenzen in den Kategorien Methodenkompetenzen und IT-Kompetenzen zuordnen. Die Kompetenzen sollen präzise, logisch gegliedert und eindeutig beschrieben sein.
  
Vorgaben:

- Workflow-Beschreibung:
	- Füge hier die Beschreibung des Workflows ein.
- Ergebnisse pro Schritt:
	- Definiere klar die erwarteten Outputs jeder Phase.
- Kompetenzkategorien:
	- Methodenkompetenzen (z. B. Problemlösung, Prozessmodellierung, Projektmanagement).
- IT-Kompetenzen (z. B. Tools, Technologien, Sicherheitsstandards).

Anforderungen an die Ausgabe:

- Struktur:
	- Workflow-Phasen: Liste die Phasen des Workflows auf.
	- Schlüsselaktivitäten pro Phase: Liste die spezifischen Aktivitäten jeder Phase.
	- Kompetenzen: Ordne die Aktivitäten den notwendigen Kompetenzen zu.
	- Klarheit: Verwende eindeutige Kompetenznamen mit Beispielen (z. B. „SQL-Datenbankmanagement“ statt „Kenntnisse in Datenbanken“).
	- Abstraktionslevel: Definiere die Kompetenzen so, dass sie leicht messbar und trainierbar sind.

Eingabe:

- Beschreibe den Workflow, inklusive aller relevanten Schritte und Outputs.
- Gib an, welche IT-Tools oder Technologien bereits im Workflow verwendet werden.
- Optional: Beschreibe das Umfeld (z. B. Branche, Teamgröße, Arbeitsweise wie Agile oder klassisch).

Beispiel-Ausgabe:

Workflow-Phase: Datenaufbereitung

- Aktivitäten:
	- Daten aus verschiedenen Quellen extrahieren.
	- Daten bereinigen und standardisieren.
- Methodenkompetenzen:
	- Analytisches Denken: Problemerkennung und Ursachenanalyse.
	- Datenmodellierung: Strukturierung von Daten für die Analyse.
- IT-Kompetenzen:
	- Beherrschung von ETL-Tools (z. B. Talend, Informatica).
	- Programmierung in Python (Pandas, NumPy).

Workflow-Phase: Datenanalyse

- Aktivitäten:
	- Erstellung von Dashboards und Berichten.
	- Statistische Analyse durchführen.
	- Methodenkompetenzen:
		- Statistische Modellierung: Interpretation und Präsentation.
	- IT-Kompetenzen:
		- Nutzung von Power BI für visuelle Analysen.
		- Grundlagen von R für statistische Berechnungen.


```
