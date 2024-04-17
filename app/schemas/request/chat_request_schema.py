from pydantic import BaseModel


class ChatReplyRequestSchema(BaseModel):
    message: str
