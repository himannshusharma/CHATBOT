# LANGCHIAN_API_KEY="lsv2_sk_5...3f34"
# OPENAI_API_KEY="sk-proj-OOEuXoAzrkqHEZiMYJXbT3BlbkFJogbk0AoihHdCK4y31Qo5"
# LANGCHAIN_PROJECT="MyChatBot"


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


## langsmith tracking

os.environ["LANGCHIAN_API_KEY"]=os.getenv("LANGCHIAN_API_KEY")
os.environ["LANGCHIAN_TRACING_V2"]="true"

## creating a chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. please provide response to the user qurries"),
        ("user","question:{question}")
    ]
)

## streamlit framework 

st.title("Langchain Demo With llama2  API")
input_text=st.text_input("search the topic you want")

## open source AI LLm call 


llm = Ollama(model="llama2")

output_parser=StrOutputParser()

## chain

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))