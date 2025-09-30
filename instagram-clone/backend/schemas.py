from pydantic import BaseModel
from datetime import datetime

# ----- Comment -----
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ----- Like -----
class Like(BaseModel):
    id: int
    post_id: int

    class Config:
        from_attributes = True

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
    comments: list[Comment] = []
    likes_count: int = 0

    class Config:
        from_attributes = True
