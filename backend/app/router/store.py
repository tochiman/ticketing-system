from fastapi import APIRouter, Depends

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