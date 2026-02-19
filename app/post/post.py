from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from app.auth import schemas , models
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.service import login_user_service, add_new_user_service ,forget_password_service

rejo=FastAPI()
router= APIRouter(
    prefix="/post",
    tags= ['posts']
)


