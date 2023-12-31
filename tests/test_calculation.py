import pytest
import requests
import time
from configparser import ConfigParser

from auth import login
from calculation import Calculation, CalculationError
from utils import get_project_id, get_calculation_id, get_cargo_space_id

config = ConfigParser()
config.read('../config.ini')
USERNAME = config.get('user_info', 'username')
PASSWORD = config.get('user_info', 'password')

access_token = login(USERNAME, PASSWORD)['access_token']

calc = Calculation(access_token)


# noinspection PyArgumentList, PyTypeChecker
class TestCalculationCreate:
    def test_create_correct(self):
        input_data = {
            "cargo_spaces": [
                get_cargo_space_id(access_token)
            ],
            "groups": [
                {
                    "title": "Test Group",
                    "pallet": 0,
                    "cargoes": [
                        {
                            "title": "Test Cargo",
                            "length": 500,
                            "width": 500,
                            "height": 500,
                            "mass": 10,
                            "stacking": True,
                            "stacking_limit": 12,
                            "turnover": True,
                            "article": "",
                            "margin_length": 0,
                            "margin_width": 0,
                            "count": 5,
                            "color": "#0000ff",
                        }
                    ],
                    "sort": 1
                }
            ],
            "userSort": True
        }
        calc_result = calc.create(project_id=get_project_id(access_token), input_data=input_data)
        assert isinstance(calc_result, dict)
        assert 'id' in calc_result and 'project' in calc_result \
               and 'status' in calc_result

    def test_create_correct_all_params(self):
        # ожидание завершения предыдущего расчёта
        time.sleep(2)

        input_data = {
            "cargo_spaces": [
                get_cargo_space_id(access_token)
            ],
            "groups": [
                {
                    "title": "Test Group",
                    "pallet": 0,
                    "cargoes": [
                        {
                            "title": "Test Cargo",
                            "length": 500,
                            "width": 500,
                            "height": 500,
                            "mass": 10,
                            "stacking": True,
                            "stacking_limit": 12,
                            "turnover": True,
                            "article": "",
                            "margin_length": 0,
                            "margin_width": 0,
                            "count": 5,
                            "color": "#0000ff",
                        }
                    ],
                    "sort": 1
                }
            ],
            "userSort": True
        }
        calc_result = calc.create(project_id=get_project_id(access_token), input_data=input_data,
                                  status='new', callback_url='https://test.com', external_api=True)
        assert isinstance(calc_result, dict)
        assert 'id' in calc_result and 'project' in calc_result \
               and 'status' in calc_result

    def test_create_incorrect(self):
        with pytest.raises(CalculationError):
            calc.create(project_id=-1, input_data={})

    def test_create_wrong_types_1(self):
        with pytest.raises(TypeError):
            calc.create(project_id=10.0, input_data={})

    def test_create_wrong_types_2(self):
        with pytest.raises(TypeError):
            calc.create(project_id=10, input_data='data')

    def test_create_wrong_types_3(self):
        with pytest.raises(TypeError):
            calc.create(project_id=10, input_data={}, callback_url=100)

    def test_create_wrong_types_4(self):
        with pytest.raises(TypeError):
            calc.create(project_id=10, input_data={}, external_api='1')

    def test_create_invalid_status(self):
        with pytest.raises(ValueError):
            calc.create(project_id=10, input_data={}, status='in queue')

    def test_create_incomplete_1(self):
        with pytest.raises(TypeError):
            calc.create(project_id=10)

    def test_create_incomplete_2(self):
        with pytest.raises(TypeError):
            calc.create(input_data={})

    def test_create_incomplete_3(self):
        with pytest.raises(TypeError):
            calc.create()


class TestCalculationGet:
    def test_get_correct_empty(self):
        calc_result = calc.get()
        assert isinstance(calc_result, dict)
        assert 'count' in calc_result and 'next' in calc_result \
               and 'previous' in calc_result and 'results' in calc_result

    def test_get_correct_all_params(self):
        calc_result = calc.get(favorite=False, is_history=True,
                               is_recalculate=False, ordering='created_at',
                               page=1, page_size=5, project_id=get_project_id(access_token),
                               status='success')
        assert isinstance(calc_result, dict)
        assert 'count' in calc_result and 'next' in calc_result \
               and 'previous' in calc_result and 'results' in calc_result

    def test_get_incorrect_1(self):
        with pytest.raises(CalculationError):
            calc.get(project_id=-1)

    def test_get_incorrect_2(self):
        with pytest.raises(CalculationError):
            calc.get(page=-1)

    def test_get_wrong_types_1(self):
        with pytest.raises(TypeError):
            calc.get(favorite=1)

    def test_get_wrong_types_2(self):
        with pytest.raises(TypeError):
            calc.get(is_history='True')

    def test_get_wrong_types_3(self):
        with pytest.raises(TypeError):
            calc.get(is_recalculate=5.0)

    def test_get_wrong_types_4(self):
        with pytest.raises(TypeError):
            calc.get(ordering=0)

    def test_get_wrong_types_5(self):
        with pytest.raises(TypeError):
            calc.get(page='first')

    def test_get_wrong_types_6(self):
        with pytest.raises(TypeError):
            calc.get(page_size=11.0)

    def test_get_wrong_types_7(self):
        with pytest.raises(TypeError):
            calc.get(project_id='10')

    def test_get_invalid_status(self):
        with pytest.raises(ValueError):
            calc.get(status='in queue')


# noinspection PyArgumentList, PyTypeChecker
class TestCalculationGetByID:
    def test_get_by_id_correct(self):
        calc_result = calc.get_by_id(get_calculation_id(access_token))
        assert isinstance(calc_result, dict)
        assert 'id' in calc_result and 'project_id' in calc_result \
               and 'is_recalculate' in calc_result and 'status' in calc_result \
               and 'updated_at' in calc_result and 'favorite' in calc_result \
               and 'created_at' in calc_result \
               and 'provisional_completion_date' in calc_result

    def test_get_by_id_incorrect(self):
        with pytest.raises(CalculationError):
            calc.get_by_id(-1)

    def test_get_by_id_wrong_type_1(self):
        with pytest.raises(TypeError):
            calc.get_by_id('-1')

    def test_get_by_id_wrong_type_2(self):
        with pytest.raises(TypeError):
            calc.get_by_id(10.5)

    def test_get_by_id_incomplete(self):
        with pytest.raises(TypeError):
            calc.get_by_id()
