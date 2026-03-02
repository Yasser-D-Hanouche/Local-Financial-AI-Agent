from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def get_database_retriever(file_path):
    print("Setting up database...")
    
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db_location = "./chroma_langchain_db"
    
    vector_store = Chroma(
        collection_name="stock_news",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    
    with open(file_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([full_text])
    
    
    print(f"Adding {len(chunks)} new paragraphs to your collection...")
    vector_store.add_documents(chunks)
    
    total_chunks = vector_store._collection.count()
    print(f"--- Database updated! Total knowledge: {total_chunks} chunks ---")
    
    return vector_store.as_retriever(search_kwargs={"k": 5})