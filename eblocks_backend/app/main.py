# main.py
# Import FastAPI

from email.mime import application
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.api import *

from fastapi.middleware.cors import CORSMiddleware

# Initialize the app
application = FastAPI(title="T.Mutero Backend")


application.include_router(router)



origins = ["*"]

application.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET operation at route '/'
@application.get('/')
def root_api():
    return {"message": "T.Mutero Backend"}




