from typing import List, Dict
from models.base import BaseSchema

class AddOrderRequest(BaseSchema):
    storeId: str
    itemList: List[Dict['id': str, 'numberOfPurchase': int]]

class AddOrderResponce(BaseSchema):
    None