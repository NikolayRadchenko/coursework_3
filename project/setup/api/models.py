from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='name'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='name'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='title'),
    'description': fields.String(required=True, max_length=1000, example='description'),
    'trailer': fields.String(required=True, example='URL'),
    'year': fields.Integer(required=True, example=2000),
    'rating': fields.Float(required=True, example=2.3),
    'genre_id': fields.Integer(required=True, example=1),
    'genre': fields.Nested(genre),
    'director_id': fields.Integer(required=True, example=1),
    'director': fields.Nested(director),
})


user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, example='email@email.com'),
    'password': fields.String(required=True, example='password'),
    'name': fields.String(example='name'),
    'surname': fields.String(example='surname'),
    'favorite_genre': fields.String(example='favorite_genre'),
    'genre': fields.Nested(genre)
})

auth: Model = api.model('Авторизация', {
    'email': fields.String(required=True, example='email@email.com'),
    'password': fields.String(required=True, example='password'),
})

auth_result: Model = api.model('', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True),
})

favorite_movie: Model = api.model('Избранное', {
    'id': fields.Integer(required=True, example=1),
    'user_id': fields.Integer(required=True, example=1),
    'user': fields.Nested(user),
    'movie_id': fields.Integer(required=True, example=1),
    'movie': fields.Nested(movie),
})
