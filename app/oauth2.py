from  jose import JWTError , jwt
from datetime import datetime , timedelta   
from . import o2_schemas
from fastapi import status,HTTPException , Depends 
from fastapi.security import OAuth2PasswordBearer
from app.utils import get_db
from sqlalchemy.orm import Session
from app.user import models
from app.user import models as user_models
from sqlalchemy.orm import Session
from app.utils import get_db
from app.core.config import settings
oauth2_schemas = OAuth2PasswordBearer(tokenUrl='singin')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES



def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta( minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt 


def verify_access_token(token: str , credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None :
            raise credentials_exception
        token_data = o2_schemas.TokenData(user_id = id)

    except JWTError :
        raise credentials_exception
    
    return token_data 





def get_current_user(
    token: str = Depends(oauth2_schemas),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_access_token(token, credentials_exception)

    db_user = db.query(user_models.User).filter(
        user_models.User.user_id == token_data.user_id
    ).first()

    if db_user is None:
        raise credentials_exception

    return db_user
