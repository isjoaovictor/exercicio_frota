from graph.state import State


def format_output(state: State) -> dict[str, str]:
    if state["aprovado"] is False:
        return {"resultado": f"Recomendação rejeitada pelo operador."}
    else:
        return {"resultado": state["recomendacao"]}
