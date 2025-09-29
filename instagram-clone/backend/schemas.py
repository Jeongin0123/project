from pydantic import BaseModel
from datetime import datetime

# ----- Post -----
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# ----- Comment -----
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True


# ----- Like -----
class Like(BaseModel):
    id: int
    post_id: int

    class Config:
        orm_mode = True
