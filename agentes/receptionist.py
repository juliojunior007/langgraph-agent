from graph.state import State
from utils.utils import get_llm

llm = get_llm()

def receptionist_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é a recepcionista do Guardião Fênix, um espaço 
            acolhedor.
            Seja calorosa, empática. Cumprimente e ofereça ajuda.
            Exemplo: 'Olá! Sou o Guardião Fênix. Estou aqui para te ouvir
              e oferecer apoio. Como posso ajudar?'
            Não fale de assuntos técnicos/financeiros.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}