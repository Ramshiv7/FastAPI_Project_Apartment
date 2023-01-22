from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import connect_db
from .. import models
from .. import utils
from .. import schemas

router = APIRouter(
    prefix='/login',
    tags = ['Authentication']
)


@router.post('/')
async def validate_user(login_details: schemas.AuthLogin, db: Session = Depends(connect_db)):
    # validate the user email with Database 
    user_verify = db.query(models.User).filter(models.User.email == login_details.email).first()
    hashed_password = user_verify.password

    # Get the Plain pass from API, & Hashed Password from Database
    plain_password = login_details.password 

    if not utils.verify_pass(plain_password, hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

    return "Password Matches - Congrats"
    # if Password Matches, Then Generate a Token 
