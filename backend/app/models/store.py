from pydantic import BaseModel
from datetime import datetime
from typing import List

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
