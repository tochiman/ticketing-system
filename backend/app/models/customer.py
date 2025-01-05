from datetime import datetime
from typing import List

from pydantic import Field, EmailStr, BaseModel

from models.base import BaseSchema

class AddCustomerRequest(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    password: str


class AddCustomerResponse(BaseSchema):
    name: str
    email: EmailStr

class EditCustomerRequest(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    password: str

class EditCustomerResponse(BaseSchema):
    name: str
    email: EmailStr

class AddAllergyRequest(BaseSchema):
    allergies: List[int]

class OrderDetailResponse(BaseModel):
    order_detail_id: str
    item_id: str
    number_of_purchase: int

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    order_id: str
    status: int
    order_details: List[OrderDetailResponse]

    class Config:
        orm_mode = True

class OrderListResponse(BaseModel):
    orders: List[OrderResponse]

    class Config:
        orm_mode = True