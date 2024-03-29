from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import connect_db
from .. import models
from .. import utils
from .. import schemas
from .. import oauth2


router = APIRouter(
    prefix='/login',
    tags = ['Authentication']
)


@router.post('/')
# async def validate_user(login_details: schemas.AuthLogin, db: Session = Depends(connect_db)):
async def validate_user(login_details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(connect_db)):
    # validate the user email with Database 
    user_verify = db.query(models.User).filter(models.User.email == login_details.username).first()
    hashed_password = user_verify.password

    # Get the Plain pass from API, & Hashed Password from Database
    plain_password = login_details.password 

    if not utils.verify_pass(plain_password, hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

    #return "Password Matches - Congrats"

    # if Password Matches, Then Generate a Token - JWT Token - Json Web Token  
    access_token = oauth2.create_access_token(data = {"user_id": user_verify.id }) # Need to Verify ID 
    #print(f"Access Token : {access_token}")
    return {"Access Token": access_token, "token_type": "bearer"}
    

