from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, schemas, database

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/{post_id}", response_model=schemas.Comment)
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db)):
    return crud.create_comment(db, post_id, comment)

@router.get("/{post_id}", response_model=list[schemas.Comment])
def read_comments(post_id: int, db: Session = Depends(database.get_db)):
    return crud.get_comments(db, post_id)

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(database.get_db)):
    db_comment = crud.delete_comment(db, comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}
