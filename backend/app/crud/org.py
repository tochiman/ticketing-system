from fastapi import HTTPException
from sqlalchemy.sql import select

from crud import models

async def add_org(db, name, email, password, phone):
    await exist_email(db, email)
    db_obj = models.Organization(name=name, email=email, password=password, phone=phone, disabled=False)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj


async def add_store(db, organization_id, name, email, password, address, phone, latitude, longitude, open_time, close_time):
    await exist_email(db, email)
    db_obj = models.Store(organization_id=organization_id, name=name, email=email, password=password, address=address, phone=phone, latitude=latitude, longitude=longitude, open_time=open_time, close_time=close_time, disabled=False)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj


async def exist_email(db, email):
    stmt = select(models.Store).where(models.Store.email == email, models.Store.disabled == False)
    store = (await db.execute(stmt)).scalars().first()
    stmt = select(models.Organization).where(models.Organization.email == email, models.Organization.disabled == False)
    org = (await db.execute(stmt)).scalars().first()
    if org or store:
        raise HTTPException(
            status_code=400,
            detail="This email address is already in use."
        )
    return


async def get_stores_by_org_id(db, organization_id):
    stmt = select(models.Store).where(models.Store.organization_id == organization_id, models.Store.disabled == False)
    stores = (await db.execute(stmt)).scalars().all()
    return stores


async def get_store_by_store_id(db, store_id):
    stmt = select(models.Store).where(models.Store.store_id == store_id, models.Store.disabled == False)
    store = (await db.execute(stmt)).scalars().first()
    return store