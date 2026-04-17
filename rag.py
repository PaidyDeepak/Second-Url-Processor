import os
import pickle
from dotenv import load_dotenv
from google import genai

import sys
import types
sys.modules['pwd'] = types.ModuleType('pwd')

from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.retrievers.ensemble import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

load_dotenv()

def get_retriever():
    if not os.path.exists("docs.pkl"):
        return None

    with open("docs.pkl", "rb") as f:
        docs = pickle.load(f)

    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./vector_db", embedding_function=embedding)
    
    vector_retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    bm25 = BM25Retriever.from_documents(docs)
    bm25.k = 3

    return EnsembleRetriever(
        retrievers=[vector_retriever, bm25],
        weights=[0.7, 0.3]
    )

def rag_query(query):
    retriever = get_retriever()
    if not retriever:
        return "Please process URLs first."
    
    # ✅ Correct method for 0.x
    results = retriever.get_relevant_documents(query)
    print(results)
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    context = "\n\n".join([doc.page_content for doc in results])

    prompt = f"""
    Answer using the given context. 
    Explain every answer in detail. Remove '**' in the generated text. 
    Do not start with 'Based on the provided context'. Never assume unknown data.
    Context: {context}
    Question: {query}
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )
    
    return response.text