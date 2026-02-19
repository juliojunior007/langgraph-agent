from src.state import State
from src.utils import get_llm

llm = get_llm()

def identificacao_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um especialista em psicologia, focado em ajudar pessoas a identificarem comportamentos narcisistas.
            Explique sinais, características e como reconhecer um relacionamento abusivo.
            Seja claro, acolhedor e use linguagem simples.
            Lembre-se: você não substitui um profissional, mas oferece orientação inicial.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}