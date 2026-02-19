import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

# Carrega variáveis de ambiente antes de qualquer coisa
load_dotenv()

from src.state import State
from src.nodes import (
    route_initial_message,
    receptionist_agent,
    classify_message,
    technical_agent,
    financial_agent,
)

def specialist_router(state: State):
    return state.get("message_type")

# Construção do grafo
graph_builder = StateGraph(State)

graph_builder.add_node("initial_router", route_initial_message)
graph_builder.add_node("receptionist", receptionist_agent)
graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("technical", technical_agent)
graph_builder.add_node("financial", financial_agent)

graph_builder.add_edge(START, "initial_router")

graph_builder.add_conditional_edges(
    "initial_router",
    lambda state: state.get("next_node"),
    {"receptionist": "receptionist", "classifier": "classifier"},
)

graph_builder.add_conditional_edges(
    "classifier",
    specialist_router,
    {"technical": "technical", "financial": "financial"},
)

graph_builder.add_edge("receptionist", END)
graph_builder.add_edge("technical", END)
graph_builder.add_edge("financial", END)

app = graph_builder.compile()