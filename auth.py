import requests

BASE_URL = 'https://back.glsystem.net/api/v1/'


class AuthenticationError(Exception):
    """Класс исключения, вызываемого при ошибке аутентификации."""
    pass


def login(username: str, password: str) -> dict:
    """
    Функция для аутентификации и получения токенов.\n
    На вход принимает имя пользователя `username` и пароль `password`.
    Возвращает словарь, содержащий токены, либо вызывает исключение `AuthenticationError`.
    """

    url = BASE_URL + 'auth/login/'

    payload = {'username': username, 'password': password}

    response = requests.post(url, data=payload)
    json = response.json()

    if response.status_code == 200:
        return {'access_token': json['access_token'], 'refresh_token': json['refresh_token']}
    else:
        raise AuthenticationError(json)
