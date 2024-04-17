from fastapi import APIRouter,status

from app.schemas.request import ChatReplyRequestSchema
from app.schemas.response import ChatReplyResponseSchema
from app.services.chat import reply as chat_reply

router = APIRouter(
    prefix="/smart-genie-rs/v1/chats",
    tags=["chats"]
)


@router.post(
    "/reply",
    status_code=status.HTTP_200_OK
)
def reply(reply_request: ChatReplyRequestSchema) -> ChatReplyResponseSchema:

    return chat_reply(reply_request)