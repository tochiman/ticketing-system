from crud import models

async def add_customer(db, name, email, password, points):
    db_obj = models.Customer(name=name, email=email, password=password, points=points)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj
