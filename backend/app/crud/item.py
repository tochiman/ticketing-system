from sqlalchemy.sql import select
from sqlalchemy.orm import joinedload

from crud import models

async def add_item(db, name, size, price, description, allergy_list, organization_id):
    item_obj = models.Item(name=name, size=size, price=price, description=description, organization_id=organization_id)
    for id in allergy_list:
        allergy = await get_allergy(db, id)
        allergy.item.append(item_obj)
    db.add(item_obj)
    await db.flush()
    await db.refresh(item_obj, ["allergy"])
    return item_obj


async def get_allergy(db, id):
    stmt = select(models.Allergy).where(models.Allergy.allergy_id == id).options(joinedload(models.Allergy.item))
    allergy = (await db.execute(stmt)).scalars().unique().first()
    return allergy


async def get_items(db, organization_id):
    stmt = select(models.Item).where(models.Item.organization_id == organization_id)
    item = (await db.execute(stmt)).scalars().all()
    return item


async def get_item(db, item_id, organization_id):
    stmt = select(models.Item).where(models.Item.item_id == item_id, models.Item.organization_id == organization_id).options(joinedload(models.Item.allergy))
    item = (await db.execute(stmt)).scalars().unique().first()
    return item
