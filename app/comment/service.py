from fastapi import HTTPException, status
from app.comment import models

# get all comments
def get_all_comments_service(db):

    comments = db.query(models.comment).all()

    return comments

# Add Comment
def add_new_comments_service(comment, db, current_user):

    new_cmt = models.comment(
        contant=comment.contant,
        published=comment.published,
        post_id=comment.post_id,
        owner_id=current_user.user_id   
    )

    db.add(new_cmt)
    db.commit()
    db.refresh(new_cmt)

    return new_cmt


# Get Comment by ID 
def get_via_id_service(id, db):

    cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id
    ).first()

    if not cmt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment with id {id} not found"
        )

    return cmt

# update comment
def remove_cmt_service(id, db, current_user):

    deleted_cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id,
        models.comment.owner_id == current_user.user_id
    ).first()

    if not deleted_cmt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )

    db.delete(deleted_cmt)
    db.commit()

    return {"message": "Deleted successfully"}


# Update Comment 
def update_cmt_service(id, comment, db, current_user):

    updated_cmt = db.query(models.comment).filter(
        models.comment.cmt_id == id,
        models.comment.owner_id == current_user.user_id   
    ).first()

    if not updated_cmt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found or not authorized"
        )

    updated_cmt.contant = comment.contant
    updated_cmt.published = comment.published

    db.commit()
    db.refresh(updated_cmt)

    return updated_cmt