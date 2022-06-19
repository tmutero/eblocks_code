from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
import pymysql

db_user = dotenv_values().get('DBUSER')
db_pass = dotenv_values().get('DBPASS')
db_ipaddress = dotenv_values().get('DBIPADDRESS')
db_port = dotenv_values().get('DBPORT')
db_name = dotenv_values().get('DBNAME')

# db_endpoint = 'mysql+pymysql://root:@127.0.0.1:3306/eblocks'
DATABASE_URL = f'mysql+pymysql://{db_user}:{db_pass}@{db_ipaddress}:{db_port}/{db_name}'


db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine, expire_on_commit=False)
Base = declarative_base()



def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        


        



