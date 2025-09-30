from sqlalchemy.orm import Session
from backend import models, schemas

# ----- Post -----
def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    posts = db.query(models.Post).offset(skip).limit(limit).all()
    result = []
    for post in posts:
        result.append(
            schemas.Post(
                id=post.id,
                title=post.title,
                content=post.content,
                created_at=post.created_at,
                updated_at=post.updated_at,
                comments=post.comments,
                likes_count=len(post.likes)
            )
        )
    return result

def get_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post:
        return schemas.Post(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at,
            updated_at=post.updated_at,
            comments=post.comments,
            likes_count=len(post.likes)
        )
    return None

def update_post(db: Session, post_id: int, post: schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

# ----- Comment -----
def create_comment(db: Session, post_id: int, comment: schemas.CommentCreate):
    db_comment = models.Comment(content=comment.content, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment

# ----- Like -----
def add_like(db: Session, post_id: int):
    db_like = models.Like(post_id=post_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def count_likes(db: Session, post_id: int):
    return db.query(models.Like).filter(models.Like.post_id == post_id).count()

def remove_like(db: Session, like_id: int):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like:
        db.delete(db_like)
        db.commit()
    return db_like
