from fastapi import APIRouter, Depends # type: ignore

import hashlib
from env import SALT
import io
from starlette.responses import StreamingResponse
import qrcode

from database import get_async_db

from models import customer as models_customer
from models import order as models_order
from crud import customer, order, payment, item, org

from lib.auth import customer_login, customer_logout, get_current_customer

import logging #login情報のための追加(デバック用)

router = APIRouter(tags=["customer"])

""" customerレコード追加 """
@router.post("/add_customer")
async def add_customer(add_customer_request: models_customer.AddCustomerRequest, db = Depends(get_async_db)) -> models_customer.AddCustomerResponse:
    name = add_customer_request.name
    email = add_customer_request.email
    password = add_customer_request.password
    points = 0
    return await customer.add_customer(db, name, email, password, points)

""" アカウント認証 """
@router.post("/login")
async def login_customer(_ =  Depends(customer_login)):
    return

""" ログアウト """
@router.post("/logout")
async def logout_customer(_ = Depends(customer_logout)):
    return

""" customerのpoints取得 """
@router.post("/get_isServed")
async def get_isServed(current_customer = Depends(get_current_customer)):
    return current_customer.points

""" ログイン中ユーザのユーザデータ取得 """
@router.get("/me")
async def me(current_customer = Depends(get_current_customer)):
    return current_customer

""" ログイン中ユーザのユーザデータ編集 """
@router.post("/edit_customer")
async def edit_customer(edit_customer_request: models_customer.EditCustomerRequest, db = Depends(get_async_db), current_customer = Depends(get_current_customer)) -> models_customer.EditCustomerResponse:
    id = current_customer.customer_id
    name = edit_customer_request.name
    email = edit_customer_request.email
    password = edit_customer_request.password
    points = current_customer.points
    return await customer.edit_customer(id, db, name, email, password, points)

""" ログイン中ユーザの削除 """
@router.post("/delete_customer")
async def delete_customer(db = Depends(get_async_db), current_customer = Depends(get_current_customer)):
    logger = logging.getLogger("delete_customer")
    logger.warning(f"Current customer: {current_customer}")  # ログにcurrent_customerを出力

    id = current_customer.customer_id
    return await customer.delete_customer(id, db)

""" customer_to_allergyレコード追加 """
@router.post("/edit_allergy")
async def edit_allergy(add_allergy_request:models_customer.AddAllergyRequest, db = Depends(get_async_db), current_customer = Depends(get_current_customer)):
    customer_id = current_customer.customer_id
    allergy_list = add_allergy_request.allergies
    return await customer.edit_allergy(db, customer_id, allergy_list)

"""
注文履歴の取得
・orderレコード取得
・order_idからpaymentデータ取得
・order_idからorder_detailデータ取得
"""
@router.get("/get_order")
async def get_order(db = Depends(get_async_db), current_cutomer = Depends(get_current_customer)):
    customer_id = current_cutomer.customer_id
    orders = await customer.get_orders_by_store(db, customer_id)
    return models_customer.OrderListResponse(orders=orders)

""" 
オーダー
・orderレコード追加
・order_detailレコード追加
・paymentレコード追加
・pointsの変更
"""
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
    points = current_customer.points - total
    return await customer.edit_customer(id,db,name,email,password,points)

""" point増加(定数) """
@router.post("/add_100p")
async def add_100p(db= Depends(get_async_db),current_customer = Depends(get_current_customer)):
    id = current_customer.customer_id
    name = current_customer.name
    email = current_customer.email
    password = current_customer.password
    points = current_customer.points + 100
    return await customer.edit_customer(id,db,name,email,password,points)

""" point増加(可変) """
@router.post("/add_points")
async def add_100p(point,db= Depends(get_async_db),current_customer = Depends(get_current_customer)):
    id = current_customer.customer_id
    name = current_customer.name
    email = current_customer.email
    password = current_customer.password
    points = current_customer.points + point
    return await customer.edit_customer(id,db,name,email,password,points)

""" storeレコード全取得 """
@router.get("/get_all_store")
async def get_all_store(db = Depends(get_async_db)):
    return await org.get_stores(db)

""" store_idからitemレコード取得 """
@router.get("/get_items")
async def get_items(store_id, db = Depends(get_async_db)):
    return await item.get_available(db,store_id)

""" QRコード生成時の文字列取得 """
@router.get("/get_qr/{order_id}")
async def get_qr(order_id):
    sha_256 = hashlib.pbkdf2_hmac('sha256', order_id.encode(), SALT, 10000).hex()
    qr_src = str(order_id) + ':' + sha_256
    img = qrcode.make(qr_src)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
