from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from typing import Optional



class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    id : Optional[str] = None