from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, schemas, database

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

# 게시글 생성
@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    return crud.create_post(db=db, post=post)

# 게시글 목록 조회
@router.get("/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)

# 특정 게시글 조회
@router.get("/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(database.get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# 게시글 수정
@router.put("/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(database.get_db)):
    db_post = crud.update_post(db, post_id, post)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# 게시글 삭제
@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    db_post = crud.delete_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
