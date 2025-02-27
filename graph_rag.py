#https://python.langchain.com/docs/integrations/retrievers/graph_rag/

from common import *

from qwen import embeddings, chat_model
from dataset import animals

from graph_retriever.strategies import Eager
from langchain_graph_retriever import GraphRetriever

# from pprint import pprint
# for doc in animals:
#   print(doc)
# sys.exit(-1)

vector_store = InMemoryVectorStore.from_documents(
    documents=animals,
    embedding=embeddings,
)

traversal_retriever = GraphRetriever(
    store = vector_store,
    edges = [("habitat", "habitat"), ("origin", "origin")],
    strategy = Eager(k=5, start_k=1, max_depth=2),
)


def compare():
  results = traversal_retriever.invoke("what animals could be found near a capybara?")
  for doc in results:
      print(f"{doc.id}: {doc.page_content}")

  # When max_depth=0, the graph traversing retriever behaves like a standard retriever:
  # standard_retriever = GraphRetriever(
  #     store = vector_store,
  #     edges = [("habitat", "habitat"), ("origin", "origin")],
  #     strategy = Eager(k=5, start_k=5, max_depth=0),
  # )
  standard_retriever = vector_store.as_retriever(search_kwargs={"k":5})
  results = standard_retriever.invoke("what animals could be found near a capybara?")

  for doc in results:
      print(f"{doc.id}: {doc.page_content}")
  
def chain_invoke():
  prompt = ChatPromptTemplate.from_template(
  """Answer the question based only on the context provided.

  Context: {context}

  Question: {question}"""
  )

  def format_docs(docs):
      return "\n\n".join(f"text: {doc.page_content} metadata: {doc.metadata}" for doc in docs)

  chain = (
      {"context": traversal_retriever | format_docs, "question": RunnablePassthrough()}
      | prompt
      | chat_model
      | StrOutputParser()
  )
  
  print(chain.invoke("what animals could be found near a capybara?"))

chain_invoke()