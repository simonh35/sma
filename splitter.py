from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

# Split documents into chunks
def split_documents(documents: list[Document]):
    return text_splitter.split_documents(documents)
