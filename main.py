from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = b3KKuHC2eR9V5hiDfAzG3aHvzWnkHx4T9zKZpFSl
BASE_URL = https://open-api.bser.io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에선 도메인 지정 권장
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/user")
def get_user_info(nickname: str):
    url = f"{BASE_URL}/v1/user/nickname"
    headers = {"x-api-key": API_KEY}
    params = {"query": nickname}
    resp = requests.get(url, headers=headers, params=params)
    return resp.json()
