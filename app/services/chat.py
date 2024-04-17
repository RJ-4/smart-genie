from typing import Union, Sequence, Dict, Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.utils import Output
from sqlalchemy import Result

from app.prompts.prompts import get_sql_query_prompt, get_bot_response_prompt
from app.schemas.request import ChatReplyRequestSchema
from app.schemas.response import ChatReplyResponseSchema

from langchain_core.runnables import RunnablePassthrough

from app.services.openai import get_llm
from database import get_schema, execute_sql


def reply(chat_reply_request: ChatReplyRequestSchema) -> ChatReplyResponseSchema:

    sql = generate_sql(chat_reply_request.message)
    rows = execute_sql(sql)
    bot_response = generate_bot_response(rows)

    return ChatReplyResponseSchema(bot_response=bot_response, sql=sql)


def generate_sql(text: str) -> Output:

    sql_query_chain = (
            RunnablePassthrough.assign(schema=get_schema)
            | get_sql_query_prompt()
            | get_llm().bind(stop="\nSQL Result:")
            | StrOutputParser()
    )
    return sql_query_chain.invoke({"question": text})


def generate_bot_response(db_rows: Union[str, Sequence[Dict[str, Any]], Result[Any]]) -> str:

    prompt = get_bot_response_prompt().format(db_rows=db_rows)
    openai_response = str(get_llm().invoke(prompt))
    bot_response_content = openai_response.split("response_metadata")[0]
    bot_response = bot_response_content.split("content=")[1].replace("'", "")

    return bot_response
