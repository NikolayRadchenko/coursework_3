from project.dao import GenresDAO, MoviesDAO, DirectorsDAO, UsersDAO

from project.services import GenresService, MoviesService, DirectorsService, UsersService, AuthService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = MoviesDAO(db.session)
movie_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService()
