#!/usr/bin/env python3
""" Class amenity module """
from models import storage_type
from models.entity import Entity, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(Entity, Base):
    """ Entity representation of an amenity """
    if storage_type == 'db':
        __tablename__ = 'amenity'
        name = Column(String(128), nullable=False)
    else:
        name = str()

    def __init__(self, **data):
        """ Initializes the instance of Amenity """
        super().__init__(**data)
