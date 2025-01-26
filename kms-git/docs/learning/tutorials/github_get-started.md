---
title: GitHub - Get Started Tutorial
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
Dieses Tutorial führt Schritt für Schritt durch die Einrichtung, Nutzung und Wartung von GitHub, beginnend bei den Systemanforderungen bis hin zur Fehlerbehebung. Es ist speziell für Einsteiger ohne Vorkenntnisse in GitHub konzipiert, bietet jedoch eine präzise und umfassende Anleitung zu Kernfunktionen wie Repository-Management, Branching und Zusammenarbeit. Mit klaren Anweisungen, Validierungsmethoden und Lösungsansätzen für häufige Probleme ermöglicht es eine sichere und effektive Nutzung von GitHub, unterstützt durch Verweise auf offizielle Dokumentationen und praktische Beispiele.
```
---
# Einführung

Dieses Tutorial bietet eine umfassende Anleitung, um GitHub von Grund auf zu installieren, zu konfigurieren und zu nutzen. Es richtet sich an Benutzer ohne Vorkenntnisse in GitHub, aber mit einem grundlegenden Verständnis von IT-Konzepten.

# Im Detail
## 0. Systemvoraussetzungen & Vorbereitung

### Zweck
Stellen Sie sicher, dass Ihr System die Mindestanforderungen erfüllt, und bereiten Sie es für die Installation von GitHub vor.

### Voraussetzungen
- Betriebssystem: Windows 10/11, macOS 11+ oder eine aktuelle Linux-Distribution
- Internetverbindung
- Administratorrechte auf dem Rechner

### Durchführung
1. **Systemanforderungen prüfen:**
   - Windows:
     - Öffnen Sie "Einstellungen" > "System" > "Info".
     - Stellen Sie sicher, dass Sie mindestens 4 GB RAM und 10 GB freien Speicherplatz haben.
   - macOS:
     - Öffnen Sie das Apple-Menü > "Über diesen Mac".
     - Prüfen Sie RAM und Festplattenspeicher.
   - Linux:
     - Führen Sie den Befehl `free -h` und `df -h` aus, um RAM und Speicherplatz zu überprüfen.

2. **Netzwerkverbindung testen:**
   - Öffnen Sie einen Browser und rufen Sie [GitHub.com](https://github.com) auf.
   - Stellen Sie sicher, dass die Seite geladen wird.

### Fehlerbehebung
Problem: **Website GitHub.com kann nicht geladen werden.**
- Ursache: Netzwerkverbindung ist gestört.
- Lösung: 
  - Prüfen Sie die Internetverbindung.
  - Führen Sie `ping github.com` in der Eingabeaufforderung aus.
  - Stellen Sie sicher, dass Firewalls GitHub nicht blockieren.

## Referenzen
- [GitHub System Requirements](https://docs.github.com)

---

## 1. Download & Verifizierung

### Zweck
Laden Sie die offizielle Software sicher herunter und überprüfen Sie die Integrität.

### Voraussetzungen
- Ein Browser ist installiert.
- Die URL der offiziellen GitHub-Downloads.

### Durchführung
1. **Download:**
   - Besuchen Sie die [GitHub Desktop-Website](https://desktop.github.com).
   - Wählen Sie die Version für Ihr Betriebssystem und klicken Sie auf **Download**.

2. **Integrität prüfen:**
   - Windows:
     - Öffnen Sie die Eingabeaufforderung und führen Sie `certutil -hashfile GitHubDesktopSetup.exe SHA256` aus.
     - Vergleichen Sie den Hash-Wert mit der auf der Website angegebenen Prüfsumme.
   - macOS/Linux:
     - Führen Sie im Terminal `shasum -a 256 GitHubDesktop.dmg` oder `GitHubDesktop.AppImage` aus.

### Fehlerbehebung
Problem: **Hash-Wert stimmt nicht überein.**
- Ursache: Der Download wurde möglicherweise manipuliert.
- Lösung: Laden Sie die Datei erneut herunter und prüfen Sie den Hash erneut.

## Referenzen
- [Download GitHub Desktop](https://desktop.github.com)

---

## 2. Installation & Grundkonfiguration

### Zweck
Installieren Sie GitHub Desktop und richten Sie grundlegende Einstellungen ein.

### Voraussetzungen
- Heruntergeladene Installationsdatei.
- Ein GitHub-Konto (optional).

### Durchführung
1. **Installation:**
   - Windows:
     - Doppelklicken Sie auf die Datei `GitHubDesktopSetup.exe`.
     - Folgen Sie den Anweisungen des Installationsassistenten.
   - macOS:
     - Ziehen Sie die `GitHub Desktop`-App in den Ordner `Applications`.
   - Linux:
     - Führen Sie im Terminal aus:
       ```bash
       chmod +x GitHubDesktop.AppImage
       ./GitHubDesktop.AppImage
       ```

2. **Erstkonfiguration:**
   - Starten Sie GitHub Desktop.
   - Melden Sie sich mit Ihrem GitHub-Konto an oder erstellen Sie ein neues Konto.

3. **SSH-Schlüssel einrichten (optional):**
   - Öffnen Sie das Terminal und führen Sie aus:
     ```bash
     ssh-keygen -t ed25519 -C "youremail@example.com"
     ```
   - Fügen Sie den öffentlichen Schlüssel zu Ihrem GitHub-Konto hinzu.

### Fehlerbehebung
Problem: **Installation schlägt fehl.**
- Ursache: Unzureichende Berechtigungen.
- Lösung: Starten Sie die Installation mit Administratorrechten.

## Referenzen
- [GitHub Desktop Installation Guide](https://docs.github.com)

---

## 3. Erste Schritte & Navigation

### Zweck
Lernen Sie die Benutzeroberfläche und Grundfunktionen von GitHub Desktop kennen.

### Voraussetzungen
- Installierte und geöffnete GitHub Desktop-Anwendung.

### Durchführung
1. **Repository klonen:**
   - Klicken Sie auf **File > Clone Repository**.
   - Wählen Sie ein Repository aus Ihrem Konto oder geben Sie eine URL ein.

2. **Erste Änderungen vornehmen:**
   - Öffnen Sie eine Datei aus dem Repository und bearbeiten Sie sie.
   - Speichern Sie die Änderungen.

3. **Änderungen committen:**
   - Geben Sie eine Commit-Nachricht ein und klicken Sie auf **Commit to main**.

### Fehlerbehebung
Problem: **Repository kann nicht geklont werden.**
- Ursache: Ungültige URL oder Berechtigungen fehlen.
- Lösung: Überprüfen Sie die URL und die Zugriffsberechtigungen.

## Referenzen
- [GitHub Desktop Documentation](https://docs.github.com)

---

## 4. Kernfunktionen

### Zweck
Erlernen Sie die Hauptfunktionen von GitHub Desktop, einschließlich Branching, Merging und der Erstellung von Pull Requests.

### Voraussetzungen
- Ein geklontes Repository in GitHub Desktop.

### Durchführung
1. **Branch erstellen:**
   - Klicken Sie auf das Dropdown-Menü in der oberen Leiste, das den aktuellen Branch anzeigt.
   - Wählen Sie **New Branch**.
   - Geben Sie einen Namen ein und klicken Sie auf **Create Branch**.
   - Erwartetes Ergebnis: Ein neuer Branch wird erstellt und als aktiver Branch angezeigt.

2. **Änderungen vornehmen und committen:**
   - Bearbeiten Sie Dateien im neuen Branch.
   - Geben Sie eine Commit-Nachricht ein und klicken Sie auf **Commit to [Branch-Name]**.

3. **Branch mit Hauptbranch zusammenführen:**
   - Wechseln Sie in den Hauptbranch (z. B. `main`).
   - Klicken Sie auf **Branch > Merge into Current Branch**.
   - Wählen Sie den zu mergen Branch aus und bestätigen Sie.

4. **Pull Request erstellen:**
   - Klicken Sie auf **Create Pull Request**.
   - Fügen Sie eine Beschreibung hinzu und klicken Sie auf **Submit**.

### Fehlerbehebung
Problem: **Merge-Konflikte.**
- Ursache: Widersprüchliche Änderungen in den Branches.
- Lösung:
  1. Öffnen Sie den Editor, um die Konfliktstellen anzuzeigen.
  2. Lösen Sie die Konflikte und speichern Sie die Datei.
  3. Committen Sie die Änderungen erneut.

## Referenzen
- [Branches in GitHub Desktop](https://docs.github.com)
- [Pull Requests Guide](https://docs.github.com)

---

## 5. Basis-Workflows

### Zweck
Verstehen Sie die alltäglichen Arbeitsabläufe mit GitHub, wie das Erstellen von neuen Repositories, Synchronisierung und Zusammenarbeit.

### Voraussetzungen
- GitHub Desktop ist installiert und konfiguriert.

### Durchführung
1. **Neues Repository erstellen:**
   - Klicken Sie auf **File > New Repository**.
   - Geben Sie Name, Beschreibung und Speicherort ein.
   - Aktivieren Sie **Initialize with README**, falls gewünscht.
   - Klicken Sie auf **Create Repository**.

2. **Remote-Repository verknüpfen:**
   - Klicken Sie auf **Publish Repository**.
   - Wählen Sie Sichtbarkeit (öffentlich/privat) und klicken Sie auf **Publish**.

3. **Änderungen synchronisieren:**
   - Nehmen Sie Änderungen vor und committen Sie sie.
   - Klicken Sie auf **Push Origin**, um die Änderungen in das Remote-Repository hochzuladen.

4. **Zusammenarbeit:**
   - Fügen Sie Mitwirkende hinzu: Gehen Sie zu Ihrem Repository auf GitHub.com > **Settings > Collaborators and Teams**.
   - Laden Sie Personen ein, indem Sie ihre GitHub-Benutzernamen eingeben.

### Fehlerbehebung
Problem: **Push schlägt fehl.**
- Ursache: Authentifizierungsprobleme.
- Lösung: Überprüfen Sie, ob Sie bei GitHub Desktop angemeldet sind, und generieren Sie bei Bedarf ein neues Access Token.

## Referenzen
- [GitHub Repositories](https://docs.github.com)
- [GitHub Collaboration Guide](https://docs.github.com)

---

## 6. Troubleshooting & Wartung

### Zweck
Lösen Sie typische Probleme und halten Sie Ihre GitHub-Installation auf dem neuesten Stand.

### Voraussetzungen
- Administratorrechte auf Ihrem Rechner.

### Durchführung
1. **Aktualisieren von GitHub Desktop:**
   - Öffnen Sie **Help > About GitHub Desktop**.
   - Klicken Sie auf **Check for Updates** und installieren Sie verfügbare Updates.

2. **Fehlerprotokolle prüfen:**
   - Öffnen Sie **Help > Show Logs in Explorer**.
   - Überprüfen Sie die Log-Dateien auf Fehlermeldungen.

3. **Backup erstellen:**
   - Exportieren Sie Änderungen mit:
     ```bash
     git bundle create repository-backup.bundle --all
     ```
   - Speichern Sie die Datei an einem sicheren Ort.

4. **Konfliktanalyse:**
   - Nutzen Sie den Befehl:
     ```bash
     git status
     ```
     um Konflikte zu identifizieren und aufzulösen.

### Fehlerbehebung
Problem: **Anwendung startet nicht.**
- Ursache: Beschädigte Installation.
- Lösung:
  1. Deinstallieren Sie GitHub Desktop vollständig.
  2. Löschen Sie verbleibende Dateien unter `%AppData%\GitHubDesktop` (Windows) oder `~/Library/Application Support/GitHub Desktop` (macOS).
  3. Installieren Sie die neueste Version.

## Referenzen
- [Troubleshooting Guide](https://docs.github.com)
- [GitHub Support](https://support.github.com)

---

## Abschließende Validierung
- Testen Sie Ihre Einrichtung, indem Sie ein Repository erstellen, Änderungen vornehmen und einen Pull Request abschließen.
- Nutzen Sie die [GitHub Learning Lab](https://lab.github.com) Tutorials, um Ihre Fähigkeiten weiter auszubauen.

# Weiterführende Quellen

**GitHub Desktop Benutzerhandbuch:**  
[GitHub Desktop Documentation](https://docs.github.com/en/desktop)  
Dieses umfassende Benutzerhandbuch bietet detaillierte Anleitungen zur Installation, Konfiguration und Nutzung von GitHub Desktop. Ideal, um tiefer in einzelne Funktionen wie Branch-Management und Pull Requests einzutauchen.

**GitHub CLI Dokumentation:**  
[GitHub CLI Documentation](https://cli.github.com/manual/)  
Detaillierte Dokumentation zur GitHub CLI, mit der Sie GitHub-Operationen direkt über die Kommandozeile ausführen können. Eine gute Ergänzung für Nutzer, die über die Desktop-Oberfläche hinaus arbeiten möchten.

**Git Grundlagen:**  
[Pro Git Buch (kostenlos online)](https://git-scm.com/book/en/v2)  
Ein kostenloses Buch, das die Grundlagen von Git erklärt – der Versionskontrollsoftware, auf der GitHub basiert. Besonders hilfreich, um die technischen Hintergründe besser zu verstehen.

**GitHub Learning Lab:**  
[GitHub Learning Lab](https://lab.github.com)  
Interaktive Tutorials und Workshops, die Sie durch die wichtigsten Funktionen von GitHub führen. Ideal für Einsteiger und Fortgeschrittene, die praktische Übung suchen.

**GitHub Statusseite:**  
[GitHub Status](https://www.githubstatus.com)  
Aktuelle Informationen zu Betriebsstörungen oder Problemen bei GitHub-Diensten. Ein unverzichtbares Tool bei Verbindungsproblemen oder unerwarteten Fehlermeldungen.

**GitHub API Dokumentation:**  
[GitHub REST API Documentation](https://docs.github.com/en/rest)  
Für Entwickler, die GitHub in ihre eigenen Anwendungen integrieren möchten, bietet diese Quelle eine ausführliche Anleitung zu den API-Endpunkten.

**Open Source Guides:**  
[Open Source Guides by GitHub](https://opensource.guide)  
Hilfreiche Leitfäden für die Arbeit an und mit Open-Source-Projekten. Eine wertvolle Ressource, um die Zusammenarbeit auf GitHub besser zu verstehen.

**Fehlerbehebung in GitHub Desktop:**  
[Troubleshooting Guide for GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/troubleshooting-github-desktop)  
Spezifische Anleitungen zur Behebung häufiger Probleme bei der Nutzung von GitHub Desktop.

**SSH Key Management:**  
[SSH Keys on GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)  
Anleitungen zur Erstellung und Verwaltung von SSH-Schlüsseln für eine sichere Authentifizierung bei GitHub.

**Versionierung und Branching:**  
[Git Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)  
Ein Kapitel aus dem Pro Git Buch, das die Grundlagen von Branching und Merging erklärt. Perfekt, um diese wichtigen Funktionen in Git und GitHub besser zu verstehen.