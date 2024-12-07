from fastapi import APIRouter, Depends

from database import get_async_db

from models import customer as models_customer
from crud import customer

from lib.auth import customer_login, customer_logout, get_current_customer

router = APIRouter()

""" customerレコード追加(新規登録) """
# テンプレートのため要確認
@router.post("/add_customer")
async def add_customer(add_customer_request: models_customer.AddCustomerRequest, db = Depends(get_async_db)) -> models_customer.AddCustomerResponse:
    name = add_customer_request.name
    email = add_customer_request.email
    password = add_customer_request.password
    points = 0
    return await customer.add_customer(db, name, email, password, points)

""" ログイン中ユーザ(customer)のdata取得 (name, email, password) """
@router.get("/show_customer")
async def show_customer(current_customer = Depends(get_current_customer)):
    name = current_customer.name
    email = current_customer.email
    password = current_customer.password
    points = current_customer.point
    return {name: name, email:email, password:password, points: points}

""" ログイン中ユーザ(customer)のdata編集 (name, email, password) """
@router.post("/edit_customer")
async def edit_customer(edit_customer_request: models_customer.EditCustomerRequest, db = Depends(get_async_db), current_customer = Depends(get_current_customer)) -> models_customer.EditCustomerResponse:
    id = current_customer.id
    name = edit_customer_request.name
    email = edit_customer_request.email
    password = edit_customer_request.password
    points = edit_customer_request.points
    return await customer.edit_customer(id, db, name, email, password, points)

""" ログイン中ユーザ(customer)の削除 """
# 任せたぜ清宮



""" ログイン """
@router.post("/login")
async def login_customer(_ =  Depends(customer_login)):
    return

""" ログアウト """
@router.post("/logout")
async def logout_customer(_ = Depends(customer_logout)):
    return

# ログイン済みのユーザのみアクセス可能
# @router.post("/me")
# async def me(current_customer = Depends(get_current_customer)):
#     return current_customer
