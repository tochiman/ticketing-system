from fastapi import APIRouter, Depends

from database import get_async_db

from models import customer as models_customer
from models import order as models_order
from crud import customer, order, payment, item, org

from lib.auth import customer_login, customer_logout, get_current_customer

import logging #login情報のための追加(デバック用)

router = APIRouter(tags=["customer"])

@router.post("/add_customer")
async def add_customer(add_customer_request: models_customer.AddCustomerRequest, db = Depends(get_async_db)) -> models_customer.AddCustomerResponse:
    name = add_customer_request.name
    email = add_customer_request.email
    password = add_customer_request.password
    points = 0
    return await customer.add_customer(db, name, email, password, points)

@router.post("/edit_customer")
async def edit_customer(edit_customer_request: models_customer.EditCustomerRequest, db = Depends(get_async_db), current_customer = Depends(get_current_customer)) -> models_customer.EditCustomerResponse:
    id = current_customer.customer_id
    name = edit_customer_request.name
    email = edit_customer_request.email
    password = edit_customer_request.password
    points = edit_customer_request.points
    return await customer.edit_customer(id, db, name, email, password, points)

@router.post("/add_order")
async def add_order(add_order_request: models_order.AddOrderRequest, db = Depends(get_async_db), current_customer = Depends(get_current_customer)):
    customer_id = current_customer.customer_id
    store_id = add_order_request.storeId
    ordered = await order.add_order(db, customer_id, store_id)
    order_id = ordered.order_id
    items = add_order_request.itemList
    total = 0
    for ordered_item in items:
        item_id = ordered_item.id
        item_info = await item.get_item(db,item_id)
        number_of_purchase = ordered_item.numberOfPurchase
        total += item_info.price * number_of_purchase
        await order.add_order_detail(order_id, item_id, number_of_purchase)
    await payment.add_payment(db, order_id, total)
    id = current_customer.customer_id
    name = current_customer.name
    email = current_customer.email
    password = current_customer.password
    points = current_customer.points
    current_points = points - total
    return await customer.edit_customer(id,db,name,email,password,current_points)

@router.get("/get_all_store")
async def get_all_store(db = Depends(get_async_db)):
    return await org.get_stores(db)

@router.get("/get_items")
async def get_items(store_id, db = Depends(get_async_db)):
    return await item.get_available(db,store_id)

@router.post("/login")
async def login_customer(_ =  Depends(customer_login)):
    return

@router.post("/logout")
async def logout_customer(_ = Depends(customer_logout)):
    return

@router.post("/delete_customer")
async def delete_customer(db = Depends(get_async_db), current_customer = Depends(get_current_customer)):
    logger = logging.getLogger("delete_customer")
    logger.warning(f"Current customer: {current_customer}")  # ログにcurrent_customerを出力

    id = current_customer.customer_id
    return await customer.delete_customer(id, db)

# ログイン済みのユーザのみアクセス可能
@router.post("/me")
async def me(current_customer = Depends(get_current_customer)):
    return current_customer


