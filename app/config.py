from pydantic import BaseSettings


class Config(BaseSettings):

    host: str = "localhost"
    port: int = 8000
    reload: bool = True


config = Config()