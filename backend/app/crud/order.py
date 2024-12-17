from crud import models
from sqlalchemy.sql import select

async def add_order(db, customer_id):
    db_obj = models.Order(customer_id)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def add_order_detail(db, order_id, item_id, number_of_purchase):
    db_obj = models.OrderDetail(order_id,item_id,number_of_purchase)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj
