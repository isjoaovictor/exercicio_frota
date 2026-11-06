from typing import Any, TypedDict

class State(TypedDict):
    pergunta: str
    frota: Any
    resposta_llm: str
    resultado: str


state: State = {
    "pergunta": "",
    "frota": {},
    "resposta_llm": "",
    "resultado": "",
}