from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings

ollama_chatmodel = OllamaLLM(
    model="modelscope.cn/AI-ModelScope/Qwen2-VL-7B-Instruct-GGUF:latest", #"Qwen2.5-14B-Instruct-GGUF:latest",
    base_url="http://localhost:11434",
    temperature=0)

ollama_embeddings = OllamaEmbeddings(
    model="bge-m3:latest",
    base_url="http://localhost:11434"
)
