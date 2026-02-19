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
            "content": """You are an expert at routing user messages.
                If the message is a simple greeting, a thank you, or conversational fluff,
                route to the 'receptionist'.
                If the message contains a specific question or problem about technical
                or financial issues, route to the 'classifier'.""",
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"next_node": result.next_node}