import streamlit as st
from src.graph import app
from langchain_core.messages import HumanMessage, AIMessage
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

st.set_page_config(page_title="Guardião Fênix", page_icon="🛡️")
st.title("🛡️ Guardião Fênix")
st.markdown("Apoio para pessoas em relacionamentos abusivos.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    langgraph_messages = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            langgraph_messages.append(HumanMessage(content=m["content"]))
        else:
            langgraph_messages.append(AIMessage(content=m["content"]))

    with st.spinner("Processando..."):
        try:
            output = app.invoke({"messages": langgraph_messages})
            resposta = output["messages"][-1].content
        except Exception as e:
            resposta = f"Erro: {e}"

    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)