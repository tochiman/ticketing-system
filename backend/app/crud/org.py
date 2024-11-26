from crud import models

async def add_org(db, name, email, password):
    db_obj = models.Organization(name=name, email=email, password=password)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj


async def add_store(db, organization_id, name, email, password, address, open_time, close_time):
    db_obj = models.Store(organization_id=organization_id, name=name, email=email, password=password, address=address, open_time=open_time, close_time=close_time)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj