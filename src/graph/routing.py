from graph.state import State



def route_by_intent(state: State) -> str:
    """Roteia o fluxo com base na intenção classificada."""
    return state["intent"]