
from infrastructure.storage import storage
from infrastructure.database import db

import logging


def init_log():
    logging.basicConfig(
        level="INFO", format="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s")


def init_database():
    db.init_app()


def init_storage():
    # storage
    storage.init_app()
