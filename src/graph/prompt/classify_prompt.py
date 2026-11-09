from langchain_core.prompts import ChatPromptTemplate

CLASSIFY_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Classifique a pergunta como (primeiro_a_chegar) quando ele perguntar sobre qual navio chegará primeiro.\n"
        "Classifique como (regras) quando o usuario fizer perguntas que não necessitam de ferramentas, mas sim regras de negócio, exemplo: perguntas sobre tempestade ou reserva de combustível\n"
        "Classifique como (fora_escopo) quando a pergunta não estiver relacionada a frota, escopo do sistema, ou perguntas que não se encaixem nas funções previstas.\n"
    ),
    (
        "human",
        "{pergunta}"
    )
])