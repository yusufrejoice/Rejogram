from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.comment import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.comment.service import  get_all_comments_service , add_new_comments_service , get_via_id_service ,remove_cmt_service ,update_cmt_service

router= APIRouter(
    prefix="/comment",
    tags= ['comments']
)

air = FastAPI()


# getting all commants   
@router.get("/get_all")
def get_all_commants(db:Session = Depends (get_db)):
    

    return get_all_comments_service(db) 



# add commants 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.cmt_response)
def add_new_comments(cmt: schemas.cmt_request, db: Session = Depends(get_db)):


    return add_new_comments_service(cmt,db)

#getting commants details via id         
@router.get("/get/{id}",response_model=schemas.cmt_response)
def get_cmt(id : str ,db:Session = Depends (get_db)):

    
    return get_via_id_service(id,db)




# removing comment via id         
@router.delete("/remove/{id}")
def remove_cmt(id: str,db:Session = Depends (get_db)):
    

    return remove_cmt_service(id,db)


@router.put("/update/{id}", response_model=schemas.cmt_response)
def update_cmt(
    id: int,
    passanger: schemas.cmt_request,
    db: Session = Depends(get_db)
):
    
    return update_cmt_service(id,passanger,db)