from graph.state import State


def refuse(state: State) -> dict:
    """Retorna uma resposta indicando que a pergunta está fora do escopo."""
    return {"resultado": "Desculpe, não posso ajudar com essa pergunta. Ela está fora do escopo do meu conhecimento."}
