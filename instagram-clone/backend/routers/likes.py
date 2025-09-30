from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, database

router = APIRouter(
    prefix="/likes",
    tags=["likes"]
)

# 좋아요 추가
@router.post("/{post_id}")
def add_like(post_id: int, db: Session = Depends(database.get_db)):
    return crud.add_like(db, post_id)

# 게시글 좋아요 수 조회
@router.get("/{post_id}")
def count_likes(post_id: int, db: Session = Depends(database.get_db)):
    count = crud.count_likes(db, post_id)
    return {"post_id": post_id, "likes": count}

# 좋아요 삭제
@router.delete("/{like_id}")
def remove_like(like_id: int, db: Session = Depends(database.get_db)):
    db_like = crud.remove_like(db, like_id)
    if not db_like:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"message": "Like removed successfully"}
