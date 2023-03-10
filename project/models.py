from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    genre = relationship('Genre')
    director_id = Column(Integer(), ForeignKey('directors.id'))
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre = Column(String(100))