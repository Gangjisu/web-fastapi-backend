from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gangjisu.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.options("/echo")
async def options_echo(request: Request):
    return JSONResponse(status_code=200)

@app.post("/echo")
def echo_message(msg: Message):
    return {"response": f"'{msg.message}'를 잘 받았습니다!"}
