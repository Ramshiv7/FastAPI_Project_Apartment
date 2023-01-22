from datetime import datetime, timedelta

# JWT import 
from jose import JWTError, jwt

# Oauth2 
from fastapi.security.oauth2 import OAuth2PasswordBearer

# OAuth2 Bearer 

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


# Verify Current User 