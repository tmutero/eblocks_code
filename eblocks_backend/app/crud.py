from typing import List
from sqlalchemy.orm import Session
from app.exceptions import ContactAlreadyExistError, ContactNotFoundError
from app.models import Contact
from app.schemas import CreateAndUpdateContact


# Function to get list of contact info
def get_all_contact(session: Session, limit: int, offset: int) -> List[Contact]:
    return session.query(Contact).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_contact_info_by_id(session: Session, _id: int) -> Contact:
    contact = session.query(Contact).get(_id)

    if contact is None:
        raise ContactNotFoundError

    return contact


# Function to add a new contact info to the database
def create_contact(session: Session, contact: CreateAndUpdateContact) -> Contact:
    car_details = session.query(Contact).filter(Contact.value == contact.value, Contact.name == contact.name).first()
    if car_details is not None:
        raise ContactAlreadyExistError

    new_contact = Contact(**contact.dict())
    session.add(new_contact)
    session.commit()
    session.refresh(new_contact)
    return new_contact


# Function to update details of the contact
def update_contact(session: Session, _id: int, info_update: CreateAndUpdateContact) -> Contact:
    contact = get_contact_info_by_id(session, _id)

    if contact is None:
        raise ContactNotFoundError

    contact.value = info_update.value
    contact.name = info_update.name
    contact.contactType = info_update.contactType
    contact.surname = info_update.surname
    contact.company = info_update.company
    contact.address = info_update.address
    contact.email_address = info_update.email_address

    session.commit()
    session.refresh(contact)

    return contact


# Function to delete a contact info from the db
def delete_contact(session: Session, _id: int):
    contact = get_contact_info_by_id(session, _id)

    if contact is None:
        raise ContactNotFoundError

    session.delete(contact)
    session.commit()

    return
