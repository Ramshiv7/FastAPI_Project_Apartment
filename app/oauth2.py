from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status

# JWT import 
from jose import JWTError, jwt

# Oauth2 
from fastapi.security.oauth2 import OAuth2PasswordBearer

# OAuth2 Bearer - This is for Get_Current_User func. - it ties everything together

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Secret Key
# Algorithm 
# Expiration Time 

SECRET_KEY = '0xc33c3e923bcf7ee9d67fc9c4b860ab9e824898642452d8e074a65df90'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_TIME = 30


# Generate a Token 
def create_access_token(data: dict): # input is Email & Password from API
    to_encode = data.copy()
    """
    to_encode = {"user_id": id,
    "exp" : 30,
     }

    """

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    to_encode.update({'exp': expire})
    print(to_encode)

    # Encode & Generate a Token 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)

    return encoded_jwt


# Verify the Token 

def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
        print(f'token data : {token_data}')

    except JWTError : 
        raise credentials_exception

    return token_data

# Verify Current User - Called from post Method of the Owner.py
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Bad Cred',
    headers={"WWW-Authenticate": "Bearer"})
    print(f'token from get_current_user: {token}\n\n')
    print(f'credentials_exception:{credentials_exception}')

    return verify_access_token(token, credentials_exception)