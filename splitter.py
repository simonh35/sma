from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Split documents into chunks
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return text_splitter.split_documents(documents)
