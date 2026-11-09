from graph.state import State
from graph.tools import TOOLS
from utils.llm_adapter import get_llm


def analyze(state: State) -> dict:
    """enviar mensagens a llm e informar as ferramentas disponíveis."""
    llm = get_llm().bind_tools(TOOLS)
    return {"messages": [llm.invoke(state["messages"])]}
