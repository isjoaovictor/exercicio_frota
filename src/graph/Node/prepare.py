from graph.state import State
import json
from graph.prompt.analyze_prompt import ANALYZE_PROMPT


def prepare(state: State) -> dict:
    """Prepara as mensagens para o LLM com base na frota e na pergunta do estado."""
    mensagens = ANALYZE_PROMPT.format_messages(
        frota=json.dumps(state["frota"]),
        pergunta=state["pergunta"],
    )
    return {"messages": mensagens}
        



