import uuid
from typing import List

from models.base import BaseSchema


class ItemRequest(BaseSchema):
    name: str
    size: str
    price: int
    description: str
    allergy: List[int]


class Allergy(BaseSchema):
    name: str


class ItemResponse(ItemRequest):
    allergy: List[Allergy]


class Item(BaseSchema):
    name: str
    item_id: uuid.UUID