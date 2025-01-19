from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
HASH = os.getenv("HASH")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "securityhashsss",
        "is_admin": True,
    }
}


class User(BaseModel):
    username: str
    is_admin: bool = False


class Token(BaseModel):
    access_token: str
    token_type: str


def fake_hash_password(password: str):
    return f"{HASH}{password}"


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        print("User not found")
        return False
    if user["hashed_password"] != fake_hash_password(password):
        print("Incorrect password")
        return False
    print("True")
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print("MODULE TOKEN STR 64")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = fake_users_db.get(username)
    if user is None:
        raise credentials_exception
    return User(username=username, is_admin=user["is_admin"])