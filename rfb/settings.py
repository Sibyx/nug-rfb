import logging
import os
from ipaddress import IPv4Address
from logging import INFO
from pathlib import Path

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        # Paths
        self.BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        self.ENV_FILE = os.path.join(self.BASE_DIR, '.env')
        print(self.ENV_FILE)
        # .env
        if os.path.exists(self.ENV_FILE):
            load_dotenv(dotenv_path=self.ENV_FILE, verbose=False)

        # Network config
        self.HOST = IPv4Address(os.getenv('HOST', '127.0.0.1'))
        self.PORT = os.getenv('PORT', 5900)

        # Logging
        self.VERBOSE = bool(os.getenv('VERBOSE', 1))
        self.LOG_LEVEL = int(os.getenv('LOG_LEVEL', INFO))
        self.LOG_FORMAT = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d]: %(message)s',
            datefmt='%Y-%m-%dT%H:%M:%S%z'
        )
