from pydantic import BaseModel, EmailStr
from typing import Optional 
from datetime import datetime



class OwnerBase(BaseModel):
    name : str 
    age : int 
    gender : str
    paid_maintenance : bool = False
    created_at : datetime
    
    class Config:
        orm_mode = True 


class NewOwner(BaseModel):
    name : str 
    age : int 
    gender : str
    paid_maintenance : bool = False

class UpdateOwner(OwnerBase):
    name : str
    age : int 

class OwnerReturn(BaseModel):
    name : str
    age : int
    gender : str

    class Config:
        orm_mode = True


class OwnerLogin(BaseModel):
    email : EmailStr
    password : str 

    class Config: # if Missed -> Error :  value is not a valid dict (type=type_error.dict)
        orm_mode = True


class LoginReturn(OwnerLogin):
    pass


class AuthLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token: str 
    token_type: str 


class TokenData(BaseModel):
    id: Optional[str] = None