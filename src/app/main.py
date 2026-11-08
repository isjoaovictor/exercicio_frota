import os
import sys
from pathlib import Path


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
from graph.state import state
from graph.builder import graph

def main() -> None:

    pergunta = input(f"Digite a pergunta: ")
    estado_inicial = {**state, "pergunta": pergunta}

    resposta = graph.invoke(
        estado_inicial,
        config=run_config(),
    )

    print(f"{resposta["resultado"]}")


if __name__ == "__main__":
    main()



# Qual navio chega primeiro ao porto?
