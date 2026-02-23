from app.post.models import post
from app.like.models import Like
from app.followes.models import Follow
from app.comment.models import comment

def get_me_service(db, current_user):

    # User Posts
    posts = db.query(post).filter(
        post.owner_id == current_user.user_id
    ).all()

    # Likes Count
    likes_count = db.query(Like).filter(
        Like.user_id == current_user.user_id
    ).count()

    # Followers Count
    followers_count = db.query(Follow).filter(
        Follow.following_id == current_user.user_id
    ).count()

    # Following Count
    following_count = db.query(Follow).filter(
        Follow.follower_id == current_user.user_id
    ).count()

    # Comments
    comments = db.query(comment).filter(
        comment.owner_id  == current_user.user_id
    ).all()

    return {
        "user_id": current_user.user_id,
        "username": current_user.username,
        "posts": posts,
        "total_likes": likes_count,
        "followers_count": followers_count,
        "following_count": following_count,
        "comments": comments
    }