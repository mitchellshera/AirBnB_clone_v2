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
from os import environ


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True
        )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the database session"""
        objects = {}
        classes = [BaseModel]

        if cls:
            classes = [cls] if isinstance(cls, type) else [eval(cls)]

        for c in classes:
            query = self.__session.query(c)
            for obj in query.all():
                key = f'{obj.__class__.__name__}.{obj.id}'
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
