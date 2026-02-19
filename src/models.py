from pydantic import BaseModel, Field
from typing import Literal

class InitialRouter(BaseModel):
    next_node: Literal["receptionist", "classifier"] = Field(
        ...,
        description="Escolha 'classifier' se a mensagem for sobre narcisismo ou pedido de ajuda. Caso contrário, 'receptionist' para saudações.",
    )

class MessageClassifier(BaseModel):
    message_type: Literal["identificacao", "apoio"] = Field(
        ...,
        description="Classifique como 'identificacao' (perguntas sobre sinais, características) ou 'apoio' (pedidos de ajuda emocional, como sair).",
    )