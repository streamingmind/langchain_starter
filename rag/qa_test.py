from common import *
from local_ollama import model
def simple_qa():
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    print(chain.invoke({"question": "What is LangChain?"}))
    
if __name__ == '__main__':
    simple_qa()