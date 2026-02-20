from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.post import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db


def get_all_posts_service(db):
    
    post=db.query(models.post).all()
    return post


def add_new_post_service(post,db):

    new_post= models.post(tital=post.tital,
                          contant=post.contant,
                          published=post.published,
                          owner_id=post.owner_id,
                          )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_via_id_service(id,db):

    post_details = db.query(models.post).filter(models.post.post_id==id).first()
    
    
    if not post_details :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"post with id : {id} was not found ")

    return post_details


def remove_post_service(id,db):

    deleted_post = db.query(models.post).filter(models.post.post_id==id)
    if not deleted_post.first() :
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"post with id : {id} was not exist ")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    

    return deleted_post.first()


def update_post_service(id,post,db):

    updated_post = db.query(models.post).filter(
        models.post.post_id == id
    ).first()

    if not updated_post :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found"
        )

    
    updated_post.tital = post.tital
    updated_post.contant = post.contant
    updated_post.published = post.published
    updated_post.owner_id = post.owner_id
  

    db.commit()
    db.refresh(updated_post)

    return updated_post
