#!/usr/bin/python3
"""
DBStorage definition of class
"""

import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_map = {"Amenity": Amenity, "City": City, "Place": Place,
             "Review": Review, "State": State, "User": User}


class DBStorage:
    """Communicates with the MySQL repository"""
    __engine = None
    __session = None

    def __init__(self):
        """Initiates a DBStorage container."""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db))
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Performs a database session query"""
        obj_dict = {}
        for cls_name in class_map:
            if cls is None or cls is class_map[cls_name] or cls is cls_name:
                objects = self.__session.query(class_map[cls_name]).all()
                for obj in objects:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """If not None, removes obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Invokes the remove() method on the session private attribute"""
        self.__session.remove()
