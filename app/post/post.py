from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.post import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from fastapi.security import OAuth2PasswordRequestForm
from app.post.service import get_all_posts_service,add_new_post_service,remove_post_service,update_post_service
import logging

logger = logging.getLogger(__name__)

router= APIRouter(
    prefix="/post",
    tags= ['posts']
)

air = FastAPI()

models.Base.metadata.create_all(bind=engine)


# getting users details   
@router.get("/get_all")
def get_all_posts(db:Session = Depends (get_db)):
                  #current_user :int = Depends(oauth2.get_current_user)):
    
    logger.info(f" trying to fetching all users")
    

    return get_all_posts_service(db) 



# user registretion 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.post_response)
def add_new_post(post: schemas.post_request, db: Session = Depends(get_db),
                current_user = Depends(oauth2.get_current_user)):
    
    logger.info(f"User {current_user.user_id} trying to upload {post}")

    return add_new_post_service(post,db,current_user)



        
@router.delete("/remove/{id}")
def remove_post(id: str,db:Session = Depends (get_db),
                current_user = Depends(oauth2.get_current_user)):
    
    logger.info(f"User {current_user.user_id} trying to delete post")
    return remove_post_service(id,db,current_user)


@router.put("/update/{id}", response_model=schemas.post_response)
def update_post(
    id: int,
    post : schemas.post_request,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    logger.info(f"User {current_user.user_id} trying to update {post}")
    return update_post_service(id,post,db,current_user)