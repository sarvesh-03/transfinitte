"""
setup database
"""
import os
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """
    Settings
    """

    sqlalchemy_database_url: str = os.getenv("URL")

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


settings = Settings()
