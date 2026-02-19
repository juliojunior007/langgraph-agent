from pydantic import BaseModel, Field
from typing import Literal

class InitialRouter(BaseModel):
    next_node: Literal["receptionist", "classifier"] = Field(
        ...,
        description="Choose 'classifier' if the user presents a clear technical or financial question. Otherwise, choose 'receptionist'.",
    )

class MessageClassifier(BaseModel):
    message_type: Literal["technical", "financial"] = Field(
        ...,
        description="Classify the message as 'technical' or 'financial'.",
    )