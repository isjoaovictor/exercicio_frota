import os
import sys
from pathlib import Path
from langchain_core.messages import HumanMessage
from langgraph.types import Command



SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def load_environment() -> None:
    env_file = SRC_DIR / ".env"
    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


load_environment()

from utils.langfuse_client import run_config
from graph.state import ESTADO_INICIAL
from graph.builder import graph

def main() -> None:

    pergunta = input(f"Digite a pergunta: ")
    estado_inicial = {
        **ESTADO_INICIAL,
        "pergunta": pergunta,
        "messages": [HumanMessage(content=pergunta)],
    }
    opcao = input("Aprovar recomendação? (s/n): ").strip().lower()
    while opcao not in ("s", "n"):
        opcao = input("Digite s ou n: ").strip().lower()
        
    config = {"configurable": {"thread_id": "frota-1"}}
    resposta = graph.invoke(Command(resume=opcao == "s"), config=config)
    print("Aprovado:", resposta["aprovado"])
    return
    
    print(resposta["resultado"])


if __name__ == "__main__":
    main()



# Qual navio chega primeiro ao porto?
