from fastapi import APIRouter, Depends
from typing import List

from database import get_async_db

from models import org as models_org
from models import item as models_item
from crud import org, item
import uuid

from lib.auth import organization_login, get_current_organization, organization_logout, organization_froget_password, organization_reset_password

router = APIRouter(tags=["org"])


@router.post("/add_org", tags=["org-org"])
async def add_org(add_org_request: models_org.OrgRequest, db = Depends(get_async_db)) -> models_org.OrgResponse:
    name = add_org_request.name
    email = add_org_request.email
    password = add_org_request.password
    phone = add_org_request.phone
    return await org.add_org(db=db, name=name, email=email, phone=phone, password=password)


@router.post("/login", tags=["org-org"])
async def login_org(_ =  Depends(organization_login)):
    return


@router.post("/add_store", tags=["org-store"])
async def add_store(add_store_request: models_org.StoreRequest, db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> models_org.StoreResponse:
    name = add_store_request.name
    email = add_store_request.email
    password = add_store_request.password
    address = add_store_request.address
    phone = add_store_request.phone
    latitude = add_store_request.latitude
    longitude = add_store_request.longitude
    open_time = add_store_request.open_time
    close_time = add_store_request.close_time
    organization_id = current_org.organization_id
    return await org.add_store(db=db, organization_id=organization_id, name=name, email=email, password=password, address=address, phone=phone, latitude=latitude, longitude=longitude, open_time=open_time, close_time=close_time)


@router.get("/me", tags=["org-org"])
async def me(current_org = Depends(get_current_organization)):
    return current_org


@router.post("/logout", tags=["org-org"])
async def logout_org(_ = Depends(organization_logout)):
    return


@router.get("/store_list", tags=["org-store"])
async def store_list(db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> List[models_org.Store]:
    stores = await org.get_stores_by_org_id(db, current_org.organization_id)
    return stores


@router.get("/store/{store_id}", tags=["org-store"])
async def store(store_id: uuid.UUID, db = Depends(get_async_db), _ = Depends(get_current_organization)) -> models_org.StoreResponse:
    store = await org.get_store_by_store_id(db, store_id)
    return store


@router.post("/delete_org", tags=["org-store"])
async def delete_org(db = Depends(get_async_db), current_org = Depends(get_current_organization)):
    pass


@router.post("/delete_store/{store_id}", tags=["org-store"])
async def delete_store(store_id: uuid.UUID, db = Depends(get_async_db), current_org = Depends(get_current_organization)):
    pass


@router.post("/edit_org_profile", tags=["org-org"])
async def edit_org_profile(db = Depends(get_async_db), current_org = Depends(get_current_organization)):
    pass


@router.post("/edit_store_profile/{store_id}", tags=["org-store"])
async def edit_store_profile(store_id: uuid.UUID ,db = Depends(get_async_db), current_org = Depends(get_current_organization)):
    pass


@router.post("/add_item", tags=["org-item"])
async def add_item(itemRequest: models_item.ItemRequest, db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> models_item.ItemResponse:
    name = itemRequest.name
    size = itemRequest.size
    price = itemRequest.price
    description = itemRequest.description
    allergy_list = itemRequest.allergy
    organization_id = current_org.organization_id
    obj = await item.add_item(db, name, size, price, description, allergy_list, organization_id)
    return obj


@router.post("/edit_item/{item_id}", tags=["org-item"])
async def edit_item(itemRequest: models_item.ItemRequest, item_id: uuid.UUID, db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> models_item.ItemResponse:
    pass


@router.post("/delete_item/{item_id}", tags=["org-item"])
async def delete_item(item_id: uuid.UUID, db = Depends(get_async_db), current_org = Depends(get_current_organization)):
    pass


@router.get("/get_items", tags=["org-item"])
async def get_items(db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> List[models_item.Item]:
    return await item.get_items(db, current_org.organization_id)


@router.get("/get_item/{item_id}", tags=["org-item"])
async def get_item(item_id: uuid.UUID, db = Depends(get_async_db), _ = Depends(get_current_organization)) -> models_item.ItemResponse:
    return await item.get_item(db, item_id)

@router.post("/forget_password", tags=["org-org"])
async def forget_password(_ = Depends(organization_froget_password)):
    return

@router.post("/reset_password", tags=["org-org"])
async def reset_password(_ = Depends(organization_reset_password)):
    return
