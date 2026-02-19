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

graph_builder = StateGraph(State)

graph_builder.add_node("initial_router", route_initial_message)
graph_builder.add_node("receptionist", receptionist_agent)
graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("identificacao", identificacao_agent)
graph_builder.add_node("apoio", apoio_agent)

graph_builder.add_edge(START, "initial_router")

graph_builder.add_conditional_edges(
    "initial_router",
    lambda state: state.get("next_node"),
    {"receptionist": "receptionist", "classifier": "classifier"},
)

graph_builder.add_conditional_edges(
    "classifier",
    specialist_router,
    {"identificacao": "identificacao", "apoio": "apoio"},
)

graph_builder.add_edge("receptionist", END)
graph_builder.add_edge("identificacao", END)
graph_builder.add_edge("apoio", END)

app = graph_builder.compile()