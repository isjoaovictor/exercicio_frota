from langchain_core.prompts import ChatPromptTemplate

ANALYZE_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "A frota recebida ja esta apta para zarpar, pelo filtro feito pelo nó 'prepare'.\n"
        "Além disso, precisa ser feito tambem o calculo de velocidade efetiva com a função 'velocidade_efetiva' e o calculo do ETA com a função 'calcular_eta_horas'.\n"
        "Nunca faça calculos de cabeça, sempre utilize as funções disponibilizadas. \n"
        "Para os navios aptos, ou seja, navios que podem zarpar, use o retorno de velocidade_efetiva como argumento de calcular_eta_horas. No fim, compare os ETAs e indique qual navio chega primeiro.\n"
        "Para cada navio apto, mostre a velocidade original, a velocidade efetiva e o ETA. Se as duas velocidades forem iguais, escreva “velocidade mantida”. Se a efetiva for menor, escreva “velocidade reduzida de X para Y nós”. Informe o motivo da redução apenas se estiver nos dados da frota.\n"
    ),
    (
        "human",
        "Frota: {frota}\nPergunta: {pergunta}\n"
    )
])
