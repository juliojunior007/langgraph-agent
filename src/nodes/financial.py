from langchain_openai import ChatOpenAI
from src.state import State

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0, max_tokens=300)

def financial_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": "You are a financial support specialist. Your mission is to help customers with billing, payment, and refund questions in an empathetic and precise manner.",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}