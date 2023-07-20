# Garpix Load System API SDK

Это SDK для взаимодействия с API системы Garpix Load System. Оно содержит следующие модули:

- `auth.py` - аутентификация
- `calculation.py` - работа с расчетами
- `config.ini` - конфигурационный файл

## Аутентификация

Модуль `auth.py` предоставляет функцию `login()` для аутентификации через API.

```python
import auth

tokens = auth.login('username', 'password')
```

При успехе получите токены, при ошибке - исключение `AuthenticationError`.

Базовый URL API задан в `config.ini`:

```ini
[main]
base_url = https://example.com/api/
```

## Работа с расчетами

Используйте класс `Calculation` из `calculation.py` для работы с расчетами.

```python
from calculation import Calculation

calc = Calculation(access_token)
```

Методы класса:
- `create()` - создать новый расчет
- `get()` - получить список расчетов
- `get_by_id()` - получить расчет по ID

### Создание расчета

```python
calc.create(
  project_id=123,  
  input_data={'param1': 'value1'},
  status='new'   
)
```

Возвращает данные созданного расчета или выбрасывает `CalculationError`.

### Получение расчетов

```python 
calc.get(
  project_id=123,   
  status='success'
)
```

Можно фильтровать по:
- `favorite`  
- `is_history` 
- `is_recalculate`
- и др.

### Получение расчета по ID

```python
calc = calc.get_by_id(12345)
```

Возвращает данные расчета с указанным ID.
# Аутентификация через API

Модуль auth.py предоставляет функцию `login` для аутентификации пользователя через API и получения токенов доступа.

## Использование

Чтобы аутентифицировать пользователя, вызовите функцию `login`, передав ей имя пользователя и пароль:

```
import auth

tokens = auth.login('username', 'password')
```

Это вернет словарь с токенами в случае успешной аутентификации. 

В случае ошибки будет выброшено исключение `AuthenticationError`.

## Настройка

Базовый URL API задается в конфигурационном файле `config.ini` в разделе `main` параметром `base_url`.

## Требования

- Python 3.6 и выше
- Библиотека `requests`
- Модуль `configparser`

# Модуль для работы с расчетами
## Mодуль предоставляет класс Calculation для работы с расчетами в системе GLS.

# Использование
Для начала работы нужно создать экземпляр класса Calculation, передав токен доступа:

```
calc = Calculation(access_token)
```
Затем можно вызывать методы:

- `create` - создание нового расчета
- `get` - получение списка расчетов
- `get_by_id` - получение конкретного расчета по id

# Создание расчета
```
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

# Получение расчетов
Чтобы получить список расчетов, вызовите метод get и передайте нужные параметры фильтрации:

```
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

# Получение расчета по id
Для получения конкретного расчета вызовите get_by_id, передав id расчета:

```
calc = calc.get_by_id(12345)
```
Вернется словарь с данными этого расчета.

# Настройка
Базовый URL API задается в config.ini в разделе main параметром base_url.

# Требования
- Python 3.6+
- Requests
- ConfigParser
