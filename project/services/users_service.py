from typing import Optional

from project.dao.users_dao import UsersDAO
from project.tools.security import generate_password_hash
from project.exceptions import ItemNotFound
from project.models import User


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_by_id(self, uid: int) -> User:
        if user := self.dao.get_by_id(uid):
            return user
        raise ItemNotFound(f'User with id={uid} not exists.')

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def create(self, user_data: dict[str, str]):
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def update_password(self, email, new_password):
        self.dao.update_password(email, new_password)

    def delete(self, uid: int):
        self.dao.delete(uid)

    def get_favorites(self, email):
        user = self.get_by_email(email)
        favorites = self.dao.get_favorites(user.id)
        return favorites

