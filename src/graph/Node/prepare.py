from graph.state import State
import json
from graph.prompt.analyze_prompt import ANALYZE_PROMPT
from graph.tools import reserva_ok


def prepare(state: State) -> dict:
    """Prepara as mensagens para o LLM com base na frota e na pergunta do estado."""
    navios_aptos = []
    for navio in state["frota"]["navios"]:
        apto = reserva_ok.invoke(navio)
        if apto is True:
            navios_aptos.append(navio)
        frota_apta = {**state["frota"], "navios": navios_aptos}

    mensagens = ANALYZE_PROMPT.format_messages(
        frota=json.dumps(frota_apta, ensure_ascii=False),
        pergunta=state["pergunta"],
    )
    return {"messages": mensagens}
