from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.like.models import Like
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from app.like.service import  add_like_service , delete_like_service
import logging

logger = logging.getLogger(__name__)

router= APIRouter(
    prefix="/like",
    tags= ['likes']
)

air = FastAPI()


@router.post("/add/{post_id}")
def like_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    
    logger.info(f"User {current_user.user_id} trying to like to {post_id}")
    
    return add_like_service(post_id,db,current_user)

    


@router.delete("/remove/{post_id}")
def unlike_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    logger.info(f"User {current_user.user_id} trying to delete like to {post_id}")

    return delete_like_service(post_id,db,current_user)