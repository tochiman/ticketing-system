from datetime import datetime, time

from pydantic import Field, EmailStr, field_validator

from models.base import BaseSchema

class AddOrgRequest(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    phone: str
    password: str


class AddOrgResponse(BaseSchema):
    name: str
    email: EmailStr
    phone: str


class AddStoreRequest(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    password: str
    address:  str
    phone: str
    latitude: str
    longitude: str
    open_time: time
    close_time: time


    @field_validator("open_time", "close_time", mode="before")
    def validate_time(cls, value):
        return datetime.strptime(value, '%H:%M').time()


class AddStoreResponse(BaseSchema):
    name: str = Field(..., max_items=256)
    email: EmailStr
    address:  str
    phone: str
    latitude: str
    longitude: str
    open_time: time
    close_time: time
