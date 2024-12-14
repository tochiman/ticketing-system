from fastapi import APIRouter, Depends
from typing import List
from crud import store
from models.store import OrderListResponse
from database import get_async_db
from models import org as models_store
from crud import store
from lib.auth import store_login, get_current_store

router = APIRouter()

@router.post("/login")
async def login_store(_ =  Depends(store_login)):
    return

# ログイン済みのユーザのみアクセス可能
@router.post("/me")
async def me(current_store = Depends(get_current_store)):
    return current_store

@router.get("/orders/{store_id}", response_model=OrderListResponse)
async def get_order_list(store_id: str, db = Depends(get_async_db)):
    # store_idを元にオーダーリストを取得
    orders = await store.get_orders_by_store(db, store_id)
    
    # レスポンスを作成して返す
    return OrderListResponse(orders=orders)
