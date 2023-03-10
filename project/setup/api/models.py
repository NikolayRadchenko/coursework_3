from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название'),
    'description': fields.String(required=True, max_length=1000, example='Описание'),
    'trailer': fields.String(required=True, example='Ссылка'),
    'year': fields.Integer(required=True, example=2000),
    'rating': fields.Float(required=True, example=2.3),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Имя'),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='Почта'),
    'password': fields.String(required=True, max_length=100, example='Пароль'),
    'name': fields.String(max_length=100, example='Имя'),
    'surname': fields.String(max_length=100, example='Второе имя'),
    'favorite_genre': fields.String(max_length=100, example='Любимый жанр'),
})
