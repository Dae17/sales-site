FROM nikolaik/python-nodejs:python3.10-nodejs18-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJ_DEBUG 0

# Install Postgres Dependencies
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install --no-install-recommends python3-dev postgresql postgresql-contrib python3-psycopg2 libpq-dev gcc
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

# Install Frontend Dependencies, then Build Frontend.
WORKDIR /usr/src/app/frontend
RUN npm install
RUN npm run build
WORKDIR /usr/src/app

RUN python manage.py collectstatic
EXPOSE 8000
CMD gunicorn --bind=0.0.0.0:8000 devproject.wsgi