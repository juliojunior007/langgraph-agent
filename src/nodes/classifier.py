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
            "content": """Você é um classificador empático. Classifique a mensagem em:
            - 'identificacao': se a pessoa quer entender o que é narcisismo, sinais de abuso, características.
            - 'apoio': se a pessoa está sofrendo, pedindo ajuda, como lidar, como sair.
            Seja sensível e não julgue.""",
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"message_type": result.message_type}