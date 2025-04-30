from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import os

BSER_API_KEY  = os.getenv('BSER_API_KEY')
BSER_BASE_URL = os.getenv('BSER_BASE_URL')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에선 도메인 지정 권장
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/user")
def get_user_info(nickname: str):
    url = f"{BSER_BASE_URL}/v1/user/nickname"
    headers = {"x-api-key": BSER_API_KEY}
    params = {"query": nickname}
    resp = requests.get(url, headers=headers, params=params)
    return resp.json().get("user",{})

# [2] Get user rank info
@app.get("/user/rank")
def get_user_rank(user_num, season_id):
    url = f"{BSER_BASE_URL}/v1/rank/{user_num}/{season_id}/3" #{team_mode}
    headers = {"x-api-key": BSER_API_KEY}
    resp = requests.get(url, headers=headers) # print("▶ Get User Rank:", resp.status_code)
    return resp.json().get("userRank",{})
# [2]

# [3] Get user stats
@app.get("/user/stats")
def get_user_stats(user_num, season_id):
    url = f"{BSER_BASE_URL}/v1/user/stats/{user_num}/{season_id}"
    headers = {"x-api-key": BSER_API_KEY}
    resp = requests.get(url, headers=headers) # print("▶ Get User Stats:", resp.status_code)
    return resp.json().get("userStats",{})
# [3]

# [4] Get user games
@app.get("/user/games")
def get_user_games(user_num):
    url = f"{BSER_BASE_URL}/v1/user/games/{user_num}"
    headers = {"x-api-key": BSER_API_KEY}
    resp = requests.get(url, headers=headers) # print("▶ Get User Games:", resp.status_code)
    return resp.json().get("userGames",{})
# [4]
