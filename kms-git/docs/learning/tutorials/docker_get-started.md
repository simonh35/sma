---
title: Docker - Get Started Tutorial
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
Dieses umfassende Tutorial bietet eine Schritt-für-Schritt-Anleitung zur Installation, Konfiguration und Nutzung von Docker, beginnend mit den Systemvoraussetzungen bis hin zu fortgeschrittenen Workflows und Troubleshooting. Es richtet sich an Benutzer ohne Docker-Vorkenntnisse und ermöglicht durch klare Anweisungen, validierbare Ergebnisse und vollständige Fehlerbehebungsstrategien einen sicheren und effektiven Einstieg in die Containerisierung. Der Nutzer profitiert von einem strukturierten Lernpfad, reproduzierbaren Ergebnissen und einer maximal detaillierten Dokumentation, die ihn befähigt, Docker erfolgreich zu installieren und zu nutzen.
```
---
# Einführung

Dieses Tutorial erklärt Schritt für Schritt die Installation, Einrichtung und Nutzung von Docker auf einem frisch installierten Betriebssystem. Ziel ist es, Docker korrekt zu installieren, erste Container auszuführen und die grundlegenden Workflows zu verstehen. Dieses Tutorial richtet sich an Benutzer ohne Vorkenntnisse in Docker, jedoch mit grundlegenden IT-Kenntnissen.


# Im Detail

## 0. Systemvoraussetzungen & Vorbereitung

### Zweck
Sicherstellen, dass das System die Anforderungen für Docker erfüllt, um eine reibungslose Installation und Nutzung zu gewährleisten.

### Voraussetzungen
- Frische Betriebssysteminstallation (Windows 10/11, macOS 12+, oder Ubuntu 20.04+)
- Administratorrechte
- Internetverbindung

### Durchführung
1. **Hardwareprüfung**
   - Aktion: Stellen Sie sicher, dass Ihr System mindestens 4 GB RAM und 2 CPU-Kerne hat.
   - Erwartetes Ergebnis: System erfüllt die Anforderungen.
   - Validierung: Öffnen Sie die Systeminformationen (`Windows+Pause`, `System Preferences`, oder `lscpu` auf Linux).

2. **Virtualisierung aktivieren**
   - Aktion: Aktivieren Sie die Virtualisierung in der BIOS/UEFI-Konfiguration.
   - Erwartetes Ergebnis: Virtualisierung ist aktiviert.
   - Validierung: Führen Sie unter Windows `systeminfo` aus und prüfen Sie, ob „Virtualisierung aktiviert“ angezeigt wird.

3. **Installationsziel vorbereiten**
   - Aktion: Erstellen Sie ein Verzeichnis wie `C:\Docker` oder `/usr/local/docker`.
   - Erwartetes Ergebnis: Verzeichnis existiert.
   - Validierung: Verzeichnis mit `ls` oder Datei-Explorer überprüfen.

---

## 1. Download & Verifizierung

### Zweck
Laden Sie die aktuelle Docker-Version herunter und stellen Sie sicher, dass die Dateien authentisch sind.

### Voraussetzungen
- Internetzugang
- Installierte Tools wie `sha256sum` (Linux) oder `PowerShell`

### Durchführung
1. **Docker Desktop herunterladen**
   - Aktion: Besuchen Sie die [Docker Download-Seite](https://www.docker.com/products/docker-desktop) und laden Sie die Installationsdatei herunter.
   - Erwartetes Ergebnis: Die Installationsdatei (`.exe`, `.dmg`, oder `.deb`) befindet sich im Download-Ordner.

2. **Datei verifizieren**
   - Aktion: Laden Sie den passenden SHA256-Checksum-Wert von der Website herunter.
   - Erwartetes Ergebnis: Die Checksumme stimmt mit der Datei überein.
   - Validierung: 
     - Windows: `Get-FileHash -Path .\Docker-Installer.exe -Algorithm SHA256`
     - Linux/macOS: `sha256sum docker-installer.deb`

---

## 2. Installation & Grundkonfiguration

### Zweck
Installieren Sie Docker auf Ihrem System und führen Sie die erste Konfiguration durch.

### Voraussetzungen
- Heruntergeladene und verifizierte Installationsdatei

### Durchführung
1. **Installation ausführen**
   - Aktion: Doppelklicken Sie die Installationsdatei und folgen Sie den Anweisungen.
   - Erwartetes Ergebnis: Docker Desktop wird installiert.
   - Validierung: Starten Sie Docker über das Startmenü oder Terminal (`docker --version`).

2. **Grundkonfiguration**
   - Aktion: Melden Sie sich mit einem Docker-Konto an (oder erstellen Sie eines) und aktivieren Sie die notwendigen Funktionen wie WSL 2 auf Windows.
   - Erwartetes Ergebnis: Docker läuft und ist einsatzbereit.
   - Validierung: `docker run hello-world`

---

## 3. Erste Schritte & Navigation

### Zweck
Einführung in die Benutzeroberfläche und grundlegende Befehle von Docker.

### Voraussetzungen
- Erfolgreich installiertes Docker

### Durchführung
1. **Docker CLI nutzen**
   - Aktion: Öffnen Sie das Terminal und führen Sie `docker info` aus.
   - Erwartetes Ergebnis: Docker-Informationen werden angezeigt.

2. **Erster Container**
   - Aktion: `docker run hello-world` ausführen.
   - Erwartetes Ergebnis: Eine Erfolgsmeldung mit einer kurzen Erklärung von Docker wird angezeigt.
   - Validierung: Container läuft und beendet sich korrekt.

---

## 4. Kernfunktionen

### Zweck
Grundlegende Docker-Funktionen wie Container starten, stoppen und verwalten.

### Voraussetzungen
- Lauffähiges Docker

### Durchführung
1. **Container starten**
   - Aktion: `docker run -it ubuntu bash` ausführen.
   - Erwartetes Ergebnis: Interaktiver Container mit Ubuntu wird gestartet.

2. **Container verwalten**
   - Aktion: `docker ps` (laufende Container) und `docker ps -a` (alle Container) verwenden.
   - Validierung: Liste der Container wird angezeigt.

3. **Container stoppen**
   - Aktion: `docker stop [CONTAINER_ID]`.
   - Validierung: Der Container wird gestoppt (`docker ps` zeigt ihn nicht mehr an).

---

## 5. Basis-Workflows

### Zweck
Praktische Docker-Workflows wie das Erstellen von Docker-Images und das Nutzen von Dockerfiles.

### Voraussetzungen
- Grundlegende Docker-Kenntnisse

### Durchführung
1. **Dockerfile erstellen**
   - Aktion: Erstellen Sie eine Datei `Dockerfile` mit folgendem Inhalt:
     ```dockerfile
     FROM ubuntu:latest
     RUN apt-get update && apt-get install -y curl
     CMD ["bash"]
     ```
   - Validierung: Datei mit `cat Dockerfile` überprüfen.

2. **Image bauen**
   - Aktion: `docker build -t my-ubuntu .`
   - Erwartetes Ergebnis: Image wird erstellt.
   - Validierung: `docker images` zeigt `my-ubuntu` an.

3. **Image verwenden**
   - Aktion: `docker run -it my-ubuntu`.
   - Erwartetes Ergebnis: Container startet.

---

## 6. Troubleshooting & Wartung

### Zweck
Lösen Sie häufige Probleme und warten Sie Ihre Docker-Installation.

### Voraussetzungen
- Docker installiert und in Nutzung

### Durchführung
1. **Fehlermeldungen analysieren**
   - Problem: `docker: Cannot connect to the Docker daemon.`
   - Ursache: Docker-Dienst läuft nicht.
   - Lösung: Starten Sie den Dienst:
     - Windows: Docker Desktop öffnen und starten.
     - Linux: `sudo systemctl start docker`.

2. **Container aufräumen**
   - Aktion: `docker system prune -a` (löscht alle ungenutzten Ressourcen).
   - Validierung: Speicherplatz wird freigegeben (`docker system df`).

# Weiterführende Quellen

## Offizielle Docker-Dokumentation
**Docker Installation Guide:** Eine detaillierte Anleitung zur Installation von Docker auf verschiedenen Betriebssystemen.  
[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

**Docker CLI Referenz:** Vollständige Übersicht aller verfügbaren Docker-Befehle mit Beispielen.  
[https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)

**Dockerfile Referenz:** Ausführliche Dokumentation zu Dockerfiles, einschließlich Syntax und Best Practices.  
[https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)

---

## Community und Tutorials
**Docker Hub:** Zentrale Plattform für das Teilen und Herunterladen von Docker-Images. Enthält auch eine umfassende Sammlung von Community-Images.  
[https://hub.docker.com/](https://hub.docker.com/)

**Docker Getting Started Tutorial:** Offizielles Tutorial, das die grundlegenden Docker-Konzepte praktisch erklärt.  
[https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)

---

## Troubleshooting und Best Practices
**Docker Troubleshooting Guide:** Offizielle Anleitung zur Lösung häufiger Docker-Probleme.  
[https://docs.docker.com/config/daemon/#troubleshoot](https://docs.docker.com/config/daemon/#troubleshoot)

**Docker Best Practices:** Sammlung von Empfehlungen zur effizienten Nutzung von Docker in Entwicklungs- und Produktionsumgebungen.  
[https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)

---

## Erweiterte Themen
**Docker Compose Referenz:** Dokumentation und Beispiele für die Nutzung von Docker Compose zur Orchestrierung mehrerer Container.  
[https://docs.docker.com/compose/](https://docs.docker.com/compose/)

**Kubernetes und Docker:** Überblick über die Integration von Docker und Kubernetes für Container-Orchestrierung.  
[https://kubernetes.io/docs/setup/production-environment/container-runtimes/](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

**Docker Security:** Leitfaden zur Absicherung von Docker-Containern und Images.  
[https://docs.docker.com/engine/security/](https://docs.docker.com/engine/security/)

Dieses Kapitel stellt eine kuratierte Auswahl spezifischer Ressourcen bereit, die die Inhalte des Tutorials vertiefen und praktisch anwendbar machen. Die Links sind direkt relevant und helfen dabei, das Verständnis zu erweitern und Probleme effektiv zu lösen.