from src.state import State
from src.models import InitialRouter
from src.utils import get_llm

llm = get_llm()

def route_initial_message(state: State):
    last_message = state["messages"][-1]
    router_llm = llm.with_structured_output(InitialRouter)
    result = router_llm.invoke([
        {
            "role": "system",
            "content": """Você é um especialista em rotear mensagens para
              o Guardião Fênix.
            Se for saudação (oi, olá, bom dia) → 'receptionist'.
            Se falar sobre relacionamento, narcisismo, abuso, ou pedir ajuda →
              'classifier'.""",
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"next_node": result.next_node}