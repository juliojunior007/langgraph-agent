from src.state import State
from src.utils import get_llm

llm = get_llm()

def technical_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": "You are a technical support specialist. Your mission is to help customers with technical issues, internet problems, message errors, and login issues in a clear and helpful manner.",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}