---
title: Workflow 1 - Lokale Automatisierungs-Umgebung
author: skr
type: workflow
publish: true
tags: 
source: 
dependencies: "[[2024-sma]]"
date_created: 2024-11-28
---
---
```ad-tldr
title: TL;DR
Dieser Workflow zeigt Ihnen, wie Sie eine lokale Basis-Umgebung für AI-gestützte Workflows mit Docker und n8n einrichten. Durch die Installation von Docker Desktop und das Einrichten eines n8n-Containers können Sie eine flexible, anpassbare Infrastruktur schaffen, die über den Webbrowser gesteuert wird. Der Mehrwert: Eine skalierbare, einfach zu verwaltende Plattform für Automatisierung und Prozessoptimierung, die Sie Schritt für Schritt aufbauen und erweitern können.

```
---
# Einführung

Der Workflow zielt darauf ab, eine lokale Basis-Umgebung für den Betrieb einer voll-funktionalen AI-Infrastruktur aufzubauen. Dies beinhaltet die Nutzung von Docker und n8n als zentrale Komponenten, um zukünftige Automatisierungs- und Workflow-Anforderungen effizient zu unterstützen. Vorbereitende Maßnahmen umfassen das Lesen relevanter Dokumentationen und das Durcharbeiten der grundlegenden Tutorials.

# Im Detail

## Voraussetzungen

Bevor Sie beginnen, lesen Sie die Product Sheets zu den Produkten:

- [[docker\ | Docker]]
- [[n8n]]

Anschließend durchlaufen Sie die Get-Started Tutorials zu den Produkten:

- [[github_get-started| Docker-Tutorial: GetStarted]]
- [[github_get-started \ |  GitHub-Tutorial: Get Started]]

## Technology Stack

Die eingesetzten Technologien und ihre Funktion im Workflow:
	•	Docker: Verwaltung und Betrieb von Containern auf lokaler Ebene.
	•	n8n: Erstellung und Automatisierung von Workflows.
	•	Webbrowser: Zugriff auf den n8n-Editor zur visuellen Bearbeitung von Workflows.

## Detaillierte Schritte zur Einrichtung

### Umgebung auf Betriebssystem-Ebene

	1.	Docker installieren:
	•	Laden Sie Docker Desktop herunter und installieren Sie die Anwendung gemäß den Anweisungen des Herstellers.
	2.	Datenordner erstellen:
	•	Legen Sie einen neuen Ordner mit dem Namen n8n-data an einem beliebigen Speicherort auf Ihrer Festplatte an. Dieser Ordner dient als Speicherort für Containerdaten.

### Docker-Konfiguration

Schritt 1: Docker Image herunterladen

	1.	Starten Sie Docker Desktop und navigieren Sie zu Images.
	2.	Geben Sie im Suchfeld n8nio/n8n ein.
	3.	Wählen Sie die neueste Version (latest) und klicken Sie auf Pull, um das Image herunterzuladen.
	4.	Sobald der Download (ca. 1,06 GB) abgeschlossen ist, wird das Image unter Images / local angezeigt.

Schritt 2: Docker Container erstellen

	1.	Wählen Sie das heruntergeladene Image aus und klicken Sie auf Run.
	2.	In den optionalen Einstellungen konfigurieren Sie Folgendes:
	•	Container Name: z. B. n8n-container.
	•	Host Port: 5678.
	•	Volumes:
	•	Host Path: Wählen Sie den zuvor erstellten Ordner n8n-data.
	•	Container Path: /home/node/.n8n.
	3.	Lassen Sie die Umgebungsvariablen leer (falls keine spezielle Konfiguration erforderlich ist).
	4.	Starten Sie den Container.

Schritt 3: Zugriff auf den n8n-Editor

	1.	Nach dem Start des Containers wird eine URL generiert, die den Zugriff auf den n8n-Editor ermöglicht.
	2.	Bei Verwendung der Beispielkonfiguration ist der Editor unter http://localhost:5678/ erreichbar.

### Konfiguration im Webbrowser

	1.	n8n-Account anlegen:
	•	Registrieren Sie sich für ein kostenfreies Konto.
	2.	Premium Key anfordern:
	•	Falls verfügbar, nutzen Sie das Gratis-Premium-Angebot.
	3.	Kurse belegen:
	•	Absolvieren Sie die Kurse unter n8n Dokumentation, um die Funktionen und Möglichkeiten der Plattform zu verstehen.

### Verwaltung des Containers in Docker

	1.	Pause des Containers:
	•	Öffnen Sie in Docker Desktop die Registerkarte Containers.
	•	Wählen Sie den n8n-Container und klicken Sie auf Stop, wenn Sie eine Pause einlegen möchten.
	2.	Wiederaufnahme:
	•	Starten Sie den Container erneut über dieselbe Oberfläche.

Zusammenfassung

Mit diesem Workflow richten Sie eine lokale Umgebung ein, die den Betrieb von Automatisierungs-Workflows unterstützt. Docker dient als Grundlage für Container-Management, während n8n als Automatisierungsplattform über eine intuitive Benutzeroberfläche im Webbrowser fungiert.

# Weiterführende Quellen

**[Docker Documentation – Get Started](https://docs.docker.com/get-started/):**  
Offizielle Einführung in Docker. Diese Quelle bietet eine schrittweise Anleitung zur Installation, ersten Schritten und Nutzung von Docker-Containern.

**[n8n Documentation – Getting Started](https://docs.n8n.io/getting-started/):**  
Eine ausführliche Anleitung zur Einrichtung und Nutzung von n8n, einschließlich grundlegender und fortgeschrittener Workflows. Ideal für neue Benutzer.

**[n8n Video Tutorials](https://n8n.io/videos/):**  
Eine Sammlung von Videoanleitungen, die praxisorientierte Beispiele für die Nutzung von n8n zur Automatisierung von Prozessen bieten.

**[Docker Hub – n8n Image](https://hub.docker.com/r/n8nio/n8n):**  
Das offizielle Docker-Image von n8n. Hier finden Sie die aktuellsten Versionen, Dokumentationen und Details zu Image-Konfigurationen.

**[n8n Academy](https://n8n.io/academy/):**  
Kurse, Tutorials und Anleitungen, um die Automatisierungsfähigkeiten von n8n zu meistern. Ideal für die Entwicklung eigener Workflows.

**[Docker Cheatsheet](https://dockerlabs.collabnix.com/docker/cheatsheet/):**  
Eine praktische Übersicht mit den wichtigsten Docker-Befehlen und -Konzepten für den schnellen Zugriff. Nützlich für effizientes Arbeiten in der Terminal-Umgebung.

**[n8n Community Forum](https://community.n8n.io/):**  
Ein Forum für n8n-Nutzer, in dem Fragen gestellt und Best Practices ausgetauscht werden können. Eine wertvolle Ressource bei spezifischen Problemen.