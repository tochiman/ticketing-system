from http.client import HTTPException
from crud import models
from sqlalchemy.sql import select
from lib import auth

async def add_customer(db, name, email, password, points):
    await exist_email(db, email)
    db_obj = models.Customer(name=name, email=email, password=password, points=points)
    db.add(db_obj)
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def edit_customer(id, db, name, email, password, points):
    db_obj = auth.get_user_by_id(db,id,1)
    db_obj.name = name
    db_obj.email = email
    db_obj.password = password
    db_obj.points = points
    await db.flush()
    await db.refresh(db_obj)
    return db_obj

async def delete_customer(id,db):
    db_obj = auth.get_user_by_id(db,id,1)
    if db_obj is None:
        raise ValueError("User not found")  # ユーザーが見つからない場合のエラー処理
    #データベースから削除
    await db.delete(db_obj)
    await db.flush()
    return db_obj

async def exist_email(db, email):
    stmt = select(models.Customer).where(models.Customer.email == email, models.Customer.disabled == False)
    customer = (await db.execute(stmt)).scalars().first()
    if customer:
        raise HTTPException(
            status_code=400,
            detail="This email address is already in use."
        )
    return
