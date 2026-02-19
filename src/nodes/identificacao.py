from src.state import State
from src.utils import get_llm

llm = get_llm()

def identificacao_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um especialista em psicologia. Ajude a
            identificar comportamentos narcisistas.
            Explique sinais (falta de empatia, manipulação, etc.) de forma 
            clara e acolhedora.
            Lembre: você não substitui um profissional. Incentive busca de 
            ajuda.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}