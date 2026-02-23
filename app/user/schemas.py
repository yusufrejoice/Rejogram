from pydantic import BaseModel
from typing import List
from datetime import datetime

class MyPost(BaseModel):
    post_id: int
    tital: str
    contant: str

    class Config:
        orm_mode = True


class MyComment(BaseModel):
    comment_id: int
    post_id: int
    content: str

    class Config:
        orm_mode = True


class MeResponse(BaseModel):
    user_id: int
    username: str
    posts: list[MyPost]
    total_likes: int
    followers_count: int
    following_count: int
    comments: list[MyComment]

    class Config:
        orm_mode = True