#!/usr/bin/Python3
"""This module defines a class to manage data base storage for hbnb clone"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import MySQLdb


class DBStorage:
    """This class manages storage of hbnb models in data base"""

    __engine = None
    __session = None

    classes = {
        'User': User, 'Place': Place, 'State': State,
        'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """creates the engine"""

        credentials = {
            "user": getenv("HBNB_MYSQL_USER"),
            "pwd": getenv("HBNB_MYSQL_PWD"),
            "host": getenv("HBNB_MYSQL_HOST"),
            "db": getenv("HBNB_MYSQL_DB")
        }

        self.__engine = create_engine('mysql+mysqldb://{user}:{pwd}@{host}'
                                      ':3306/{db}'.format(**credentials),
                                      encoding='utf-8', pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session depending of the class name"""

        objs_dict = {}
        if cls:
            my_query = self.__session.query(cls).all()
            for obj in my_query:
                objs_dict[cls + "." + obj.id] = obj
        else:
            for key, value in self.classes.items():
                my_query = self.__session.query(value).all()
                for obj in my_query:
                    objs_dict[key + "." + obj.id] = obj

        return objs_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''
        call remove() method on the private session attribute
        '''
        self.__session.remove()
