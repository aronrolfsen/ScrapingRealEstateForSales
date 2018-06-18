from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, Float

import scraper_app.settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**scraper_app.settings.DATABASE))


def create_houses_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Houses(DeclarativeBase):
    __tablename__ = "houses"

    id = Column(Integer,primary_key=True)
    address = Column('address', String, unique=True)
    city = Column('city', String, nullable=True)
    area = Column('area', String, nullable=True)
    size = Column('size', Integer, nullable=True)
    price = Column('price', Integer, nullable=True)
    debt = Column('debt', Integer, nullable=True)