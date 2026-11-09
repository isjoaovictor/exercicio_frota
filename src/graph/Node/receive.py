import json
from pathlib import Path

from graph.state import State


DATA_FILE = Path(__file__).parents[2] / "dados" / "frota_tempestade.json"


def receive(state: State) -> dict[str, object]:
    """Recebe a frota de navios do arquivo JSON e retorna um dicionário contendo a frota."""
    with DATA_FILE.open(encoding="utf-8") as file:
        frota = json.load(file)

    return {"frota": frota}