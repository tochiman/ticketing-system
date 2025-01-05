from http.client import HTTPException
from crud import models, item
from sqlalchemy.sql import select
from sqlalchemy.orm import selectinload
from lib import auth

from models import Order, OrderDetail, Item, Payment,  Customer

async def add_customer(db, name, email, password, points):
    await exist_email(db, email)
    db_obj = models.Customer(name=name, email=email, password=password, points=points)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def edit_customer(id, db, name, email, password, points):
    db_obj = auth.get_user_by_id(db,id,1)
    db_obj.name = name
    db_obj.email = email
    db_obj.password = password
    db_obj.points = points
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def delete_customer(id,db):
    db_obj = auth.get_user_by_id(db,id,1)
    db_obj.disabled = True
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def exist_email(db, email):
    stmt = select(models.Customer).where(models.Customer.email == email, models.Customer.disabled == False)
    customer = (await db.execute(stmt)).scalars().first()
    if customer:
        raise HTTPException(
            status_code=400,
            detail="This email address is already in use."
        )
    return

async def edit_allergy(db, customer_id, allergy_list):
    stmt = select(models.Customer).where(models.Customer.customer_id == customer_id, models.Item.disabled == False)
    customer = (await db.execute(stmt)).scalars().unique().first()
    for allergy in customer.allergy:
        allergy.customer.remove(customer)
    for id in allergy_list:
        allergy = await item.get_allergy(db, id)
        allergy.customer.append(customer)
    await db.flush()
    await db.refresh(customer, ["allergy"])
    return customer

async def get_order_list(customer_id,db):
    query = (
        select(Order)
        .join(OrderDetail)
        .join(Item)
        .join(Customer)
        .join(Payment)
        .where(Customer.customer_id == customer_id)
        .options(selectinload(Order.order_details).joinedload(OrderDetail.item))
    )
    result = await db.execute(query)
    db_obj = result.scalars().all()
    return db_obj
