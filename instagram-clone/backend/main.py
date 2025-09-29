from fastapi import FastAPI
from . import models, database
from .routers import posts, comments, likes

# DB 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# 라우터 등록
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

@app.get("/")
def root():
    return {"message": "Instagram Clone Backend Running!"}
