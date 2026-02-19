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
            "content": """Classifique a mensagem em UMA das seguintes categorias:
            - 'identificacao': quer entender sinais, características do narcisismo.
            - 'apoio': está sofrendo, pedindo ajuda emocional, como lidar com sentimentos.
            - 'defesa': quer técnicas práticas para se proteger (Gray Rock, contato zero, como agir).
            - 'soberania': busca orientação para sair do relacionamento, recomeçar a vida, organizar recursos.
            - 'autocuidado': dicas de recuperação, autoestima, bem-estar.
            Seja sensível e preciso.""",
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"message_type": result.message_type}