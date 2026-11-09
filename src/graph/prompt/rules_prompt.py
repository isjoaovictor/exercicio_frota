from langchain_core.prompts import ChatPromptTemplate
from utils.llm_adapter import get_llm
from graph.state import State

RULES_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Para um navio que estiver em uma tempestade, a velocidade máxima permitida é de 12 nós.\n"
        "Um navio com combustível abaixo da reserva mínima não pode zarpar(não pode viajar).\n"
        "O tempo estimado de viagem é medido pela distancia dividido pela velocidade efetiva do navio, e o resultado é dado em horas.\n"
        "Responda a pergunta somente com base nas regras de negócio acima, sem utilizar ferramentas externas.\n"
    ),
    (
        "human",
        "{pergunta}"
    )
])

