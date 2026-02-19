from src.state import State
from src.models import MessageClassifier
from src.utils import get_llm

llm = get_llm()

def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'technical': if it asks for technical support, internet issues,
              message error, login problems, or any technical assistance
            - 'financial': if it asks for financial information, prices,
              billing, or payment issues
            """,
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"message_type": result.message_type}