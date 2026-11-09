from graph.state import State
from langgraph.types import interrupt


def human_review(state: State) -> dict:
    mensagem = state["messages"][-1].text
    interrupt({"recomendacao": mensagem})
    return {"recomendacao": mensagem}
