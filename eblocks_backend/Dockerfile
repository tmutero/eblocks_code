FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 5000
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD ["python", "./models.py"]


CMD ["uvicorn", "app.main:application", "--host", "127.0.0.1", "--port", "5000"]
#CMD uvicorn app.main:application --host 127.0.0.1 --port 


# FROM python:3.9

# COPY . .

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install python dependencies
# RUN pip freeze > requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # running migrations
# CMD ["python", "./models.py"]


# COPY . /code/
# EXPOSE 5000

# CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "5000"]