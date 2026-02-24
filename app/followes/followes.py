from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.followes import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.followes.models import Follow
from app.followes import models
#from app.followes.service import follow_user
from app import oauth2
import logging
from app.followes.service import follow_service , unfollow_service

logger = logging.getLogger(__name__)




router= APIRouter(
    prefix="/follow",
    tags= ['followes']
)

@router.post("/{user_id}")
def follow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    
    logger.info("POST /follow/{user_id} endpoint called")

    return follow_service(user_id,db,current_user)

    


@router.delete("/unfollow/{user_id}")
def unfollow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    
    logger.info("delete /follow/unfollow/{user_id} endpoint called")

    return unfollow_service(user_id,db,current_user)

   








