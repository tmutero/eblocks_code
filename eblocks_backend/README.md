# FastAPI example app

This repository contains code for asynchronous example api using the [Fast Api framework](https://fastapi.tiangolo.com/) ,Uvicorn server and Postgres Database to perform crud operations on notes.

## Installation method 1 (Run application locally)

Quickstart
----------

Then run the following commands to bootstrap your environment with ``poetry``: ::

    git clone https://github.com/xiaozl/fastapi-realworld-example-app-mysql.git
    cd fastapi-realworld-example-app-mysql
    poetry install
    poetry shell

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application: ::
    
    DBUSER="root"
    DBPASS=""
    DBIPADDRESS="127.0.0.1"
    DBPORT="3306"
    DBNAME="eblocks"


To run the web application in debug use init mysql db: ::

On Windows 
    uvicorn app.main:application --host 127.0.0.1 --port 5000

Mac or Linux 
    sh run.sh

## Installation method 2 (Run Locally using Docker)

1.Ensure [Docker](https://docs.docker.com/install/) is installed
2.Ensure [Docker Compose](https://docs.docker.com/compose/install/) is installed
3.Clone this Repo
`git clone (https://github.com/KenMwaura1/Fast-Api-example)`

4.`cd Fast-Api-example`

5.Use Docker-Compose to spin up containers `docker-compose up -d --build`

6.If everything completes should be available on [notes](http://localhost:8002/notes)

7.Docs are generated on [docs](http://localhost:8002/docs)

## Tests

Tests are available using pytest
Run them using `pytest .` while in the root directory (/Fast-Api-example)

## Documentation

Open API Documentation is provided by [Redoc](http://localhost:8002/redoc)