import os
import sys
import bs4
import json

from langchain import hub

from langchain_openai.chat_models.base import BaseChatOpenAI

from langchain_community.document_loaders import WebBaseLoader


from langgraph.graph import START, StateGraph

from typing_extensions import List, TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.output_parsers import ResponseSchema, StructuredOutputParser

