from langchain_core.prompts import ChatPromptTemplate

ANALYZE_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Primeiro, chame reserva_ok para todos os navios e aguarde os resultados. Só depois chame velocidade_efetiva e calcular_eta_horas, exclusivamente para os navios cuja reserva foi aprovada.\n"
        "Para cada navio, é preciso analisar a reserva de combustível com a função 'reserva_ok' se ela retornar False, o modelo deve informar que ela nao pode zarpar, excluindo da comparação sem calcular o ETA dele, se o combustivel for menor que a reserva, exclua o navio da lista e nao considere ele para as perguntas.\n" 
        "Além disso, precisa ser feito tambem o calculo de velocidade efetiva com a função 'velocidade_efetiva' e o calculo do ETA com a função 'calcular_eta_horas'.\n"
        "Nunca faça calculos de cabeça, sempre utilize as funções disponibilizadas. \n"
        "Para os navios aptos, ou seja, navios que podem zarpar, use o retorno de velocidade_efetiva como argumento de calcular_eta_horas. No fim, compare os ETAs e indique qual navio chega primeiro.\n"
    ),
    (
        "human",
        "Frota: {frota}\nPergunta: {pergunta}\n"
    )
])
    