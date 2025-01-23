from langchain_ollama import OllamaEmbeddings

# Returns embedding
def get_embedding():
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    return embedding