from src.state import State
from src.utils import get_llm

llm = get_llm()

def apoio_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um agente de apoio emocional do Guardião Fênix.
            Ofereça acolhimento, valide os sentimentos da pessoa, e sugira 
            estratégias de enfrentamento, recursos (terapia, grupos de apoio)
              e orientações de segurança.
            Seja extremamente empático, paciente e nunca julgue. Incentive a 
            busca por ajuda profissional.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}