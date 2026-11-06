from graph.state import State


def format_output(state: State) -> dict[str, str]:
    return {"resultado": f"Resposta: {state['resposta_llm']}"}