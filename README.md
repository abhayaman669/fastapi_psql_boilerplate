# FASTAPI + PSQL API Boilerplate

[FastAPI Docs](https://fastapi.tiangolo.com/)  

## Set up for local

```
>>> python3 -m venv venv
>>> pip install -r requirements.txt
```

## Running manually on local

Create a `.env` file (use .example-env as a reference) and then run following command.

```
>>> source .env
>>> python main.py
```

## Using alembic for DB management

1. Add models to `models.py`

example for a model class:

```
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String) 
    phone = Column(String)
    user_type = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
```

2. Create a revision

```
>>> PYTHONPATH=. alembic revision --autogenerate -m "..."
```

3. Running migrations

```
>>> PYTHONPATH=. alembic upgrade head
```

## Running test

```
>>> pytest tests/
```

[Pytest docs](https://docs.pytest.org/en/stable/)  
[Fastapi testing docs](https://fastapi.tiangolo.com/tutorial/testing/)  

## Running through docker

```
>>> sudo docker image build .
>>> sudo docker run -d -p 8080:80 <image>
```