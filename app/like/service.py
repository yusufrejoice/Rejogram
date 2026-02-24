from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.like import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
import logging
from app.like.models import Like

logger = logging.getLogger(__name__)


def add_like_service(post_id,db,current_user):

    existing_like = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == current_user.user_id
    ).first()

    if existing_like:
        raise HTTPException(status_code=400, detail="Already liked")

    new_like = Like(
        post_id=post_id,
        user_id=current_user.user_id
    )

    db.add(new_like)
    db.commit()

    logger.info(f" liked by ID {current_user.user_id} to ID {post_id}")

    return {"message": "Post liked"}


def delete_like_service(post_id,db,current_user):

    like = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == current_user.user_id
    )

    if not like.first():
        raise HTTPException(status_code=404, detail="Not liked")

    like.delete(synchronize_session=False)
    db.commit()

    logger.info(f" unliked by ID {current_user.user_id} to ID {post_id}")

    return {"message": "Post unliked"}


















# def get_all_likes_service(db):
    
#     like=db.query(models.like).all()
#     return like


# def add_new_likes_service(like,db):

#     new_like= models.like( post_id=like.post_id ,
#                           owner_id=like.owner_id
#                              )
#     db.add(new_like)
#     db.commit()
#     db.refresh(new_like)

#     return new_like


# def get_via_id_service(id,db):

#     like_details = db.query(models.like).filter(models.like.like_id==id).first()
    
    
#     if not like_details :
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
#                             detail= f"like with id : {id} was not found ")

#     return like_details


# def remove_like_service(id,db):

#     deleted_like = db.query(models.like).filter(models.like.like_id==id)
#     if not deleted_like.first() :
#         raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
#                             detail= f"like with id : {id} was not exist ")
    
#     deleted_like.delete(synchronize_session=False)
#     db.commit()
    

#     return deleted_like.first()


# def update_like_service(id,like,db):

#     updated_like = db.query(models.like).filter(
#         models.like.like_id == id
#     ).first()

#     if not updated_like :
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"like with id {id} not found"
#         )

    
#     updated_like.tital = like.tital
#     updated_like.contant = like.contant
#     updated_like.published = like.published
#     updated_like.owner_id = like.owner_id
  

#     db.commit()
#     db.refresh(updated_like)

#     return updated_like
