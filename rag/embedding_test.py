from ollama import embeddings
def embed():
    # Create a vector store with a sample text
    from langchain_core.vectorstores import InMemoryVectorStore

    text = "LangChain is the framework for building context-aware reasoning applications"
    
    text2 = (
        "LangGraph is a library for building stateful, multi-actor applications with LLMs"
    )

    vectorstore = InMemoryVectorStore.from_texts(
        [text, text2],
        embedding=embeddings,
    )

    # Use the vectorstore as a retriever
    retriever = vectorstore.as_retriever()

    # Retrieve the most similar text
    retrieved_documents = retriever.invoke("What is LangChain?")

    # show the retrieved document's content
    for d in retrieved_documents:
        print(d.page_content)
    
    # single_vector = embeddings.embed_query(text)
    # print(str(single_vector)[:100])  # Show the first 100 characters of the vector
    
    # text2 = (
    #     "LangGraph is a library for building stateful, multi-actor applications with LLMs"
    # )
    # two_vectors = embeddings.embed_documents([text, text2])
    # for vector in two_vectors:
    #     print(str(vector)[:100])  # Show the first 100 characters of the vector


if __name__ == '__main__':
    embed()