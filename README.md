### Test task for everest
_________________________

## Use technology

-   Flask
-   Flask-Admin
-   Flask-Security
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
## Endpoint 

    $ curl -X POST -H "Content-Type: application/json" -d '{
        "jsonrpc": "2.0",
        "method": "order.get_status",
        "params": {"order_id": 15},
        "id": 1
    }' http://localhost:5010/delivery/jsonrpc
______________________________
## TODO 

-   [x]  Создать каталог товаров с характеристиками: цвет, вес, цена.

-   [x]  Отдеть создать адреса доставки с фильтрами по стране, городу, улице. Будет плюсом если реализовать адреса в виде связанного списка

-   [x]  Создать перечень заказов товаров с адресами, кол-вом товаров, и статусами заказов.

-   [x]  Реализовать возможность CRUD операций

-   [ ]  С помощью Celery отсеживать статус заказов и при изменении статуса записывать действие в файл в виде: "ЗАКАЗ %NUM% ИЗМЕНИЛО СТАТУС НА %STATE%"

-   [x]  Создать ендпоинт для полученияи нформации по статусу заказов по номеру заказа. Использовать базовую аутентификацию и JSON-RPC

-   [ ]  Описать все в README.md 

-   [ ]  Реализовать утентификацию в админку

-   [x]  Докеризировать

-   [ ]  Дампик бд

__________________________________

