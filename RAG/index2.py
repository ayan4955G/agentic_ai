from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv
load_dotenv()


pdf_path = Path(__file__).parent / "test.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

print(docs[1]) 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")

embedder = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

sample_embedding = embedder.embed_query("test")
print(f"Embedding dimension: {len(sample_embedding)}")

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedder,      
    url="http://localhost:6333",
    collection_name="leaning_RAG"
)

print("Indexing of document is done .....")