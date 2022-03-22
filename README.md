
##  Hammer Systems API

### Описание
Тестовое задание REST API компании Hammer Systems.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Стек технологий:
проект написан на Python с использованием Django REST Framework
библиотека Simple JWT - работа с JWT-токеном
система управления версиями - git
Запуск проекта
Клонируйте репозитроий с проектом:
git clone https://github.com/Belinskii1/hammer_systems_task.git

В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

Выполните миграции:

python manage.py migrate

Создайте суперпользователя:
python manage.py createsuperuser

Запустите сервер:
python manage.py runserver

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация (redoc.yaml) доступна по адресу http://localhost:8000/redoc/

С помощью команды pytest вы можете запустить тесты и проверить работу модулей

#### 1. Аутентификация.
Выполните POST-запрос http://localhost:8000/api/v1/auth/signup/ передав мобильный номер телефона.

API вернет 4х значный код в формате:  
`{`    
    `"Ваш код активации": "1234"`    
`}`    

Далее выполните POST-запрос http://localhost:8000/api/v1/auth/code/ передав ранее полученный код.

API вернет 6х значный инвайт код, а так же токен в формате:  
`{`  
     `"Ваш токен": "b2ov41-e29fb6245d5923f50fd9859356c75379",`    
     `"Ваш инвайт код": "Q9UK59"`  
`}`  

#### 2. Получение данных о пользователе.

Выполните POST или GET-запрос http://localhost:8000/api/v1/users/.

API вернет информацию о пользователя в следующем формате:

`[`  
    `{`  
        `"first_name": "",`  
        `"last_name": "",`  
        `"username": "admin",`  
        `"telephone_number": "89298284301",`  
        `"invite_code": "",`  
        `"invite_code_list": []`  
    `},`  
    `{`  
        `"first_name": "",`  
        `"last_name": "",`  
        `"username": "",`  
        `"telephone_number": "89298284302",`  
        `"invite_code": "",`  
        `"invite_code_list": []`  
    `}`  
`]`  


Для получения информации профиля и его редактирования выполните POST или GET-запрос http://localhost:8000/api/v1/users/{username}/.

API вернет информацию о пользователя в следующем формате:

`{`   
    `"first_name": "",`  
    `"last_name": "",`  
    `"username": "admin",`  
    `"telephone_number": "89298284301",`  
    `"invite_code": "",`  
    `"invite_code_list": []`  
`}` 
