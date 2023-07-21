# импорт необходимых модулей
from auth import login, AuthenticationError
from calculation import Calculation, CalculationError


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
project_id = 0  # ID проекта
input_data = {}  # данные для расчёта
try:
    result = calc.create(project_id=project_id, input_data=input_data)
    print('\nРасчёт создан: {}'.format(result))
except CalculationError as e:
    print('\nОшибка создания расчёта: {}'.format(e))

# со всеми возможными аргументами
status = 'new'  # статус расчёта
callback_url = 'www.test.com'  # URL для отправки ответа
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
project_id = 0  # ID проекта
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
calculation_id = 0  # ID расчёта
try:
    calculation_result = calc.get_by_id(calculation_id=calculation_id)
    print('\nРасчёт с ID == {}: {}'.format(calculation_id, calculation_result))
except CalculationError as e:
    print('\nОшибка получения расчёта: {}'.format(e))
