from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# use CryptContext to Has the Password 

# Hashing Method = bcrypt 
# Function = HS256

def hash_pass(pwd: str):
    return pwd_context.hash(pwd)

def verify_pass(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)