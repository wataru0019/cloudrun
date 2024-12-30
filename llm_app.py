import os
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from typing import Annotated
from pydantic import BaseModel, Field
from langsmith import Client
from dotenv import load_dotenv
import module_yfinance

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.environ.get("LANGCHAIN_PROJECT")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

client = Client()

def kenkai_kabuka(stock_code: str):
    kabuka = module_yfinance.get_stock_price(stock_code)
    kabuka_news = module_yfinance.get_company_news(stock_code)
    kabuka_str = kabuka.to_string()
    prompt = PromptTemplate.from_template('''
    以下の株価データとニュースをもとに、株価の推移に関する見解を述べよ

    stock: {kabuka}
    news: {news}
    ''')

    chain = prompt | model | StrOutputParser()
    result = chain.invoke({"kabuka": kabuka_str, "news": kabuka_news})

    return result


def test(message: str):
    prompt = PromptTemplate.from_template('''
    ユーザーの入力に応じ、テンションが上がる応答をしてください。

    human: {message}
    ''')

    chain = prompt | model | StrOutputParser()
    result = chain.invoke({"message": message})

    print(result)

if __name__ == "__main__":
    kenkai_kabuka()

