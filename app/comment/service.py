from fastapi import HTTPException, status
from app.comment import models
import logging

logger = logging.getLogger(__name__)




def get_all_comments_service(db):

    logger.info("Fetching all comments")

    comments = db.query(models.comment).all()

    logger.info(f"Total comments fetched: {len(comments)}")

    return comments



def add_new_comments_service(comment, db, current_user):

    logger.info(f"User {current_user.user_id} is adding a comment")

    new_cmt = models.comment(
        contant=comment.contant,
        published=comment.published,
        post_id=comment.post_id,
        owner_id=current_user.user_id   
    )

    db.add(new_cmt)
    db.commit()
    db.refresh(new_cmt)

    logger.info(f"Comment created with ID {new_cmt.cmt_id}")

    return new_cmt




def get_via_id_service(id, db):

    logger.info(f"Fetching comment with ID {id}")

    cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id
    ).first()

    if not cmt:
        logger.warning(f"Comment with ID {id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment with id {id} not found"
        )

    return cmt



def remove_cmt_service(id, db, current_user):

    logger.info(f"User {current_user.user_id} trying to delete comment {id}")

    deleted_cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id,
        models.comment.owner_id == current_user.user_id
    ).first()

    if not deleted_cmt:
        logger.warning(f"Delete failed for comment {id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )

    db.delete(deleted_cmt)
    db.commit()

    logger.info(f"Comment {id} deleted successfully")

    return {"message": "Deleted successfully"}



# Update Comment 
def update_cmt_service(id, comment, db, current_user):

    logger.info(f"User {current_user.user_id} updating comment {id}")

    updated_cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id,
        models.comment.owner_id == current_user.user_id   
    ).first()

    if not updated_cmt:
        logger.warning(f"Update failed for comment {id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found or not authorized"
        )

    updated_cmt.contant = comment.contant
    updated_cmt.published = comment.published

    db.commit()
    db.refresh(updated_cmt)

    logger.info(f"Comment {id} updated successfully")

    return updated_cmt