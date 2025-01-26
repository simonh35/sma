---
title: Python - Get Started Tutorial
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

Diese Seite bietet eine praxisorientierte Anleitung zur Installation und ersten Nutzung von Python, einschließlich der Systemvoraussetzungen, der Einrichtung eines Texteditors, der Installation von Python und der Ausführung erster Skripte. Sie führt den Benutzer Schritt für Schritt durch den Prozess, liefert hilfreiche Beispiele und gibt Tipps zur Fehlerbehebung. Der Mehrwert liegt in der klaren Struktur und der direkten Anwendbarkeit, wodurch sowohl Anfänger als auch Fortgeschrittene schnell und effizient mit Python arbeiten können.
```
---
# Einführung

In der heutigen digitalen Welt ist Python eine der gefragtesten Programmiersprachen, die sowohl für Anfänger als auch für erfahrene Entwickler von Bedeutung ist. Dieses Dokument bietet eine umfassende Anleitung zur Installation und Konfiguration von Python, einschließlich der Systemvoraussetzungen, der Durchführung der Installation und der ersten Schritte mit der Sprache. Es richtet sich an Benutzer, die Python auf ihrem System einrichten möchten, um die Grundlagen der Programmierung zu erlernen oder bestehende Kenntnisse zu vertiefen.

Der zentrale Gedanke dieser Seite ist es, eine strukturierte und schrittweise Anleitung zu bieten, die sicherstellt, dass Benutzer alle notwendigen Voraussetzungen erfüllen, um Python erfolgreich zu installieren und zu nutzen. Die Inhalte sind so gestaltet, dass sie den Leser durch den gesamten Prozess führen, von der Überprüfung des Betriebssystems über die Installation eines geeigneten Texteditors bis hin zur Ausführung einfacher Python-Skripte. Dies schafft eine klare Verbindung zwischen den theoretischen Grundlagen und der praktischen Anwendung.

Die Informationen sind besonders relevant für Personen, die neu in der Programmierung sind oder ihre Kenntnisse in Python erweitern möchten. Die detaillierten Anweisungen und Beispiele ermöglichen es den Lesern, die Konzepte direkt anzuwenden und erste Programmiererfahrungen zu sammeln. Die Inhalte sind praxisorientiert und bieten eine solide Grundlage, die sowohl für Anfänger als auch für Fortgeschrittene nützlich ist. Die Zielgruppe umfasst daher sowohl Einsteiger, die ihre ersten Schritte in der Programmierung machen, als auch erfahrene Entwickler, die ihre Umgebung optimieren möchten.
# Im Detail

## Systemvoraussetzungen & Vorbereitung

### Zweck

Dieser Abschnitt stellt sicher, dass Ihr System die Anforderungen für Python erfüllt und alle notwendigen Vorbereitungen getroffen werden, um eine reibungslose Installation zu gewährleisten.

### Voraussetzungen

- Betriebssystem: Windows 10/11, macOS 12+ oder eine aktuelle Linux-Distribution (z. B. Ubuntu 22.04).
- Hardware:
  - Prozessor: 1 GHz oder schneller
  - RAM: Mindestens 2 GB
  - Festplattenspeicher: 200 MB für Python, zusätzliche 500 MB für Bibliotheken
- Internetverbindung: Für den Download von Python und Abhängigkeiten.

### Durchführung

1. Überprüfen Sie Ihr Betriebssystem:

- lsb_release -a
  - Windows: `Einstellungen > System > Info`
  - macOS: `Apple-Menü > Über diesen Mac`
  - Linux:
- Erwartetes Ergebnis: Sie kennen die genaue Version Ihres Betriebssystems.
- Validierung: Notieren Sie die Version und vergleichen Sie sie mit den oben genannten Anforderungen.

1. Installieren Sie einen Texteditor:

- Aktion: Laden Sie Visual Studio Code (VS Code) herunter und installieren Sie es.
  - Download-Link: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Erwartetes Ergebnis: VS Code ist installiert und startbereit.
- Validierung: Öffnen Sie VS Code und prüfen Sie, ob es ohne Fehler startet.

### Fehlerbehebung

Problem: Betriebssystemversion ist zu alt.Ursache: Python unterstützt ältere Betriebssysteme nicht.Lösung: Aktualisieren Sie Ihr Betriebssystem auf eine unterstützte Version.

## Download & Verifizierung

### Durchführung

1. Get-FileHash python-3.12.0-amd64.exe -Algorithm SHA256shasum -a 256 python-3.12.0-macosx10.9.pkg

- Windows PowerShell:
- macOS/Linux Terminal:

## Installation & Grundkonfiguration

### Installation überprüfen:

```
python --version
```

### Pip überprüfen:

```
pip --version
```

## Erste Schritte & Navigation

### Python-Interpreter verwenden:

```
print("Hello, World!")
```

### Erstes Python-Skript:

```
# hello.pyprint("Hello, Python!")
```

Ausführen des Skripts:

```
python hello.py
```

## Kernfunktionen

### Variablen und Datentypen:

```
# variables.pyname = "Alice"age = 25print(f"My name is {name} and I am {age} years old.")
```

### Schleifen und Bedingungen:

```
# loops.pyfor i in range(5):    if i % 2 == 0:        print(f"{i} is even")    else:        print(f"{i} is odd")
```

## Basis-Workflows

### Taschenrechner-Beispiel:

```
def calculator(a, b, operation):    if operation == "add":        return a + b    elif operation == "subtract":        return a - b    else:        return "Invalid operation"print(calculator(10, 5, "add"))  # Ausgabe: 15
```

## Troubleshooting & Wartung

### Fehlerprotokolle analysieren:

```
python -m trace --trace script.py
```

## Referenzen

- [Offizielle Python-Dokumentation](https://docs.python.org/3/)
- [Python Downloads](https://www.python.org/downloads/)

# Weiterführende Quellen

**Offizielle Python-Dokumentation:** Umfassende Informationen zu Python, einschließlich Tutorials, Referenzen und Best Practices. Ideal für alle, die tiefer in die Sprache eintauchen möchten. [Link zur Dokumentation](https://docs.python.org/3/)

**Python Package Index (PyPI):** Die zentrale Anlaufstelle für Python-Pakete. Hier finden Sie eine Vielzahl von Bibliotheken, die Ihre Python-Projekte erweitern können. [Link zu PyPI](https://pypi.org/)

**Real Python:** Eine Plattform mit hochwertigen Tutorials und Artikeln zu Python, die sowohl für Anfänger als auch für Fortgeschrittene geeignet sind. Bietet praktische Beispiele und tiefere Einblicke in spezifische Themen. [Link zu Real Python](https://realpython.com/)

**W3Schools Python Tutorial:** Ein interaktives Tutorial, das die Grundlagen von Python einfach und verständlich erklärt. Ideal für Anfänger, die schnell lernen möchten. [Link zu W3Schools](https://www.w3schools.com/python/)

**GeeksforGeeks Python Programming Language:** Eine Sammlung von Artikeln, Tutorials und Beispielen, die verschiedene Aspekte der Python-Programmierung abdecken. Nützlich für das Verständnis spezifischer Konzepte und Techniken. [Link zu GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/)

**Codecademy Python Course:** Ein interaktiver Kurs, der Ihnen hilft, Python von Grund auf zu lernen. Bietet praktische Übungen und Projekte, um das Gelernte anzuwenden. [Link zu Codecademy](https://www.codecademy.com/learn/learn-python-3)

**Kaggle:** Eine Plattform für Datenwissenschaft und maschinelles Lernen, die viele Python-Ressourcen und -Kurse bietet. Ideal für diejenigen, die Python in der Datenanalyse und im maschinellen Lernen anwenden möchten. [Link zu Kaggle](https://www.kaggle.com/learn/python)

Diese Quellen bieten wertvolle Informationen und Ressourcen, um Ihr Wissen über Python zu vertiefen und praktische Fähigkeiten zu entwickeln.