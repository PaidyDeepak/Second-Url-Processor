import requests
from scrapling import Selector
import json
import pickle
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def normalize(text):
    return " ".join(text.split()).lower()

def scrape(url):
    """Scrapes a single URL and returns text."""
    try:
        response = requests.get(url, timeout=10)
        page = Selector(response.text)
        return page.get_all_text()
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def store():
    with open("scraped3.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    texts = []
    metadatas = []

    for url, content in data.items():
        if content.strip():
            texts.append(content)
            metadatas.append({"source": url})

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents(texts, metadatas=metadatas)

    # Deduplication
    seen = set()
    unique_docs = []
    for doc in docs:
        content_hash = normalize(doc.page_content)
        if content_hash not in seen:
            unique_docs.append(doc)
            seen.add(content_hash)

    # Save docs for BM25 (Required by rag.py)
    with open("docs.pkl", "wb") as f:
        pickle.dump(unique_docs, f)

    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create and persist vector DB
    vector_db = Chroma.from_documents(
        unique_docs, 
        embedding, 
        persist_directory="./vector_db"
    )
    return True