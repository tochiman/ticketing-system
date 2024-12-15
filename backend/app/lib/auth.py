import secrets
from datetime import datetime, timedelta, timezone, date

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

from fastapi import Cookie, Depends, HTTPException, Response, status, BackgroundTasks
from sqlalchemy.sql import select, delete
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from uuid import UUID

from env import GMAIL_ADDRESS,GMAIL_APP_PASSWORD,HOST

from database import get_async_db

from crud import models

RESET_TOKEN_EXPIRE_MINUTES = 30
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
    stmt = delete(models.Session).where(models.Session.session_id == session_id, models.Session.user_type == user_type)
    await db.execute(stmt)
    return


async def set_reset_password(db, email, expire, token):
    obj = await get_reset_password_by_email(db, email)
    if obj:
        obj.token = token
        obj.expire = expire
    else:
        obj = models.ResetPassword(email=email, token=token, expire=expire)
        db.add(obj)
    await db.flush()
    await db.refresh(obj)
    return obj


async def get_reset_password_by_email(db, email):
    stmt = select(models.ResetPassword).where(models.ResetPassword.email == email)
    obj = (await db.execute(stmt)).scalars().first()
    return obj


async def get_reset_password_by_token(db, token):
    stmt = select(models.ResetPassword).where(models.ResetPassword.token == token)
    obj = (await db.execute(stmt)).scalars().first()
    return obj


async def delete_reset_password(db, token):
    stmt = delete(models.ResetPassword).where(models.ResetPassword.token == token)
    await db.execute(stmt)
    return


async def delete_expired_records(db):
    current_time = datetime.now()
    stmt = delete(models.ResetPassword).where(models.ResetPassword.expire < current_time)
    await db.execute(stmt)
    return


async def create_password_reset_token(db, email):
    expire = datetime.utcnow() + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    token_data = {
        "exp": expire,
        "sub": email,
    }
    hashed = pwd_context.hash(str(token_data))
    await set_reset_password(db, email, expire, hashed)
    return hashed


def get_user_type(user_type):
    if user_type == 1:
        return "customer"
    elif user_type == 2:
        return "org"
    elif user_type == 3:
        return "store"
    return None

def send_reset_email(email: str, reset_token: str, user_type):
    message = MIMEMultipart()
    message["From"] = GMAIL_ADDRESS
    message["To"] = email
    message["Subject"] = "パスワードリセットのご案内"
    reset_url = f"{HOST}/{get_user_type(user_type)}/reset-password?token={reset_token}".replace("//", "/")
    with open('lib/email.html', 'r', encoding="utf-8") as f:
        html = f.read().replace("{{reset_url}}", reset_url)
    message.attach(MIMEText(html, "html"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(message)
    return


async def update_password(db, email, password, user_type):
    if user_type == 1:
        stmt = select(models.Customer).where(models.Customer.email == email)
        user = (await db.execute(stmt)).scalars().first()
        user.password = password
        await db.flush()
        await db.refresh(user)
        return user
    elif user_type == 2:
        stmt = select(models.Organization).where(models.Organization.email == email)
        user = (await db.execute(stmt)).scalars().first()
        user.password = password
        await db.flush()
        await db.refresh(user)
        return user
    return None


class ForgetPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    password: str
    token: str


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


class ForgetPassword:
    def __init__(self, user_type):
        self.user_type = user_type


    async def __call__(self, fpr: ForgetPasswordRequest, background_tasks: BackgroundTasks, db = Depends(get_async_db)):
        email = fpr.email
        user = await get_user_by_email(db, email, self.user_type)
        if user:
            reset_token = await create_password_reset_token(db, email)
            url_safe_reset_token = base64.urlsafe_b64encode(reset_token.encode()).decode('utf-8').replace('=', '')
            background_tasks.add_task(send_reset_email, email, url_safe_reset_token, self.user_type)
        return


class ResetPassword:
    def __init__(self, user_type):
        self.user_type = user_type


    async def __call__(self, rpr: ResetPasswordRequest, db = Depends(get_async_db)):
        await delete_expired_records(db)
        padding = 4 - (len(rpr.token) % 4)
        url_safe_token = rpr.token + ("=" * padding)
        token = base64.urlsafe_b64decode(url_safe_token).decode('utf-8')
        try:
            obj = await get_reset_password_by_token(db, token)
            if not obj:
                raise
            await delete_reset_password(db, token)
            if obj.email == rpr.email:
                await update_password(db, obj.email, rpr.password, self.user_type)
                return
        except:
            pass
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired reset token"
        )


# Customer
customer_login = Login(1)
get_current_customer = GetCurrentUser(1)
customer_logout = Logout(1)
customer_froget_password = ForgetPassword(1)
customer_reset_password = ResetPassword(1)

# Organization
organization_login = Login(2)
get_current_organization = GetCurrentUser(2)
organization_logout = Logout(2)
organization_froget_password = ForgetPassword(2)
organization_reset_password = ResetPassword(2)

# Store
store_login = Login(3)
get_current_store = GetCurrentUser(3)
store_logout = Logout(3)
