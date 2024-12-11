from fastapi import APIRouter, Depends

from database import get_async_db

from models import org as models_org
from crud import org

from lib.auth import organization_login, get_current_organization, organization_logout

router = APIRouter()


# テンプレートのため要確認
@router.post("/add_org")
async def add_org(add_org_request: models_org.AddOrgRequest, db = Depends(get_async_db)) -> models_org.AddOrgResponse:
    name = add_org_request.name
    email = add_org_request.email
    password = add_org_request.password
    phone = add_org_request.phone
    return await org.add_org(db=db, name=name, email=email, phone=phone, password=password)


@router.post("/login")
async def login_org(_ =  Depends(organization_login)):
    return


@router.post("/add_store")
async def add_store(add_store_request: models_org.AddStoreRequest, db = Depends(get_async_db), current_org = Depends(get_current_organization)) -> models_org.AddStoreResponse:
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

@router.get("/me")
async def me(current_org = Depends(organization_login)):
    return current_org

@router.post("/logout")
async def logout_org(_ = Depends(organization_logout)):
    return

@router.get("/store-list")
async def store_list(current_org = Depends(organization_login)):
    return current_org.stores