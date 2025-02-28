from common import *
from local_ollama import ollama_chatmodel
from qwen import qwen_chatmodel

def simple_qa():
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | ollama_chatmodel #qwen_chatmodel

    print(chain.invoke({"question": "What is LangChain?"}))
    
if __name__ == '__main__':
    simple_qa()