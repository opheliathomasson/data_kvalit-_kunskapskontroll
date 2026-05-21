import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=api_key
)


def generate_answer(question, context):
    prompt = f"""
You are an ancient and knowledgeable wizard librarian.
Answer questions about the Harry Potter universe using the retrieved context.
Keep your answers concise, immersive, and helpful.
If the retrieved data does not contain the answer, admit that the archives do not hold that knowledge.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content