from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import models, database
from backend.routers import posts, comments, likes

# DB 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# CORS 설정 (React Vite 기본 포트 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
# app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

@app.get("/")
def root():
    return {"message": "Instagram Clone Backend Running!"}
