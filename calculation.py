import os

import requests
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))
BASE_URL = config.get('main', 'base_url')


class CalculationError(Exception):
    """Класс исключения, вызываемого при ошибке создания или получения расчёта."""
    pass


class Calculation:
    """Класс, реализующий расчёт в GLS."""

    def __init__(self, access_token: str) -> None:
        self.url = BASE_URL + 'calculation/'
        self.headers = {'Authorization': 'Bearer {}'.format(access_token)}
        self.status_options = ['calculating', 'cancel', 'designed', 'error',
                               'for_recalculation', 'in_queue', 'irrelevant', 'new',
                               'queue_recalculation', 'recalculation', 'success']

    def create(self, project_id: int, input_data: dict, status=None,
               callback_url=None, external_api=None) -> dict:
        """Создание нового расчёта."""

        if not isinstance(project_id, int):
            raise TypeError('`project_id` must be an integer')
        if not isinstance(input_data, dict):
            raise TypeError('`input_data` must be a dictionary')
        if status is not None and status not in self.status_options:
            raise ValueError('`status` is invalid')
        if callback_url is not None and not isinstance(callback_url, str):
            raise TypeError('`callback_url` must be a string')
        if external_api is not None and not isinstance(external_api, bool):
            raise TypeError('`external_api` must be a boolean')

        payload = {'project': project_id, 'input_data': input_data, 'status': status,
                   'callback_url': callback_url, 'external_api': external_api}

        response = requests.post(self.url, data=payload, headers=self.headers)

        if response.status_code == 201:
            return response.json()
        elif response.status_code == 500:
            raise CalculationError(response.text)
        else:
            raise CalculationError(response.json())

    def get(self, favorite=None, is_history=None, is_recalculate=None, ordering=None,
            page=None, page_size=None, project_id=None, status=None) -> dict:
        """Получение результатов расчёта."""

        if favorite is not None and not isinstance(favorite, bool):
            raise TypeError('`favorite` must be a boolean')
        if is_history is not None and not isinstance(is_history, bool):
            raise TypeError('`is_history` must be a boolean')
        if is_recalculate is not None and not isinstance(is_recalculate, bool):
            raise TypeError('`is_recalculate` must be a boolean')
        if ordering is not None and not isinstance(ordering, str):
            raise TypeError('`ordering` must be a string')
        if page is not None and not isinstance(page, int):
            raise TypeError('`page` must be an integer')
        if page_size is not None and not isinstance(page_size, int):
            raise TypeError('`page_size` must be an integer')
        if project_id is not None and not isinstance(project_id, int):
            raise TypeError('`project_id` must be an integer')
        if status is not None and status not in self.status_options:
            raise ValueError('`status` is invalid')

        params = {'favorite': favorite, 'is_history': is_history,
                  'is_recalculate': is_recalculate, 'ordering': ordering,
                  'page': page, 'page_size': page_size,
                  'project_id': project_id, 'status': status}

        response = requests.get(self.url, headers=self.headers, params=params)
        json = response.json()

        if response.status_code == 200:
            return json
        else:
            raise CalculationError(json)

    def get_by_id(self, calculation_id: int) -> dict:
        """Получение результатов расчёта по его id."""

        if not isinstance(calculation_id, int):
            raise TypeError('`calculation_id` must be an integer')

        url = self.url + '{}/'.format(calculation_id)

        response = requests.get(url, headers=self.headers)
        json = response.json()

        if response.status_code == 200:
            return json
        else:
            raise CalculationError(json)
