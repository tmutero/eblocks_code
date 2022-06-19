import datetime
from xmlrpc.client import DateTime
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Enum
from app.database import Base, db_engine
import enum



class ContactType(str, enum.Enum):
    Email = "Email"
    Mobile = "Mobile"


class Contact(Base):
    __tablename__ = "tbl_contact"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), index=True)
    surname = Column(String(250), index=True)
    value = Column(String(250), index=True)
    contactType = Column(String(250), index=True)
    company = Column(String(250), index=True)
    address = Column(String(250), index=True)
    email_address = Column(String(250), index=True)
    
    
if __name__ == "__main__":
    Base.metadata.create_all(db_engine)
