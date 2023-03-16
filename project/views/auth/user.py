from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import auth_required, get_email_from_token, login_required

api = Namespace('user')


@api.route('/')
class AuthView(Resource):
    @api.expect(user)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    @auth_required
    def get(self):
        """
        Страница пользователя
        """
        email = get_email_from_token(request.headers)
        return user_service.get_by_email(email)

    @login_required
    def patch(self):
        """
        Изменение информации о пользователе
        """
        user_service.update(request.json)
        return "OK", 201


@api.route('/password/')
class AuthView(Resource):
    @login_required
    def put(self):
        """
        Изменение пароля пользователя
        """
        email = get_email_from_token(request.headers)
        data = request.json
        user_service.update_password(email, data.get('password'))
        return "OK", 201
