from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import get_email_from_token

api = Namespace('user')


@api.route('/<int:user_id>/')
class AuthView(Resource):
    @api.expect(user)
    @api.response(201, description='OK')
    def get(self, user_id: int):
        """
        Страница пользователя
        """
        # email = get_email_from_token(request.headers)
        return user_service.get_by_id(user_id)

