from pydantic import BaseModel
from app.models import ContactType
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateContact(BaseModel):
    name: str
    value: str
    contactType: str
    surname : str
    company : str
    address : str
    email_address : str


# TO support list and get APIs
class ContactSchema(CreateAndUpdateContact):
    id: int

    class Config:
        orm_mode = True


# To support list contact API
class PaginatedContact(BaseModel):
    limit: int
    offset: int
    data: List[ContactSchema]
    

