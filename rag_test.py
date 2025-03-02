
#https://python.langchain.com/docs/tutorials/rag/

from common import *
from qdrant import *
from local_ollama import ollama_chatmodel, ollama_embeddings
#
# Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)
# for s in all_splits: print(s)
# sys.exit(-1)

client = QdrantClient(":memory:")
client.delete_collection("test")
client.create_collection(
    collection_name="test",
    vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
)
vector_store = QdrantVectorStore(
    client=client,
    collection_name="test",
    embedding=ollama_embeddings,
)

# Index chunks
_ = vector_store.add_documents(documents=all_splits)

# Define prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")
print("prompt:", prompt)


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    for doc in retrieved_docs:
        print("retrieved:", doc.page_content)
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = ollama_chatmodel.invoke(messages)
    return {"answer": response}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

response = graph.invoke({"question": "What is Task Decomposition?"})
print(response["answer"])