FROM ubuntu:20.04

RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip

RUN apt install python3-dev libpq-dev python3.8-venv -y

RUN pip install django djangorestframework django-cors-headers django-forestadmin gunicorn psycopg2 dj-database-url

ADD . /app

WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "pravum.wsgi"]
