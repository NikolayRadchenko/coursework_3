class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class UserAlreadyExists(BaseServiceError):
    code = 400
    massage = "Такой пользователь уже существует"