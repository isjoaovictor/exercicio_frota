from graph.state import State


def decide(state: State) -> dict[str, str]:
    """Usa a conclusão do analyze (última mensagem do modelo, após as ferramentas)."""
    mensagens = state.get("messages", [])

    for mensagem in reversed(mensagens):
        if mensagem.type == "ai" and not getattr(mensagem, "tool_calls", None):
            texto = mensagem.text
            if texto:
                return {"resposta_llm": texto}

    raise RuntimeError("Nenhuma resposta final do modelo foi encontrada em 'messages'.")
