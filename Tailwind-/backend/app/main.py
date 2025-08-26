from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# ✅ 引入 dataanaly
from data_analy.dataanaly import run_analysis_wrapper

app = FastAPI()

# 允许所有跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可以改成前端 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 默认用户名密码数据库
users_db = {"admin": "123456"}

# token 数据库
tokens_db = set()

# 生成一个默认 token
DEFAULT_TOKEN = "default_token_12345"
tokens_db.add(DEFAULT_TOKEN)

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def root():
    # 调用 dataanaly 的函数
    analysis_result = run_analysis_wrapper()
    return {"message": f"Hello, Codespaces! {analysis_result}"}

# POST 接口登录，返回 token
@app.post("/login")
def login_post(data: LoginRequest):
    # 可以忽略用户名密码，直接返回默认 token
    return {"message": "登录成功", "token": DEFAULT_TOKEN}

# GET 接口获取文章，前端需带 Authorization Header: Bearer token
@app.get("/posts")
def get_posts(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="未授权")
    token = authorization.split(" ")[1]
    if token not in tokens_db:
        raise HTTPException(status_code=401, detail="无效 token")
    return [
        {"id": 1, "title": "第一篇文章", "summary": "这是第一篇文章的摘要"},
        {"id": 2, "title": "第二篇文章", "summary": "这是第二篇文章的摘要"},
    ]
