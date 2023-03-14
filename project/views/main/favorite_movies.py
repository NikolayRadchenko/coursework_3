from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import favorite_movie, movie
from project.tools.security import get_email_from_token

api = Namespace('favorites')


@api.route('/movies/')
class FavoriteMoviesView(Resource):
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all favorite movies.
        """
        email = get_email_from_token(request.headers)
        return user_service.get_favorites(email)


@api.route('/movies/<int:movie_id>')
class FavoriteMovieView(Resource):
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def post(self, movie_id):
        """
        Post favorite movie.
        """
        email = get_email_from_token(request.headers)
        user_service.create_favorite(email, movie_id)
        return "", 201

    def delete(self, movie_id):
        """
        Delete favorite movie.
        """
        email = get_email_from_token(request.headers)
        user_service.delete_favorite(email, movie_id)
        return "", 201

