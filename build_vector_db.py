from dotenv import load_dotenv
import os
import pandas as pd

from pathlib import Path

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_chroma import Chroma


# Load environment variables

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# Load CSV data

csv_path = "data_processed/main_harry_potter_cleaned.csv"

df = pd.read_csv(csv_path, encoding="utf-8")

loader = CSVLoader(
    file_path=csv_path,
    encoding="utf-8"
)

documents = loader.load()

print(f"CSV documents: {len(documents)}")


# Load text files

book_documents = []

for file_path in Path("data_raw").glob("*.txt"):

    print(f"Loading {file_path.name}")

    loader = TextLoader(
        file_path,
        encoding="utf-8"
    )

    docs = loader.load()

    for doc in docs:
        doc.metadata["source"] = file_path.name

    book_documents.extend(docs)

print(f"Book documents: {len(book_documents)}")


# Split text into chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

book_chunks = text_splitter.split_documents(book_documents)

print(f"Chunks: {len(book_chunks)}")


# Combine all documents

all_documents = documents + book_chunks

print(f"Total documents: {len(all_documents)}")


# Create embeddings model

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Create vector database

vector_store = Chroma(
    collection_name="harry_potter_hf",
    embedding_function=embeddings,
    persist_directory="./chroma_harry_potter_test_db",
)


# Add documents to database

if vector_store._collection.count() == 0:

    batch_size = 500

    for i in range(0, len(all_documents), batch_size):

        batch = all_documents[i:i + batch_size]

        vector_store.add_documents(documents=batch)

        print(f"Added {i} to {i + len(batch)}")

    print("Vector database created")

else:
    print("Vector database already exists")