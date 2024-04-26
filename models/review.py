#!/usr/bin/python
""" Review module """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review entity """
    __tablename__ = 'reviews' if storage_t == 'db' else None
    if storage_t == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        place = relationship("Place", back_populates="reviews")
        user = relationship("User", back_populates="reviews")
    else:
        place_id = user_id = text = ""

    def __init__(self, **kwargs):
        """ Initializes Review instance """
        super().__init__(**kwargs)
