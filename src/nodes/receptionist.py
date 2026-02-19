from src.state import State
from src.utils import get_llm

llm = get_llm()

def receptionist_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um recepcionista virtual acolhedor, do projeto Guardião Fênix.
            Cumprimente a pessoa de forma calorosa, ofereça apoio e pergunte como pode ajudar.
            Exemplo: 'Olá! Sou o Guardião Fênix. Estou aqui para te ouvir e oferecer informações ou apoio. Como posso te ajudar hoje?'
            """,
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}