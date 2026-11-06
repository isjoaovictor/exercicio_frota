prompt = """
Analise a frota abaixo e descubra qual navio chega primeiro ao destino.

Para cada navio, calcule o tempo estimado de viagem usando:
tempo_em_horas = distancia_nm / velocidade_kn


Você é um despachante de porto. O ETA em horas de cada navio é "
distancia_nm dividido por velocidade_kn. Chega primeiro quem tem o menor ETA. "
Responda com o id do navio e o ETA em horas.
caso a pergunta seja do ultimo navio, responda apenas com o id do navio e o ETA em horas."

Frota:
{frota}
"""
