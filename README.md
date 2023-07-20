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
## Vодуль предоставляет класс Calculation для работы с расчетами в системе GLS.

# Использование
Для начала работы нужно создать экземпляр класса Calculation, передав токен доступа:

```
calc = Calculation(access_token)
```
Затем можно вызывать методы:

- create - создание нового расчета
- get - получение списка расчетов
- get_by_id - получение конкретного расчета по id

# Создание расчета
```
calc.create(
  project_id=123,
  input_data={'param1': 'value1'},
  status='new'  
)
```
На вход принимаются:

`project_id` - id проекта
`input_data` - входные данные для расчета
`status` - статус расчета
Также можно указать:

`callback_url` - url для callback
`external_api` - признак использования внешнего api

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

`favorite` - избранные расчеты
`is_history` - исторические расчеты
`is_recalculate` - пересчитанные
`ordering` - сортировка
`page` - номер страницы
`page_size` - размер страницы
`project_id` - id проекта
`status` - статус

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
