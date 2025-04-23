from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# GitHub Pages 프론트에서 오는 요청을 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gangjisu.github.io"],  # 정확한 도메인 지정!
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/echo")
def echo_message(data: Message):
    return {"response": f"'{data.message}'를 받았습니다!"}
