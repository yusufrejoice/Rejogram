from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from typing import Optional



# schema for likes

class follow_request(BaseModel):
    follower_id : int
    following_id : int
    
    









