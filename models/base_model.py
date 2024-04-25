#!/usr/bin/python3
"""
This script defines the BaseModel object.
"""

import models
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

time_format = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base() if models.storage_t == "db" else object


class BaseModel:
    """Type of the basic model"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Commence the foundation model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time_format) \
                        if isinstance(value, str) else datetime.utcnow()
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """The string denoting the BaseModel class"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Incorporate the present datetime into the 'updated_at' attribute."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Generate a dictionary comprising every key and value of instances"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = dict_copy["created_at"].strftime(time_format)
        dict_copy["updated_at"] = dict_copy["updated_at"].strftime(time_format)
        dict_copy.pop("_sa_instance_state", None)
        return dict_copy

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
