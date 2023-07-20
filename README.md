# Garpix Load System API SDK

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![GitHub Contributors](https://img.shields.io/github/contributors/NikolayNyunin/Garpix_Load_System-API-SDK)

Это SDK облегчающий взаимодействие с API системы Garpix Load. SDK состоит из нескольких модулей, включая `auth.py` для аутентификации пользователей, `calculation.py` для выполнения различных операций, связанных с вычислениями, и `config.ini` в качестве файла конфигурации.

## Оглавление

- [Установка](#Установка)
- [Аутентификация](#Аутентификация)
- [Модуль для работы с расчетами](#Модуль-для-работы-с-расчетами)
- [Требования](#Требования)
- [Тестирование](#Тестирование)
- [Изменения](#Изменения)
- [Авторы](#Авторы)

## Установка

Для установки SDK используйте pip:

```bash
pip install git+https://github.com/NikolayNyunin/Garpix_Load_System-API-SDK
```

В качестве альтернативы можно клонировать репозиторий и выполнить команду:

```bash
pip install .
```

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

## Требования

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
- Nikolay Nyunin ([NikolayNyunin ↗](https://github.com/NikolayNyunin))
- Bulat Askarov ([BUBLET ↗](https://github.com/BUBLET))


# Garpix Load System API SDK

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![GitHub Contributors](https://img.shields.io/github/contributors/NikolayNyunin/Garpix_Load_System-API-SDK)

This is a Software Development Kit (SDK) that facilitates interaction with the Garpix Load System API. The SDK consists of several modules including `auth.py` for user authentication, `calculation.py` for performing various operations related to calculations, and `config.ini` as a configuration file.

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Calculation Module](#calculation-module)
- [Requirements](#requirements)
- [Testing](#testing)
- [Usage](#usage)
- [Changelog](#changelog)
- [Contributors](#contributors)

## Installation

Use pip to install the SDK as follows:

```bash
pip install git+https://github.com/NikolayNyunin/Garpix_Load_System-API-SDK
```

Alternatively, you can clone the repository and run:

```bash
pip install .
```

## Authentication

The `auth.py` module provides the `login` function for authenticating users through the API and retrieving access tokens.

```python
import auth
tokens = auth.login('username', 'password')
```

This returns a dictionary with tokens upon successful authentication. In case of an error, an `AuthenticationError` exception is thrown.

## Calculation Module

The `calculation.py` module allows you to create, retrieve, and filter calculation records.

Instantiate the `Calculation` class by passing the access token:

```python
calc = Calculation(access_token)
```

You can then call the following methods:

- `create` - Create a new calculation.
- `get` - Retrieve a list of calculations.
- `get_by_id` - Retrieve a specific calculation by id.

For detailed usage, please refer to the [Usage](#usage) section.

## Requirements

- Python 3.6 and above
- Requests library
- configparser module

## Testing

Tests are written in `tests/test_calculation.py` using pytest.

## Usage

```python
from garpix_sdk import login, Calculation

tokens = login('username', 'password')
calc = Calculation(tokens['access_token'])

# Create a calculation
calculation = calc.create(...)

# Retrieve calculations
calculations = calc.get()

# Retrieve a calculation by id
single_calculation = calc.get_by_id(123)
```

## Changelog

_Version 0.1.0:_

- User authentication
- Creation, retrieval, and filtering of calculations

_Planned:_

- Support for multiple API servers
- Token persistence
- Notifications for calculation updates

## Contributors

- Nikolay Nyunin ([NikolayNyunin ↗](https://github.com/NikolayNyunin))
- Bulat Askarov ([BUBLET ↗](https://github.com/BUBLET))

