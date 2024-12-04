import secrets
from datetime import datetime, timedelta, timezone, date

from fastapi import Cookie, Depends, HTTPException, Response, status
from sqlalchemy.sql import select, delete
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from uuid import UUID

from database import get_async_db

from crud import models

ACCESS_TOKEN_EXPIRE_MINUTES = 60 # access_tokenの有効期限
SESSION_ID_LENGTH = 64 # セッションIDの長さ

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Customer(BaseModel):
    customer_id: UUID
    name: str
    email: EmailStr
    date_of_birth: date
    points: int


class Organization(BaseModel):
    organization_id: UUID
    name: str
    email: EmailStr


class Store(BaseModel):
    store_id: UUID
    organization_id: UUID
    name: str
    email: EmailStr
    address: str
    latitude: str
    longitude: str
    open_time: datetime
    close_time: datetime


async def get_user_by_email(db, email, user_type):
    if user_type == 1:
        stmt = select(models.Customer).where(models.Customer.email == email)
        user = (await db.execute(stmt)).scalars().first()
        return (user.customer_id, user.password)
    elif user_type == 2:
        stmt = select(models.Organization).where(models.Organization.email == email)
        user = (await db.execute(stmt)).scalars().first()
        return (user.organization_id, user.password)
    elif user_type == 3:
        stmt = select(models.Store).where(models.Store.email == email)
        user = (await db.execute(stmt)).scalars().first()
        return (user.store_id, user.password)
    return None


async def get_user_by_id(db, id, user_type):
    if user_type == 1:
        stmt = select(models.Customer).where(models.Customer.customer_id == id)
        user = (await db.execute(stmt)).scalars().first()
        return Customer.model_validate(user, from_attributes=True)
    elif user_type == 2:
        stmt = select(models.Organization).where(models.Organization.organization_id == id)
        user = (await db.execute(stmt)).scalars().first()
        return Organization.model_validate(user, from_attributes=True)
    elif user_type == 3:
        stmt = select(models.Store).where(models.Store.store_id == id)
        user = (await db.execute(stmt)).scalars().first()
        return Organization.model_validate(user, from_attributes=True)
    return None


async def not_exist_session_id(db, session_id):
    stmt = select(models.Session).where(models.Session.session_id == session_id)
    session = (await db.execute(stmt)).scalars().first()
    if not session:
        return True
    return False


async def get_user_id(db, session_id, user_type):
    stmt = select(models.Session).where(models.Session.session_id == session_id, models.Session.user_type == user_type)
    session = (await db.execute(stmt)).scalars().first()
    return session.user_id


async def set_session_id(db, session_id, user_id, user_type):
    session = models.Session(session_id=session_id, user_id=user_id, user_type=user_type)
    db.add(session)
    await db.flush()
    await db.refresh(session)
    return session


async def authenticate_user(db, email: str, password: str, user_type):
    user = await get_user_by_email(db, email, user_type)
    if not user:
        return False
    if not password == user[1]:
        return False
    return user[0]


async def create_session_id(db) -> str:
    while True:
        session_id = secrets.token_hex(SESSION_ID_LENGTH)
        if await not_exist_session_id(db, session_id):
            return session_id

async def delete_session(db, session_id, user_type):
    from logging import getLogger, StreamHandler
    stmt = delete(models.Session).where(models.Session.session_id == session_id, models.Session.user_type == user_type)
    await db.execute(stmt)
    return

class LoginData(BaseModel):
    email: EmailStr
    password: str


class Login:
    def __init__(self, user_type):
        self.user_type = user_type


    async def __call__(self, login_data: LoginData, response: Response, db = Depends(get_async_db)):
        user_id = await authenticate_user(
            db, login_data.email, login_data.password, self.user_type
        )
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        session_id = await create_session_id(db)
        await set_session_id(db, session_id, user_id, self.user_type)
        expires = datetime.now(tz=timezone.utc) + \
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        response.set_cookie(
            key="session_id",
            value=session_id,
            expires=expires,
            httponly=True
        )


class GetCurrentUser:
    def __init__(self, user_type):
        self.user_type = user_type


    async def __call__(self, db = Depends(get_async_db), session_id: str = Cookie(None)):
        if not session_id or await not_exist_session_id(db, session_id):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_id = await get_user_id(db, session_id, self.user_type)
        user = await get_user_by_id(db, user_id, self.user_type)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user


class Logout:
    def __init__(self, user_type):
        self.user_type = user_type


    async def __call__(self, response: Response, db = Depends(get_async_db), session_id: str = Cookie(None)):
        if not session_id or await not_exist_session_id(db, session_id):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        await delete_session(db, session_id, self.user_type)
        response.delete_cookie(
            key="session_id"
        )


# Customer
customer_login = Login(1)
get_current_customer = GetCurrentUser(1)
customer_logout = Logout(1)

# Organization
organization_login = Login(2)
get_current_organization = GetCurrentUser(2)
organization_logout = Logout(2)

# Store
store_login = Login(3)
get_current_store = GetCurrentUser(3)
store_logout = Logout(3)