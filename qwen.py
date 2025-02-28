# https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.tongyi.ChatTongyi.html

from langchain_community.llms import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings

from common import *

os.environ["DASHSCOPE_API_KEY"] = 'sk-a76b0e8621c44ff387a90e09758b597e'

#print(Tongyi().invoke("你是谁？"))

qwen_chatmodel = ChatTongyi(model="qwen-max")

qwen_embeddings = DashScopeEmbeddings(
    dashscope_api_key="sk-a76b0e8621c44ff387a90e09758b597e",
    model="text-embedding-v3")