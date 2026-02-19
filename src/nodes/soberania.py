from src.state import State
from src.utils import get_llm

llm = get_llm()

def soberania_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um especialista em reconstrução de vida para
            pessoas que estão saindo de relacionamentos abusivos.
            Ofereça orientações sobre planejamento de saída, recursos 
            (abrigos, apoio psicológico), reconstrução da autoestima e autonomia.
            Ajude a pessoa a visualizar um futuro livre e a dar pequenos passos 
            rumo à independência.
            Seja acolhedor, prático e incentive a busca de redes de apoio.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}