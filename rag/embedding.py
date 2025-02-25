from graph_rag_example_helpers.datasets.animals import fetch_documents
animals = fetch_documents()

import getpass
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(
#     model="bge-m3:latest",
# )

model = OllamaLLM(model="Qwen2.5-14B-Instruct-GGUF:latest")

embeddings = OllamaEmbeddings(
    model="bge-m3:latest",
)

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
def simple_qa():
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    print(chain.invoke({"question": "What is LangChain?"}))


if __name__ == '__main__':
    embed()