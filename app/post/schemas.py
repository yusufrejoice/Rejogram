from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from typing import Optional



# schema for post

class post_request(BaseModel):
    tital: str
    contant: str
    published: bool
    
    

class post_response(BaseModel):
    tital : str
    contant : str
    published : bool
    created_at : datetime
    owner_id : int
    
    

    class confing:
        orm_mode=True







