from sqlalchemy.sql import select

from crud import models

async def add_org(db, name, email, password, phone):
    db_obj = models.Organization(name=name, email=email, password=password, phone=phone)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj


async def add_store(db, organization_id, name, email, password, address, phone, latitude, longitude, open_time, close_time):
    db_obj = models.Store(organization_id=organization_id, name=name, email=email, password=password, address=address, phone=phone, latitude=latitude, longitude=longitude, open_time=open_time, close_time=close_time)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj


async def get_stores_by_org_id(db, organization_id):
    stmt = select(models.Store).where(models.Store.organization_id == organization_id)
    stores = (await db.execute(stmt)).scalars().all()
    return stores


async def get_store_by_store_id(db, store_id):
    stmt = select(models.Store).where(models.Store.store_id == store_id)
    store = (await db.execute(stmt)).scalars().first()
    return store