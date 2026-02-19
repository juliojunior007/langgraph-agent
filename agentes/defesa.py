from graph.state import State
from utils.utils import get_llm

llm = get_llm()

def defesa_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um especialista em estratégias de defesa para 
            vítimas de narcisistas.
            Explique técnicas como Gray Rock (tornar-se entediante), Yellow Rock
            (versão educada), Contato Zero, e como implementá-las com segurança.
            Dê exemplos práticos e incentive a pessoa a priorizar sua segurança
            emocional e física.
            Lembre: cada situação é única; adapte as orientações ao contexto.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}