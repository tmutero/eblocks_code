# Eblocks Backend

This repository contains code for asynchronous example api using the [Fast Api framework](https://fastapi.tiangolo.com/) ,Uvicorn server and Postgres Database to perform crud operations on notes.

## Installation method 1 (Run application locally)

Quickstart
----------

Create Python Environment::

    python3 -m venv eblocks_env
    cd eblocks_env

Activate Environment::

    source bin/activate

Then run the following commands to clone application ::

    git clone https://github.com/tmutero/eblocks_code.git

    cd eblocks_code/eblocks_backend

Installing the packages need to run backend::

    pip install -r requirements.text

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application: ::
    
    DBUSER="root"
    DBPASS=""
    DBIPADDRESS="127.0.0.1"
    DBPORT="3306"
    DBNAME="eblocks"


Auto create database tables run the command below [**You should be in eblocks_code/eblocks_backend/app floder] :
   
    python models.py


To run the web application in debug use: ::

On Windows 

    uvicorn app.main:application --host 127.0.0.1 --port 5000

Mac or Linux use below command or same windows command above ::

    sh run.sh 


## Tests

Tests are available using pytest
Run them using `pytest .` while in the root directory (/eblocks_code)

## Documentation

Open API Documentation is provided by [Redoc](http://localhost:5000/redoc)

or 

http://localhost:5000/docs