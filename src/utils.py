import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def load_environment():
    """Carrega as variáveis de ambiente do arquivo .env"""
    load_dotenv()

def get_llm(model="gpt-4o-mini", temperature=0.0, max_tokens=300):
    """Retorna uma instância do ChatOpenAI configurada"""
    return ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens)