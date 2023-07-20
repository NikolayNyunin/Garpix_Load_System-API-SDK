# Garpix Load System API SDK

Это SDK для взаимодействия с API системы Garpix Load System. Оно содержит следующие модули:

- `auth.py` - аутентификация
- `calculation.py` - работа с расчетами
- `config.ini` - конфигурационный файл

## Аутентификация

Модуль auth.py предоставляет функцию `login` для аутентификации пользователя через API и получения токенов доступа.
### Использование
Чтобы аутентифицировать пользователя, вызовите функцию `login`, передав ей имя пользователя и пароль:

```python
import auth
tokens = auth.login('username', 'password')
```

Это вернет словарь с токенами в случае успешной аутентификации. 
При ошибке - исключение `AuthenticationError`.

### Настройка
Базовый URL API задан в `config.ini`:

```ini
[main]
base_url = https://example.com/api/
```

## Модуль для работы с расчетами

### Использование
Для начала работы нужно создать экземпляр класса Calculation, передав токен доступа:

```
calc = Calculation(access_token)
```
Затем можно вызывать методы:

- `create` - создание нового расчета
- `get` - получение списка расчетов
- `get_by_id` - получение конкретного расчета по id

### Создание расчета
```python
calc.create(
  project_id=123,
  input_data={'param1': 'value1'},
  status='new'  
)
```
На вход принимаются:
- `project_id` - id проекта
- `input_data` - входные данные для расчета
- `status` - статус расчета
Также можно указать:
- `callback_url` - url для callback
- `external_api` - признак использования внешнего api
В случае успеха вернется словарь с данными о созданном расчете.
При ошибке будет выброшено исключение `CalculationError`.

### Получение расчетов
Чтобы получить список расчетов, вызовите метод get и передайте нужные параметры фильтрации:

```python
calc.get(
  project_id=123,
  status='success'
)
```
Доступные параметры:

- `favorite` - избранные расчеты
- `is_history` - исторические расчеты
- `is_recalculate` - пересчитанные
- `ordering` - сортировка
- `page` - номер страницы
- `page_size` - размер страницы
- `project_id` - id проекта
- `status` - статус

### Получение расчета по id
Для получения конкретного расчета вызовите get_by_id, передав id расчета:

```python
calc = calc.get_by_id(12345)
```
Вернется словарь с данными этого расчета.

### Настройка
Базовый URL API задается в config.ini в разделе main параметром base_url.

### Требования

- Python 3.6 и выше
- Библиотека `requests`
- Модуль `configparser`

## Тестирование

Тесты написаны в tests/test_calculation.py с использованием pytest.
### Установка
Используйте pip для установки:
```python
pip install git+https://github.com/NikolayNyunin/Garpix_Load_System-API-SDK
```
или скопируйте исходный код.
### Использование
```python

from garpix_sdk import login, Calculation

tokens = login('username', 'password')
calc = Calculation(tokens['access_token'])

#Создать расчет
calculation = calc.create(...)

#Получить расчеты
calculations = calc.get()

#Получить расчет по id
single_calculation = calc.get_by_id(123)
```

## Изменения
Версия 0.1.0:
- Аутентификация
- Создание, получение и фильтрация расчетов

В планах:
- Поддержка нескольких серверов API
- Сохранение токенов
- Уведомления при изменении расчетов

## Авторы
- Nikolay Nyunin
- Bulat Askarov 


