from graph.state import State
from utils.utils import get_llm

llm = get_llm()

def apoio_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """Você é um agente de apoio emocional. Ofereça acolhimento,
              valide sentimentos, sugira estratégias e recursos (terapia, grupos).
            Seja extremamente empático e nunca julgue.""",
        },
        {"role": "user", "content": last_message.content},
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}