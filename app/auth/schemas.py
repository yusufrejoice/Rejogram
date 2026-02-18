from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from pydantic import BaseModel,EmailStr
from datetime import date, datetime 
from typing import Optional


# schema for singin 

class Userlogin(BaseModel):
    email : EmailStr
    password : str





# schema for singup

class user_request(BaseModel):
    username : str
    email : EmailStr
    password: str
    date_of_birth : date
    
    

class users_response(BaseModel):
    username : str
    email: EmailStr
    date_of_birth : date
    
    

    class confing:
        orm_mode=True




# schema for forget password

class forget_password(BaseModel):
    
    new_password : str



