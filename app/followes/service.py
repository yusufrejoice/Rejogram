from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.followes import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.followes.models import Follow
from app.followes import models
from app import oauth2
import logging


logger = logging.getLogger(__name__)




def follow_service(user_id,db,current_user):

    if user_id == current_user.user_id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    existing_follow = db.query(Follow).filter(
        Follow.follower_id == current_user.user_id,
        Follow.following_id == user_id
    ).first()

    if existing_follow:
        raise HTTPException(status_code=400, detail="Already following")

    new_follow = Follow(
        follower_id=current_user.user_id,
        following_id=user_id
    )

    db.add(new_follow)
    db.commit()

    logger.info(f" followed by ID {current_user.user_id} to ID {user_id}")

    return {"message": "Followed successfully"}



def unfollow_service(user_id,db,current_user):

    follow = db.query(Follow).filter(
        Follow.follower_id == current_user.user_id,
        Follow.following_id == user_id
    )

    if not follow.first():
        raise HTTPException(status_code=404, detail="Not following this user")

    follow.delete(synchronize_session=False)
    db.commit()

    logger.info(f" unfollowed by ID {current_user.user_id} to ID {user_id}")

    return {"message": "Unfollowed successfully"}