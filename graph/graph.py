import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

from graph.state import State
from agentes import (
    route_initial_message,
    receptionist_agent,
    classify_message,
    identificacao_agent,
    apoio_agent,
    defesa_agent,
    soberania_agent,
    autocuidado_agent,
)

def specialist_router(state: State):
    return state.get("message_type")

builder = StateGraph(State)

builder.add_node("initial_router", route_initial_message)
builder.add_node("receptionist", receptionist_agent)
builder.add_node("classifier", classify_message)
builder.add_node("identificacao", identificacao_agent)
builder.add_node("apoio", apoio_agent)
builder.add_node("defesa", defesa_agent)
builder.add_node("soberania", soberania_agent)
builder.add_node("autocuidado", autocuidado_agent)

builder.add_edge(START, "initial_router")

builder.add_conditional_edges(
    "initial_router",
    lambda state: state.get("next_node"),
    {"receptionist": "receptionist", "classifier": "classifier"},
)

builder.add_conditional_edges(
    "classifier",
    specialist_router,
    {
        "identificacao": "identificacao",
        "apoio": "apoio",
        "defesa": "defesa",
        "soberania": "soberania",
        "autocuidado": "autocuidado",
    },
)

builder.add_edge("receptionist", END)
builder.add_edge("identificacao", END)
builder.add_edge("apoio", END)
builder.add_edge("defesa", END)
builder.add_edge("soberania", END)
builder.add_edge("autocuidado", END)

app = builder.compile()