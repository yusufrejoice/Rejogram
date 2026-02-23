from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from app.auth import schemas
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.service import login_user_service, add_new_user_service ,forget_password_service

rejo=FastAPI()
router= APIRouter(
    prefix="/auth",
    tags= ['authentication']
)

# user singin

@router.post('/singin') 
def login_user(user_credentials:OAuth2PasswordRequestForm = Depends() , db:Session = Depends (get_db)) :
   
   return login_user_service(user_credentials, db)



# user singup

@router.post("/singup", status_code=status.HTTP_201_CREATED,
          response_model=schemas.users_response)
def create_user(user: schemas.user_request, db: Session = Depends(get_db),
                ) :


    return add_new_user_service(user,db)



# forget password  
      
@router.put("/forget/{username}")
def update_user(username: str, password_data : schemas.forget_password , db: Session = Depends (get_db)):
    
    return f"password was updated ",forget_password_service(username,password_data.new_password,db)