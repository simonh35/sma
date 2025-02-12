# SMA

## INSTALLATION

### Cloning Git Repository
```bash
git clone https://github.com/simonh35/sma.git
cd sma
```

## Running n8n using docker compose

### For users running Ollama locally
If you're running OLLAMA locally on your Mac (not in Docker), you need to modify the OLLAMA_HOST environment variable
in the n8n service configuration. Update the x-n8n section in your Docker Compose file as follows:

```yaml
x-n8n: &service-n8n
  # ... other configurations ...
  environment:
    # ... other environment variables ...
    - OLLAMA_HOST=host.docker.internal:11434
```

Head back to your terminal:
```bash
docker compose up
```

Additionally, after you see "Editor is now accessible via: <http://localhost:5678/>":

1. Head to <http://localhost:5678/home/credentials>
2. Click on "Local Ollama service"
3. Change the base URL to "http://host.docker.internal:11434/"

### For Nvidia GPU users
```bash
docker compose --profile gpu-nvidia up
```
> [!NOTE]
> If you have not used your Nvidia GPU with Docker before, please follow the
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

### For AMD GPU users on linux
```bash
docker compose --profile gpu-amd up
```

### For everyone else (Running Ollama in a container using cpu only)
```bash
docker compose --profile cpu up
```