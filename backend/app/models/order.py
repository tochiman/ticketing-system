from datetime import datetime

from pydantic import Field, EmailStr

from models.base import BaseSchema

class AddOrderRequest(BaseSchema):
    customerId: str

class AddOrderResponce(BaseSchema):
    None