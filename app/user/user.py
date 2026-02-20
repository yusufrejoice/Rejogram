from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.models import User
from app.post.models import Post
from app.comment.models import Comment
from app.like.models import Like
from app.follows.models import Follow

router = APIRouter()

@router.get("/profile/{user_id}")
def get_profile(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    posts = db.query(Post).filter(Post.user_id == user_id).all()

    followers = db.query(Follow).filter(Follow.following_id == user_id).count()

    following = db.query(Follow).filter(Follow.follower_id == user_id).count()

    comments = db.query(Comment).filter(Comment.user_id == user_id).all()

    likes = db.query(Like).filter(Like.user_id == user_id).all()

    return {
        "username": user.username,
        "followers": followers,
        "following": following,
        "posts": posts,
        "comments": comments,
        "likes": likes
    }