from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.post import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from fastapi.security import OAuth2PasswordRequestForm
from app.post.service import get_all_posts_service,add_new_post_service,remove_post_service,update_post_service

router= APIRouter(
    prefix="/post",
    tags= ['posts']
)

air = FastAPI()

models.Base.metadata.create_all(bind=engine)


# getting users details   
@router.get("/get_all")
def get_all_posts(db:Session = Depends (get_db),
                  current_user :int = Depends(oauth2.get_current_user)):
    

    return get_all_posts_service(db,current_user) 



# user registretion 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.post_response)
def add_new_post(post: schemas.post_request, db: Session = Depends(get_db),
                current_user = Depends(oauth2.get_current_user)):


    return add_new_post_service(post,db,current_user)

#getting user details via id         
# @router.get("/get/{id}",response_model=schemas.post_response)
# def get_user(id : str,db:Session = Depends (get_db),
#              current_user = Depends(oauth2.get_current_user)):

    
#     return get_via_id_service(id,db)




# removing user via id         
@router.delete("/remove/{id}")
def remove_post(id: str,db:Session = Depends (get_db),
                current_user = Depends(oauth2.get_current_user)):
    

    return remove_post_service(id,db,current_user)


@router.put("/update/{id}", response_model=schemas.post_response)
def update_post(
    id: int,
    post : schemas.post_request,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    
    return update_post_service(id,post,db,current_user)