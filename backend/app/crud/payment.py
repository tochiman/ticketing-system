from crud import models
from sqlalchemy.sql import select

async def add_payment(db, order_id, total):
    db_obj = models.Payment(order_id, total, status=0)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj
