import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

load_dotenv()

from src.state import State
from src.nodes import (
    route_initial_message,
    receptionist_agent,
    classify_message,
    identificacao_agent,
    apoio_agent,
)

def specialist_router(state: State):
    return state.get("message_type")

builder = StateGraph(State)

builder.add_node("initial_router", route_initial_message)
builder.add_node("receptionist", receptionist_agent)
builder.add_node("classifier", classify_message)
builder.add_node("identificacao", identificacao_agent)
builder.add_node("apoio", apoio_agent)

builder.add_edge(START, "initial_router")

builder.add_conditional_edges(
    "initial_router",
    lambda state: state.get("next_node"),
    {"receptionist": "receptionist", "classifier": "classifier"},
)

builder.add_conditional_edges(
    "classifier",
    specialist_router,
    {"identificacao": "identificacao", "apoio": "apoio"},
)

builder.add_edge("receptionist", END)
builder.add_edge("identificacao", END)
builder.add_edge("apoio", END)

app = builder.compile()