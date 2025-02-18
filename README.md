# SMA-O WS24/24

## INSTALLATION

### Git Repository Clonen
```bash
git clone https://github.com/simonh35/sma.git
cd sma
```

## n8n mit Docker Compose starten

### Nutzer, die Ollama lokal ausführen
Ollama herunterladen und starten: <https://ollama.com/download>   
Im Terminal gewünschte Modelle pullen:
```bash
ollama pull llama3.2:latest
ollama pull nomic-embed-text
```

Docker Compose ausführen:
```bash
docker compose up -d
```
Nachdem die Docker-Container gestartet sind:
1. Credentials unter <http://localhost:5678/credentials> öffnen
2. Auf "Local Ollama service" klicken
3. Base URL auf "http://host.docker.internal:11434" ändern
4. Auf "Save" klicken

### Nvidia GPU Nutzer
```bash
docker compose --profile gpu-nvidia up -d
```

> [!NOTE]
> Bei erstmaliger Nutzung von Ollama über eine Nvidia GPU mit Docker:
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

### Für alle anderen Nutzer (Ollama läuft nur über CPU)
```bash
docker compose --profile cpu up -d
```

## NUTZUNG
Editor unter <http://localhost:5678/home/workflows> öffnen

### 1. Zotero
- Zotero UserID in Node "Set Zotero-UserID" setzen
- In der Node "Load Items in Zotero" unter "Header Auth" ein Credential mit dem Namen "Zotero-API-Key" und einem API Key von Zotero erstellen
- Beim klicken von "Test Workflow" werden PDF-Dateien aus Zotero geladen und in der Qdrant Vektordatenbank gespeichert
- Die erstellten Vektoren können unter <http://localhost:6333/dashboard#/collections> eingesehen werden

### 2. Obsidian
- In der Node "Qdrant Vector Store" eine Collection auswählen oder erstellen
- Workflow auf aktiv stellen
- Beim drücken von "Strg + P" in Obsidian die Command Palette öffnen
- "Post Webhook" eingeben und "Send note to n8n Workflow" auswählen
- Dabei wird die Markdown-File in der Qdrant Vektordatenbank gespeichert
 
### 3. Chat
- Dies ist der Main-Workflow
- In der Node "Qdrant Vector Store" die gewünschte Collection auswählen
- Bei der Eingabe einer Frage in das Chat-Fenster werden Dokumente aus der Qdrant Vektordatenbank verwendet, um mit einer LLM die Frage zu beantworten

## Typische Probleme
### Docker Compose file wird nicht korrekt ausgeführt
```bash
docker compose down -v
```
Dann Docker compose nochmal ausführen
### Docker Container hängen sich auf
Windows:
```bash
docker ps -q | ForEach-Object { docker kill $_ }
```
Linux/Mac:
```bash
docker kill $(docker ps -q)
```
### Ollama Modelle können in der Node nicht gewählt werden
Modelle sind wahrscheinlich nicht gepullt:
```bash
ollama pull *modellname*
```
