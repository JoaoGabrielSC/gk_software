import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

class EnvVars(Enum):
    DATABASE_URL = 'DATABASE_URL'

class Config():

    __instance = None
    def __new__(cls):
        if Config.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.config = {}
            for var in EnvVars:
                try:
                    cls.__instance.config[var.name] = os.environ[var.value]
                    print(f"Environment variable {var.name} defined")
                except KeyError:
                    print(f"Warning: Environment variable {var.name} not defined")
        return cls.__instance
    
    def get_config(self, key):
        if key in self.config:
            return self.config[key]
        else:
            return None
