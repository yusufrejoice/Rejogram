# from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
# from main import Session
# from app.followes import models,schemas
# from app.database import engine , SessionLocal
# from app.utils import pwd_context
# from app.utils import get_db




# router= APIRouter(
#     prefix="/follow",
#     tags= ['followes']
# )

# @router.post("/follow/{user_id}")
# def follow_user(user_id: int, current_user: int, db: Session = Depends(get_db)):

#     follow_ = models.follows(
#         follower_id=current_user,
#         following_id=user_id
#     )

#     db.add(follow_)
#     db.commit()

#     return {"message": "Followed successfully"}



# @router.delete("/unfollow/{user_id}")
# def unfollow_user(user_id: int, current_user: int, db: Session = Depends(get_db)):

#     follow_ = db.query(models.follows).filter(
#         modules.follows.follower_id == current_user,
#         modules.follows.following_id == user_id
#     ).first()

#     if follow_:
#         db.delete(follow_)
#         db.commit()

#     return {"message": "Unfollowed successfully"}




