### Test task for everest
_________________________

## Use technology

-   Flask
-   Flask-Admin
-   SQLAlchemy
-   Celery
-   Redis
-   Mysql/MariaDB ?
-   Docker

___________________________

### HOW TO RUN IT

-   Easy as it can be:

    `$ docker-compose -f local.yml build --no-cache`

    `$ docker-compose -f local.yml up`

-   If you need something from `flask cli` in docker just run something like this:

    `$ docker-compose -f local.yml run web flask db init`
____________________________

## TODO 

-   [x]  Создать каталог товаров с характеристиками: цвет, вес, цена

-   [x]  Отдельно создать адреса доставки с фильтрами по стране, городу, улице. Будет плюсом если реализовать адрсса в виде связанного списка.

-   [ ]  Создать список заказов товаров с адресами, кол-во товаров и статусами(выполнено, отменено, обробатывается)

-   [x]  Реализовать возможность CRUD операций

-   [ ]  С помощью Celery отсеживать статус заказов и при изменении статуса записывать действие в файл в виде: "ЗАКАЗ %NUM% ИЗМЕНИЛО СТАТУС НА %STATE%"

-   [ ]  Создать ендпоинт для полученияи нформации по статусу заказов по номеру заказа. Использовать базовую аутентификацию и JSON-RPC

-   [ ]  Опиисать все в README.md 

-   [ ]  Реализовать утентификацию в админку

-   [x]  Докеризировать

-   [ ]  Дампик бд

__________________________________
