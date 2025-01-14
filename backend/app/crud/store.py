import hashlib
import os
from models import Order, OrderDetail, Item, Store
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from crud import models
from sqlalchemy.ext.asyncio import AsyncSession

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

# ステータス更新 (0->1, 1->2, x->4)
async def status(db: AsyncSession, order_id: str, new_status: int, store_id: str):
    async with db.begin():
        # オーダー情報を取得
        stmt = select(Order).where(Order.order_id == order_id, Order.store_id == store_id)
        result = await db.execute(stmt)
        order = result.scalar_one_or_none()

        if not order:
            return None

        # ステータス変更のチェック
        if new_status == 4 or (order.status == 0 and new_status == 1) or (order.status == 1 and new_status == 2):
            order.status = new_status
            db.add(order)
            await db.commit()
            return {"order_id": order.order_id, "status": order.status}
        return None

# ステータス更新 (2 -> 3)
async def update_status(db: AsyncSession, order_id: str, qr_hash: str, store_id: str):
    async with db.begin():
        # オーダー情報を取得
        stmt = select(Order).where(Order.order_id == order_id, Order.store_id == store_id)
        result = await db.execute(stmt)
        order = result.scalar_one_or_none()

        if not order:
            return None
        
        # ハッシュの検証
        sha_256 = hashlib.pbkdf2_hmac('sha256', order_id.encode(), SALT.encode(), 10000).hex()
        if qr_hash != sha_256:
            return None

        # 2 -> 3 へのステータス変更
        if order.status == 2:
            order.status = 3
            db.add(order)
            await db.commit()
            return {"order_id": order.order_id, "status": order.status}
        return None