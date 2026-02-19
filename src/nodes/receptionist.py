from src.state import State
from src.utils import get_llm

llm = get_llm()

def receptionist_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": "You are a friendly and helpful AI receptionist for "
            "a customer service center. Greet the user, and ask them how you "
            "can help with their technical or financial questions. Keep your "
            "responses brief and polite.",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}