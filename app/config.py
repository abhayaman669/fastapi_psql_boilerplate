"""
This file will extract all the env variables from the environment
"""

from pydantic import BaseSettings


class Config(BaseSettings): # pylint:disable=too-few-public-methods
    """
    Config class
    """

    host: str = "localhost"
    port: int = 8000
    reload: bool = True
    psql_db_url: str = None


config = Config()
