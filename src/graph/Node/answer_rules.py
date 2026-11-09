import json

from graph.state import State
from utils.llm_adapter import get_llm
from graph.prompt.rules_prompt import RULES_PROMPT


def answer_rules(state: State) -> dict:
    """Responde a pergunta com base nas regras de negócio."""
    chain = RULES_PROMPT | get_llm()

    resultado = chain.invoke({
        "pergunta": state["pergunta"],
        "frota": json.dumps(state.get("frota", {}), ensure_ascii=False),
    })
    return {"resultado": resultado.text}