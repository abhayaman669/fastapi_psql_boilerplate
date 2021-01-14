from pydantic import BaseSettings


class Config(BaseSettings):

    host: str = "localhost"
    port: int = 8000
    reload: bool = True
    psql_db_url: str = None


config = Config()
