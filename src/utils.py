import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm(model="gpt-4o-mini", temperature=0.0, max_tokens=200):
    return ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens)