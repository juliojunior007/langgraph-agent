import streamlit as st
from src.graph import app  # Importa o grafo compilado do agent.py
from langchain_core.messages import HumanMessage, AIMessage
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
# Título da aplicação
st.title("🤖 Atendimento Inteligente")
st.markdown("Teste o assistente com mensagens de saudação, suporte técnico ou financeiro.")

# Inicializa o histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo de entrada do usuário
if prompt := st.chat_input("Digite sua mensagem..."):
    # Adiciona a mensagem do usuário ao histórico e exibe
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara o estado para o grafo (formato esperado: lista de mensagens)
    # O grafo espera objetos HumanMessage, então convertemos
    langgraph_messages = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            langgraph_messages.append(HumanMessage(content=m["content"]))
        else:
            langgraph_messages.append(AIMessage(content=m["content"]))

    # Invoca o grafo
    with st.spinner("Processando..."):
        try:
            output = app.invoke({"messages": langgraph_messages})
            # A última mensagem do estado é a resposta do assistente
            resposta = output["messages"][-1].content
        except Exception as e:
            resposta = f"Erro: {e}"

    # Adiciona a resposta ao histórico e exibe
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)