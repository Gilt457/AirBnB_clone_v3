#!/usr/bin/python3
"""Urban class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Representation of cities"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initialization of a city"""
        super().__init__(*args, **kwargs)
