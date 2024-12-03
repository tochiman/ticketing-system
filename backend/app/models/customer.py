from datetime import datetime

from pydantic import Field, EmailStr

from models.base import BaseSchema

class AddCustomerRequest(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    password: str


class AddCustomerResponse(BaseSchema):
    name: str
    email: EmailStr
