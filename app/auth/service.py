from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.user import models
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2 
from app.database import engine , SessionLocal
import logging

logger = logging.getLogger(__name__)


# singin account

def login_user_service(user_credentials, db: Session):

    logger.info(f"Login attempt for email: {user_credentials.username}")
        
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
    ).first()

    if not user:
        logger.warning(f"Login failed - user not found: {user_credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid credentials"
        )
    
    if not utils.verify(user_credentials.password, user.password):
        logger.warning(f"Login failed - wrong password for: {user_credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid credentials"
        )
    
    access_token = oauth2.create_access_token(
        data={"user_id": str(user.user_id)}
    )

    logger.info(f"Login successful for user_id: {user.user_id}")

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



# singup account

def add_new_user_service(user, db):

    logger.info(f"Signup attempt for username: {user.username}")

    user_data = user.dict()
    user_data["password"] = pwd_context.hash(user.password)

    new_user = models.User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"New user created with ID: {new_user.user_id}")

    return new_user


# forget password

def forget_password_service(username: str, new_password: str, db: Session):

    logger.warning(f"Password reset attempt for username: {username}")

    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if not user:
        logger.error(f"Password reset failed - user not found: {username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    hashed_password = pwd_context.hash(new_password)
    user.password = hashed_password

    db.commit()
    db.refresh(user)

    logger.info(f"Password updated successfully for user_id: {user.user_id}")

    return {"message": "Password updated successfully"}


