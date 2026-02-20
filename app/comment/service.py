from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.comment import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db


def get_all_comments_service(db):
    
    cmt=db.query(models.comment).all()
    return cmt


def add_new_comments_service(comment,db):

    new_cmt= models.comment( contant=comment.contant, 
                             published=comment.published,
                             post_id=comment.post_id ,
                             owner_id=comment.owner_id
                             )
    db.add(new_cmt)
    db.commit()
    db.refresh(new_cmt)

    return new_cmt


def get_via_id_service(id,db):

    cmt_details = db.query(models.comment).filter(models.comment.cmt_id==id).first()
    
    
    if not cmt_details :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"commennts with id : {id} was not found ")

    return cmt_details


def remove_cmt_service(id,db):

    deleted_cmt = db.query(models.comment).filter(models.comment.cmt_id==id)
    if not deleted_cmt.first() :
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"comment with id : {id} was not exist ")
    
    deleted_cmt.delete(synchronize_session=False)
    db.commit()
    

    return deleted_cmt.first()


def update_cmt_service(id,comment,db):

    updated_cmt = db.query(models.post).filter(
        models.post.post_id == id
    ).first()

    if not updated_cmt :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found"
        )

    
    updated_cmt.tital = comment.tital
    updated_cmt.contant = comment.contant
    updated_cmt.published = comment.published
    updated_cmt.owner_id = comment.owner_id
  

    db.commit()
    db.refresh(updated_cmt)

    return updated_cmt
