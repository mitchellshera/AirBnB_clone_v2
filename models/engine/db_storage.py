#!/usr/bin/python3                                                                                                                                                              
""" new engine for sqlAlchemy """
from sqlalchemy.ext.declarative import declarative_base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV', 'development')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Query on the database session"""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            if cls in classes:
                for obj in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{obj.id}"
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and create a current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
        self.__session = Session()
    def close(self):
        """ calls remove()
        """
        self.__session.close()