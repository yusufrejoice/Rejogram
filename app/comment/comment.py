from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.comment import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.oauth2 import get_current_user
from app.comment.service import  get_all_comments_service , add_new_comments_service , get_via_id_service ,remove_cmt_service ,update_cmt_service

import logging

logger = logging.getLogger(__name__)

router= APIRouter(
    prefix="/comment",
    tags= ['comments']
)

air = FastAPI()


# getting all commants   
@router.get("/get_all")
def get_all_commants(db: Session = Depends(get_db)):

    logger.info("GET /comment/get_all endpoint called")

    return get_all_comments_service(db)



# add commants 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.cmt_response)
def add_new_comments(
    cmt: schemas.cmt_request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    logger.info(f"User {current_user.user_id} hitting ADD comment endpoint")

    return add_new_comments_service(cmt, db, current_user)



#delete comment      
@router.delete("/remove/{id}")
def remove_cmt(
    id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    logger.info(f"User {current_user.user_id} trying to delete comment {id}")

    return remove_cmt_service(id, db, current_user)



# update comment
@router.put("/update/{id}", response_model=schemas.cmt_response)
def update_cmt(
    id: int,
    cmt: schemas.cmt_request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    logger.info(f"User {current_user.user_id} updating comment {id}")

    return update_cmt_service(id, cmt, db, current_user)