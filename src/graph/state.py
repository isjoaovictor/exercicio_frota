from typing import Annotated, TypedDict
from langgraph.graph import add_messages


class State(TypedDict, total=False):
    pergunta: str
    frota: dict
    intent: str
    messages: Annotated[list, add_messages]
    recomendacao: str
    aprovado: bool
    nota_operador: str
    resposta_llm: str  
    resultado: str



ESTADO_INICIAL: State = {
    "pergunta": "",
    "frota": {},
    "intent": "",
    "messages": [],
    "recomendacao": "",  
    "nota_operador": "",
    "resposta_llm": "",
    "resultado": "",
}