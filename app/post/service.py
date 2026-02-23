from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.post import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db


def get_all_posts_service(db,current_user):

    posts = db.query(models.post).filter(
        models.post.owner_id == current_user.user_id
    ).all()

    return posts


def add_new_post_service(post, db,current_user):

    new_post = models.post(
        tital=post.tital,
        contant=post.contant,
        published=post.published,
        owner_id=current_user.user_id   
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# def get_via_id_service(id,db,current_user):

#     post_details = db.query(models.post).filter(models.post.owner_id == current_user.user_id
#     ).all()
    
    
#     if not post_details :
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
#                             detail= f"post with id : {id} was not found ")

#     return post_details


def remove_post_service(id, db, current_user):

    deleted_post = db.query(models.post).filter(
        models.post.post_id == id,
        models.post.owner_id == current_user.user_id
    ).first()

    if not deleted_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    db.delete(deleted_post)
    db.commit()

    return {"message": "Post deleted successfully"}


def update_post_service(id, post, db, current_user):

    updated_post = db.query(models.post).filter(
        models.post.post_id == id,
        models.post.owner_id == current_user.user_id
    ).first()

    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    updated_post.tital = post.tital
    updated_post.contant = post.contant
    updated_post.published = post.published

    db.commit()
    db.refresh(updated_post)

    return updated_post