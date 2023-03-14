from sqlalchemy.exc import IntegrityError
from project.exceptions import UserAlreadyExists
from project.tools.security import generate_password_hash

from project.models import User, FavoriteMovies, Movie


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_data):
        try:
            user = User(**user_data)
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_one(user_data.get("id"))
        if user_data.get("email"):
            user.email = user_data.get("email")
        if user_data.get("password"):
            user.password = user_data.get("password")
        if user_data.get("name"):
            user.name = user_data.get("name")
        if user_data.get("surname"):
            user.surname = user_data.get("surname")
        if user_data.get("favourite_genre"):
            user.favourite_genre = user_data.get("favourite_genre")
        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists

    def update_password(self, email, new_password):
        user = self.get_by_email(email)
        user.password = generate_password_hash(new_password)

        self.session.add(user)
        self.session.commit()

    def get_favorites(self, user_id):
        result = self.session.query(Movie).join(FavoriteMovies).filter(FavoriteMovies.user_id == user_id).all()
        return result

    def create_favorite(self, favorite_movie_data):
        favorite_movie = FavoriteMovies(**favorite_movie_data)
        self.session.add(favorite_movie)
        self.session.commit()

    def delete_favorite(self, user_id, movie_id):
        favorite_movie_id = self.session.query(FavoriteMovies).filter(FavoriteMovies.user_id == user_id).get(movie_id)
        self.session.delete(favorite_movie_id)
        self.session.commit()
