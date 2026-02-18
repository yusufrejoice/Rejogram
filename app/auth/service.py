from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from app.auth import models,schemas 
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2 
from app.database import engine , SessionLocal


# singin account

def login_user_service(user_credentials, db: Session):
        
        user = db.query(models.singup_model).filter(models.singup_model.email == user_credentials.email).first()
        if not user :
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail=f"invalid credentials" )
    
        if not utils.verify(user_credentials.password,user.password):
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND , 
                detail=f"invalid credentials"
                )
    
        access_token = oauth2.create_access_token(data={"user_id": str(user.id)})

        return {"access token" : access_token , "token type ": "bearer"}



# singup account

def add_new_user_service(user,db):

    user_data = user.dict()
    
    user_data["password"] = pwd_context.hash(user.password)

    

    new_users = models.singup_model(**user_data)

    db.add(new_users)
    db.commit()
    db.refresh(new_users)

    return new_users


# forget password

def forget_password_service(username:str , new_password : str , db : Session ):

    

    user = db.query(models.singup_model).filter(
        models.singup_model.username == username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    hashed_password = pwd_context.hash(new_password)

    user.password = hashed_password
    db.commit()
    db.refresh(user)

    return {"message": "Password updated successful"}


