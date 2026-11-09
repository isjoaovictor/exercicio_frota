
from typing import Literal, TypedDict
from pydantic import BaseModel

from graph.state import State


from utils.llm_adapter import get_llm
from graph.prompt.classify_prompt import CLASSIFY_PROMPT



class Intencao(BaseModel):
    """Representa uma intenção classificada."""
    intent: Literal[
        "primeiro_a_chegar",
        "regras",
        "fora_escopo"
    ]

def classify(state: State) -> dict:
    """Classifica a pergunta do usuário em uma das três intenções: primeiro_a_chegar, regras ou fora_escopo."""
    chain = CLASSIFY_PROMPT | get_llm().with_structured_output(
        Intencao
    )

    resposta = chain.invoke({
        "pergunta": state["pergunta"],
    })
    return {"intent": resposta.intent}
