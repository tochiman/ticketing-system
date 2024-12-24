import secrets
from datetime import datetime, timedelta, timezone, date

from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.sql import select
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from uuid import UUID

from database import get_async_db

from crud import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Customer(BaseModel):
    customer_id: UUID
    name: str
    email: EmailStr
    date_of_birth: date
    points: int


class Order(BaseModel):
    order_id: UUID
    customer_id:UUID

class OrderDetail(BaseModel):
    order_detail_id: UUID
    order_id: UUID
    item_id: UUID
    number_of_purchase: int

class Payment(BaseModel):
    payment_id: UUID
    order_id: UUID
    total: int
    status: int
    timestamp: datetime

async def get_payments_by_customer_id(db, id):
    stmt = select(models.Payment).where(models.Payment.customer_id == id)
    payment_all = (await db.execute(stmt)).scalars().all()
    return payment_all

async def get_order_by_customer_id(db,id):
    stmt = select(models.Order).where(models.Order.cutomer_id == id)
    order_all = (await db.execute(stmt)).scalars().all()
    return order_all

async def get_order_detail_by_order_id(db,id):
    stmt = select(models.OrderDetail).where(models.OrderDetail.order_id == id)
    order_detail_all = (await db.execute(stmt)).scalars().all()
    return order_detail_all
