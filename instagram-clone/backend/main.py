from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import models, database
from backend.routers import posts, comments, likes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ✅ localhost, 127.0.0.1 둘 다 허용 (개발용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,   # 쿠키 안 쓰면 False가 안전
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

@app.get("/")
def root():
    return {"message": "Instagram Clone Backend Running!"}
