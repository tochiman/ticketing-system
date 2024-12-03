from crud import models
from sqlalchemy.sql import select
from lib import auth

async def add_customer(db, name, email, password, points):
    db_obj = models.Customer(name=name, email=email, password=password, points=points)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def edit_customer(db, name, email, password, points):
    current_customer = auth.get_current_customer
    id = current_customer.id
    db_obj = auth.get_user_by_id(db,id,1)
    db_obj.name = name
    db_obj.email = email
    db_obj.password = password
    db_obj.points = points
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def delete_customer(id):
    """ 清宮頼んだ """
    return 