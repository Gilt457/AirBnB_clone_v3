#!/usr/bin/python3
"""This module contains the State class."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import sqlalchemy
from os import getenv


class State(BaseModel, Base):
    """This class is a model representation of a state."""
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the State class."""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """Returns a list of City objects associated with this state."""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
