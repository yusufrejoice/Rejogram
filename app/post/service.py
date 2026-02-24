from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.post import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
import logging

logger = logging.getLogger(__name__)


def get_all_posts_service(db,current_user):

    posts = db.query(models.post).filter.all()

    logger.info(f" getting all post" )

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

    logger.info(f" uploaded by ID {current_user.user_id} to ID {id}")

    return new_post




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

    logger.info(f" deleted by ID {current_user.user_id} to ID {id}")

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

    logger.info(f" updated by ID {current_user.user_id} to ID {id}")

    return updated_post