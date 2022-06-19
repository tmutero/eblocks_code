from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.crud import get_all_contact, create_contact, get_contact_info_by_id, update_contact, delete_contact
from app.database import get_db
from app.exceptions import ContactException
from app.schemas import ContactSchema, CreateAndUpdateContact, PaginatedContact
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@cbv(router)
class Contacts:
    session: Session = Depends(get_db)

    # API to get the list of contact 

    
    @router.get("/get_all_contacts", response_model = CreateAndUpdateContact)
    def list_contacts(self, limit: int = 10, offset: int = 0):
        contact_list = get_all_contact(self.session, limit, offset)
        json_compatible_item_data = jsonable_encoder(contact_list)
        
        return JSONResponse(content=json_compatible_item_data)

    # API endpoint to add a contact to the database
    @router.post("/add_contact")
    def add_contact(self, contact: CreateAndUpdateContact):

        try:
            contact = create_contact(self.session, contact)
            return contact
        except ContactException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular contact
@router.get("/get_contact/{contact_id}", response_model=ContactSchema)
def get_contact(contact_id: int, session: Session = Depends(get_db)):

    try:
        contact = get_contact_info_by_id(session, contact_id)
        return contact
    except ContactException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing contacts 
@router.put("/update/{contact_id}", response_model=ContactSchema)
def update(contact_id: int, new_info: CreateAndUpdateContact, session: Session = Depends(get_db)):

    try:
        contact = update_contact(session, contact_id, new_info)
        return contact
    except ContactException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a contact info from the data base
@router.delete("/delete/{contact_id}")
def delete(contact_id: int, session: Session = Depends(get_db)):

    try:
        return delete_contact(session, contact_id)
    except ContactException as cie:
        raise HTTPException(**cie.__dict__)