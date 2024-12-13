from models import Order, OrderDetail, Item, Store
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from crud import models

async def get_order_list(db, store_id):
    query = (
        select(Order)
        .join(OrderDetail)
        .join(Item)
        .join(Store)
        .where(Store.store_id == store_id)
        .options(selectinload(Order.order_details).joinedload(OrderDetail.item))
    )
    result = await db.execute(query)
    db_obj = result.scalars().all()
    return db_obj
