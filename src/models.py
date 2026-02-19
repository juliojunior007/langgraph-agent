from pydantic import BaseModel, Field
from typing import Literal

class InitialRouter(BaseModel):
    """Decide se é saudação ou consulta sobre narcisismo."""
    next_node: Literal["receptionist", "classifier"] = Field(
        ...,
        description="'classifier' para mensagens sobre narcisismo/abuso, " \
        "'receptionist' para saudações.",
    )

class MessageClassifier(BaseModel):
    """Classifica em identificação de sinais ou apoio emocional."""
    message_type: Literal["identificacao", "apoio"] = Field(
        ...,
        description="'identificacao' para sinais/características, 'apoio' " \
        "para ajuda emocional.",
    )