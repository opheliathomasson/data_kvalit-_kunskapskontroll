def retrieve_context(vector_store, question, k=5):
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": 20
        }
    )

    results = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    return context, results
