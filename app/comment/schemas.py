from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from typing import Optional



# schema for commants

class cmt_request(BaseModel):
    contant : str
    published : bool
    post_id : int
    
    

class cmt_response(BaseModel):
    contant : str
    published : bool
    created_at : datetime
    post_id : int 
    owner_id : int
    
    

    class confing:
        orm_mode=True


        







