#!/usr/bin/python3
"""
Initiate the delivery models
"""

from os import getenv


def initialize_storage():
    storage_t = getenv("HBNB_TYPE_STORAGE")

    if storage_t == "db":
        from models.engine.db_storage import DBStorage
        return DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        return FileStorage()


storage = initialize_storage()
storage.reload()
