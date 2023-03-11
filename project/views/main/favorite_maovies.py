from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import movie
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
