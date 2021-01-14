FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN cd app/

RUN export HOST=localhost
RUN export PORT=3000
RUN export RELOAD=true
RUN export PSQL_DB_URL=postgresql://postgres:postgres@localhost:5432/boil_db

RUN pip install -r requirements.txt