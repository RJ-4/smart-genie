import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.routes as routes
from app.services.openai import init_openai
from database import init_database


init_openai()
init_database()

app = FastAPI()
app.include_router(routes.chat_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)
