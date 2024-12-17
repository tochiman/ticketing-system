import uuid
from fastapi import APIRouter, Depends
from typing import List
from models.store import OrderListResponse
from database import get_async_db
from models import item as models_item
from crud import store, item
from lib.auth import store_login, get_current_store

router = APIRouter(tags=["store"])

@router.post("/login")
async def login_store(_ =  Depends(store_login)):
    return

# ログイン済みのユーザのみアクセス可能
@router.get("/me")
async def me(current_store = Depends(get_current_store)):
    return current_store

@router.get("/orders/{store_id}", response_model=OrderListResponse)
async def get_order_list(store_id: str, db = Depends(get_async_db)):
    # store_idを元にオーダーリストを取得
    orders = await store.get_orders_by_store(db, store_id)
    
    # レスポンスを作成して返す
    return OrderListResponse(orders=orders)

@router.get("/get_items")
async def get_items(db = Depends(get_async_db), current_store = Depends(get_current_store)) -> List[models_item.Item]:
    return await item.get_items(db, current_store.organization_id)


@router.get("/get_item/{item_id}")
async def get_item(item_id: uuid.UUID, db = Depends(get_async_db), _= Depends(get_current_store)) -> models_item.ItemResponse:
    return await item.get_item(db, item_id)
