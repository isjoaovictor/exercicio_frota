from langchain.tools import tool

LIMITE_TEMPESTADE_KN = 12

@tool
def calcular_eta_horas(distancia_nm: float, velocidade_kn: float) -> float:
    """Calcula o ETA (Estimated Time of Arrival) em horas com base na distância em milhas náuticas e na velocidade em nós."""
    eta_horas = distancia_nm / velocidade_kn
    return round(eta_horas, 2)

@tool
def velocidade_efetiva(velocidade_kn: float, em_tempestade: bool, frota: dict) -> float:
    """Verifica se há uma tempestade e ajusta a velocidade de acordo."""
    if em_tempestade:
        return min(velocidade_kn, LIMITE_TEMPESTADE_KN)

    return velocidade_kn

@tool
def reserva_ok(combustivel_t: float, reserva_t: float) -> bool:
    """Verifica se a reserva de combustível é suficiente."""
    return combustivel_t >= reserva_t

TOOLS = [calcular_eta_horas, velocidade_efetiva, reserva_ok]

