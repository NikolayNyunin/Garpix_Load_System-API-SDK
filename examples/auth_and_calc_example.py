# импорт необходимых модулей
import time

from auth import login, AuthenticationError
from calculation import Calculation, CalculationError
from utils import get_project_id, get_calculation_id, get_cargo_space_id


# получение логина и пароля от пользователя
username = input('Введите имя пользователя GLS: ')
password = input('Введите пароль: ')


# получение токена для доступа к системе
tokens = login(username=username, password=password)
print('\nТокены: {}'.format(tokens))
access_token = tokens['access_token']


# инициализация объекта для работы с расчётами
calc = Calculation(access_token=access_token)


# создание нового расчёта
# только с обязательными аргументами
project_id = get_project_id(access_token)  # ID проекта
input_data = {  # данные для расчёта
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
try:
    result = calc.create(project_id=project_id, input_data=input_data)
    print('\nРасчёт создан: {}'.format(result))
except CalculationError as e:
    print('\nОшибка создания расчёта: {}'.format(e))

# ожидание завершения предыдущего расчёта
time.sleep(2)

# со всеми возможными аргументами
status = 'new'  # статус расчёта
callback_url = 'https://test.com'  # URL для отправки ответа
external_api = True  # признак использования внешнего API
try:
    result = calc.create(project_id=project_id, input_data=input_data, status=status,
                         callback_url=callback_url, external_api=external_api)
    print('\nРасчёт создан: {}'.format(result))
except CalculationError as e:
    print('\nОшибка создания расчёта: {}'.format(e))


# получение информации о расчётах
# без аргументов
try:
    calculation_results = calc.get()
    print('\nРасчёты: {}'.format(calculation_results))
except CalculationError as e:
    print('\nОшибка получения расчётов: {}'.format(e))

# со всеми возможными аргументами
favorite = False  # избранные расчёты
is_history = True  # расчёты из истории
is_recalculate = False  # перерасчёты
ordering = 'created_at'  # поле, используемое для сортировки результатов
page = 1  # номер страницы
page_size = 5  # число результатов на странице
project_id = get_project_id(access_token)  # ID проекта
status = 'success'  # статус расчёта
try:
    calculation_results = calc.get(favorite=favorite, is_history=is_history,
                                   is_recalculate=is_recalculate, ordering=ordering,
                                   page=page, page_size=page_size, project_id=project_id,
                                   status=status)
    print('\nРасчёты, удовлетворяющие параметрам: {}'.format(calculation_results))
except CalculationError as e:
    print('\nОшибка получения расчётов: {}'.format(e))


# получение информации о конкретном расчёте по его ID
calculation_id = get_calculation_id(access_token)  # ID расчёта
try:
    calculation_result = calc.get_by_id(calculation_id=calculation_id)
    print('\nРасчёт с ID == {}: {}'.format(calculation_id, calculation_result))
except CalculationError as e:
    print('\nОшибка получения расчёта: {}'.format(e))
