import os

import requests
from configparser import ConfigParser

from calculation import Calculation

config = ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))
BASE_URL = config.get('main', 'base_url')


def get_project_id(access_token: str) -> int:
    """Функция для получения валидного ID существующего проекта."""

    calc = Calculation(access_token)

    return calc.get()['results'][0]['project_id']


def get_calculation_id(access_token: str) -> int:
    """Функция для получения валидного ID существующего расчёта."""

    calc = Calculation(access_token)

    return calc.get()['results'][0]['id']


def get_cargo_space_id(access_token: str) -> int:
    """Функция для получения валидного ID существующего грузового пространства."""

    url = BASE_URL + 'cargo-space/'
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(url, headers=headers)
    json = response.json()

    return json['results'][0]['id']
