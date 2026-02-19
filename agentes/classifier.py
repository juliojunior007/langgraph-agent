from graph.state import State
from graph.models import MessageClassifier
from utils.utils import get_llm

llm = get_llm()

def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Você é um classificador de intenções para um assistente de apoio a vítimas de narcisismo.
            Analise a mensagem e classifique em UMA das categorias abaixo. Ignore pontuação e foque no significado.

            Categorias:
            - 'identificacao': a pessoa quer entender o que é narcisismo, seus sinais, características, tipos. Ex: "O que é um narcisista?", "Quais os sinais de abuso?", "Como identificar um narcisista?".
            - 'apoio': a pessoa expressa sofrimento, tristeza, solidão, angústia, e busca acolhimento. Ex: "Estou me sentindo sozinha", "Ele me humilha, estou muito triste", "Não aguento mais essa situação".
            - 'defesa': a pessoa quer técnicas práticas para lidar com o agressor no dia a dia, como Gray Rock, contato zero, como agir durante conflitos. Ex: "Como fazer Gray Rock?", "O que é contato zero?", "Como me proteger emocionalmente?".
            - 'soberania': a pessoa quer orientações para sair do relacionamento, planejar a separação, recomeçar a vida, aspectos práticos da saída. Ex: "Quero sair desse relacionamento, por onde começo?", "Como me preparar para divorciar?", "Preciso de ajuda para me organizar e ir embora".
            - 'autocuidado': a pessoa quer dicas para melhorar a autoestima, bem-estar, recuperação emocional após o abuso. Ex: "Como melhorar minha autoestima?", "Dicas para me cuidar depois de tudo", "O que fazer para me sentir melhor?".

            Responda APENAS com o nome da categoria, sem explicações."""
        },
        {"role": "user", "content": last_message.content},
    ])
    return {"message_type": result.message_type}