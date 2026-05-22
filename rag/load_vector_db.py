from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings 

def load_vector_store():
    # Create the embeddings model using the HuggingFaceEmbeddings class from langchain_community, and specify the model to use for generating the embeddings.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create the vector store using the Chroma class from langchain_chroma, and specify the persist directory for the database.
    vector_store = Chroma(
        collection_name="harry_potter_hf",
        persist_directory="./chroma_harry_potter_many_db",
        embedding_function=embeddings
    ) 

    return vector_store