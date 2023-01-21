from pydantic import BaseModel 
from typing import Optional 
from datetime import datetime


class OwnerBase(BaseModel):
    name : str 
    age : int 
    gender : str
    paid_maintenance : bool = False


    class Config:
        orm_mode = True 


class NewOwner(OwnerBase):
    pass

class UpdateOwner(OwnerBase):
    name : str
    age : int 

class OwnerReturn(BaseModel):
    name : str
    age : int
    gender : str

    class Config:
        orm_mode = True