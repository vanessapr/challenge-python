import os
from abc import ABC
from dotenv import load_dotenv, find_dotenv


class IEnvironmentConfig(ABC):
    pass


class EnvironmentConfig(IEnvironmentConfig):
    load_dotenv(find_dotenv())

    MODE_DEBUGGER = os.environ.get('MODE_DEBUGGER', False)
    PORT = os.environ.get('PORT', 5000)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'biB2YW5lc3NhcHIuODVAZ21haWwuY29tOjEyMzQ1Ngo=')