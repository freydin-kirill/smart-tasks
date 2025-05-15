from typing import Optional
from datetime import timedelta, datetime, UTC

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from common.config import SECRET_KEY, ALGORITHM
from common.database import get_async_session
from common.exeptions import InvalidCredentialsException, InactiveUserException
from src.authentication.app.schemas.token_schema import TokenData
from src.authentication.app.schemas.user_schema import UserBaseInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Hashing password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verifying password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Creating access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=15)
    expire = datetime.now(UTC) + expires_delta
    to_encode.update({"expire": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get user by username
async def get_user(username: str, db: AsyncSession = Depends(get_async_session)) -> UserBaseInDB:
    pass

async def authenticate_user(username: str, password: str, db: AsyncSession = Depends(get_async_session)):
    user = get_user(username, db)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme),
                           db: AsyncSession = Depends(get_async_session)) -> UserBaseInDB:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise InvalidCredentialsException
        token_data = TokenData(username=username)
    except JWTError:
        raise InvalidCredentialsException

    user = get_user(username=token_data.username, db=db)
    if user is None:
        raise InvalidCredentialsException
    return user

async def get_current_active_user(current_user: UserBaseInDB = Depends(get_current_user)) -> UserBaseInDB:
    if current_user.disabled:
        raise InactiveUserException
    return current_user

# Function to get user database
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    pass
