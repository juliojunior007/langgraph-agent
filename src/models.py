from pydantic import BaseModel, Field
from typing import Literal

class InitialRouter(BaseModel):
    next_node: Literal["receptionist", "classifier"] = Field(
        ...,
        description="'classifier' para mensagens sobre narcisismo/abuso, 'receptionist' para saudações.",
    )

class MessageClassifier(BaseModel):
    message_type: Literal[
        "identificacao",
        "apoio",
        "defesa",
        "soberania",
        "autocuidado"
    ] = Field(
        ...,
        description="Classifique a mensagem em: identificacao (sinais), apoio (acolhimento), defesa (técnicas como Gray Rock), soberania (recomeço, sair do relacionamento), autocuidado (bem-estar).",
    )