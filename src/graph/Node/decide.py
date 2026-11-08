import json

from graph.prompt.choose_ship import prompt
from graph.state import State
from utils.llm_adapter import get_llm


def decide(state: State) -> dict[str, str]:
    llm = get_llm()

    if llm is None:
        raise RuntimeError("O LLM não está configurado.")

    frota = state["frota"]

    frota_texto = (
        json.dumps(frota, ensure_ascii=False)
        if not isinstance(frota, str)
        else frota
    )

    resposta = llm.invoke(prompt.format(frota=frota_texto))

    return {"resposta_llm": resposta.text}
