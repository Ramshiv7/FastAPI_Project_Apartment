from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..database import  connect_db
from .. import models
from .. import schemas
from .. import utils

# Provide API router & Import APIRouter from fastapi
router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/', response_model=schemas.LoginReturn)
def login_details(details: schemas.OwnerLogin, db: Session = Depends(connect_db)):
    # new_data = models.Login(**details.dict()) -- Before Hashing 
    pwd_data = utils.hash_pass(details.password)
    details.password = pwd_data # Hashed Password has been Updated
    new_data = models.User(**details.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data