from common import BaseChatOpenAI
llm = BaseChatOpenAI(
    model='deepseek-chat', 
    openai_api_key='sk-1786860c976a4ca09373074943f6fd20', 
    openai_api_base='https://api.deepseek.com',
    max_tokens=64*1024
)
response = llm.invoke("Hi!")
print(response.content)