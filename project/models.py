from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer(), nullable=False)
    rating = Column(Float(), nullable=False)
    genre_id = Column(Integer(), ForeignKey('genres.id'), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer(), ForeignKey('directors.id'), nullable=False)
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genres = Column(String(100))


class FavoriteMovies(models.Base):
    __tablename__ = 'favorite_movies'

    user_id = Column(ForeignKey(User.id))
    movie_id = Column(ForeignKey(Movie.id))
