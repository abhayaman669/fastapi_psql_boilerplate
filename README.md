# FASTAPI + PSQL API Boilerplate
  
[![codecov](https://codecov.io/gh/abhayaman669/fastapi_psql_boilerplate/branch/main/graph/badge.svg)](https://codecov.io/gh/abhayaman669/fastapi_psql_boilerplate)
  
[FastAPI Docs](https://fastapi.tiangolo.com/)
[Docs for this boilerplate](https://github.com/abhayaman669/fastapi_psql_boilerplate/tree/main/docs)

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

## Running linter

```
>>> pylint `pwd`
```

> NOTE: The above cmd is tested on ubuntu.

## Running test

```
>>> pytest tests/
```

[Pytest docs](https://docs.pytest.org/en/stable/)  
[Fastapi testing docs](https://fastapi.tiangolo.com/tutorial/testing/)  

## Running coverage

```
>>> coverage run -m pytest tests/
>>> coverage report
>>> coverage html
```

## Running through docker

```
>>> sudo docker image build .
>>> sudo docker run -d --name myapp 8080:80 <image>
```

## CI using Circleci

We are using Circleci for CI.

**Steps to setup**
  
- Go to [CircleCI](https://circleci.com/).
- Connect you github account.
- you can simply follow the steps there to set up your project there.
- Update `.circleci/config.yml` as per your need.

**Important links for CI**
  
- [What is CI?](https://www.cloudbees.com/continuous-delivery/continuous-integration)
- [Circleci official docs](https://circleci.com/docs/2.0/getting-started/)