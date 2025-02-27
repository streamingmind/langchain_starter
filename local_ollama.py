from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings

model = OllamaLLM(
    model="Qwen2.5-14B-Instruct-GGUF:latest",
    base_url="http://localhost:11434")

embeddings = OllamaEmbeddings(
    model="bge-m3:latest",
    base_url="http://localhost:11434"
)
