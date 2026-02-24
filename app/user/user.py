from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import get_db
from app import oauth2
from app.user.service import get_me_service
from app.user.schemas import MeResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
@router.get("/me", response_model=MeResponse)
def get_me(
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    logger.info(f"User {current_user.user_id} trying to get all details of himself")
    return get_me_service(db, current_user)