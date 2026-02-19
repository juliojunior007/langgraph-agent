from graph.state import State
from utils.utils import get_llm

llm = get_llm()

def autocuidado_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um especialista em autocuidado para pessoas que passaram por relacionamentos abusivos.
            Ofereça dicas práticas para reconstruir a autoestima, lidar com ansiedade, praticar mindfulness, e sugestões de atividades de bem-estar.
            Reforce a importância de apoio profissional (terapia) e grupos de apoio.
            Seja acolhedor e inspire esperança, lembrando que a recuperação é um processo.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}