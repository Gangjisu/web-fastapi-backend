from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ GitHub Pages 도메인 CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gangjisu.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 메시지 모델 정의
class Message(BaseModel):
    message: str

# ✅ /echo POST 엔드포인트
@app.post("/echo")
def echo(msg: Message):
    return {"response": f"'{msg.message}'를 잘 받았습니다!"}

# ✅ 기본 GET 엔드포인트 (선택사항이지만 없으면 / 에 404 뜸)
@app.get("/")
def read_root():
    return {"message": "FastAPI 서버는 잘 실행 중입니다!"}
