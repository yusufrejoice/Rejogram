from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.followes import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.followes.models import Follow
from app.followes import models
#from app.followes.service import follow_user
from app import oauth2




router= APIRouter(
    prefix="/follow",
    tags= ['followes']
)

@router.post("/{user_id}")
def follow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):

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

    return {"message": "Followed successfully"}


@router.delete("/unfollow/{user_id}")
def unfollow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):

    follow = db.query(Follow).filter(
        Follow.follower_id == current_user.user_id,
        Follow.following_id == user_id
    )

    if not follow.first():
        raise HTTPException(status_code=404, detail="Not following this user")

    follow.delete(synchronize_session=False)
    db.commit()

    return {"message": "Unfollowed successfully"}








