import os

import requests
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))
BASE_URL = config.get('main', 'base_url')


class AuthenticationError(Exception):
    """Класс исключения, вызываемого при ошибке аутентификации."""
    pass


def login(username: str, password: str) -> dict:
    """
    Функция для аутентификации и получения токенов.\n
    На вход принимает имя пользователя `username` и пароль `password`.
    Возвращает словарь, содержащий токены, либо вызывает исключение `AuthenticationError`.
    """

    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError('`username` and `password` must be strings')

    url = BASE_URL + 'auth/login/'

    payload = {'username': username, 'password': password}

    response = requests.post(url, data=payload)
    json = response.json()

    if response.status_code == 200:
        return json
    else:
        raise AuthenticationError(json)
