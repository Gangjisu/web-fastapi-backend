from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# GitHub Pages 주소 허용 (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gangjisu.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/echo")
def echo_message(msg: Message):
    return {"response": f"'{msg.message}'를 잘 받았습니다!"}
