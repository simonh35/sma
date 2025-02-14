# SMA

## INSTALLATION

### Git Repository Clonen
```bash
git clone https://github.com/simonh35/sma.git
cd sma
```

## n8n mit Docker Compose starten

### - Nutzer, die Ollama lokal ausführen
```bash
docker compose up
```


### - Nvidia GPU Nutzer
```bash
docker compose --profile gpu-nvidia up
```
Nachdem der Docker-Container gestartet ist:
1. Credentials unter <http://localhost:5678/credentials> öffnen
2. Auf "Local Ollama service" klicken
3. Base URL auf "http://ollama:11434" ändern
4. Auf "Save" klicken

> [!NOTE]
> Bei erstmaliger Nutzung von Ollama über eine Nvidia GPU mit Docker, 
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).


### - Für alle anderen Nutzer (Ollama läuft nur über CPU)
```bash
docker compose --profile cpu up
```