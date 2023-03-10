from project.dao import GenresDAO, MoviesDAO, DirectorsDAO

from project.services import GenresService, MoviesService, DirectorsService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = MoviesDAO(db.session)
movie_dao = DirectorsDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
