#!/usr/bin/python3
"""Within this module is the User class."""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class signifies a user."""

    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructs a User"""
        super().__init__(*args, **kwargs)
