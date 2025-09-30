from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ----- User -----
# class UserBase(BaseModel):
#     email: EmailStr
#     username: str

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     created_at: datetime
#     class Config:
#         from_attributes = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     email: Optional[str] = None

# ----- Comment -----
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int
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
