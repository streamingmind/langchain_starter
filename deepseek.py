from common import BaseChatOpenAI

deepseek_chatmodel = BaseChatOpenAI(
    model='deepseek-chat', 
    openai_api_key='sk-1786860c976a4ca09373074943f6fd20', 
    openai_api_base='https://api.deepseek.com',
)
#response = deepseek_chatmodel.invoke("Hi!")
#print(response.content)