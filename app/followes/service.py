from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.followes import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from followes.models import Follow
from app import oauth2
from fastapi.security import OAuth2PasswordRequestForm

# @router.post("/{user_id}", response_model=schemas.FollowResponse)
# def follow_user(user_id: int,
#                 db: Session = Depends(get_db),
#                 current_user = Depends(get_current_user)):

#     if user_id == current_user.id:
#         raise HTTPException(status_code=400, detail="You cannot follow yourself")

#     existing = db.query(Follow).filter(
#         Follow.follower_id == current_user.id,
#         Follow.following_id == user_id
#     ).first()

#     if existing:
#         raise HTTPException(status_code=400, detail="Already following")

#     new_follow = Follow(
#         follower_id=current_user.id,
#         following_id=user_id
#     )

#     db.add(new_follow)
#     db.commit()
#     db.refresh(new_follow)

#     return new_follow


# @router.delete("/{user_id}")
# def unfollow_user(user_id: int,
#                   db: Session = Depends(get_db),
#                   current_user = Depends(get_current_user)):

#     follow = db.query(Follow).filter(
#         Follow.follower_id == current_user.id,
#         Follow.following_id == user_id
#     ).first()

#     if not follow:
#         raise HTTPException(status_code=404, detail="Follow not found")

#     db.delete(follow)
#     db.commit()

#     return {"message": "Unfollowed successfully"}