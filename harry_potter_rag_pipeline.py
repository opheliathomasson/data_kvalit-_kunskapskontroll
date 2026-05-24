from dotenv import load_dotenv
import os

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# --- LOAD ONCE FUNCTIONS ---

def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        collection_name="harry_potter_hf",
        embedding_function=embeddings,
        persist_directory="./chroma_harry_potter_test_db",
    )

    return vector_store


def load_model():

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key
    )


# --- CACHE SAFE GLOBALS (IMPORTANT) ---

vector_store = load_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
model = load_model()


# --- MAIN FUNCTION ---

def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a wise wizard.

Use ONLY the retrieved data.

Retrieved data:
{context}

Question:
{question}
"""

    response = model.invoke(prompt)

    return response.content