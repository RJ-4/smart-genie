from langchain_openai import ChatOpenAI

llm: ChatOpenAI


def init_openai() -> None:

    global llm
    llm = ChatOpenAI(temperature=0)


def get_llm() -> ChatOpenAI:
    return llm
