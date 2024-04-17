from pydantic import Field
from app.schemas import CamelCaseSchema


class ChatReplyResponseSchema(CamelCaseSchema):
    bot_response: str = Field(default="")
    sql: str = Field(default="")
