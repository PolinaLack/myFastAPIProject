### HolidayChecker
Это приложение помогает согласовать и занести в базу данных отпуска коллег.
Может так же использоваться для любых других расписаний. 

Имеет ограничение пересекающихся интервалов (по умолчанию допускается 3, это можно изменить в файле `scheme/migration_0.sql` в переменной `max_vacation_allowed`)

Для запуска потребуется 
1. установить Docker
2. переименовать `docker-compose copy.yml` в `docker-compose.yml`
3. указать в нем любые значения для этих полей

```   
environment:
      - POSTGRES_USER=
      - POSTGRES_PASSWORD=
      - POSTGRES_DB=
```

4. создать файл  `.env`  и скопировать туда значения переменных по аналогии

```
POSTGRES_USER = 
POSTGRES_PASSWORD = 
POSTGRES_DB = 

POSTGRES_DIALECT_DRIVER = "postgresql+psycopg2"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
```

5. запустить в терминале

```
docker-compose build
```

5. запустить в терминале
```
docker-compose up
```

опробовать endpoint можно будет по адресу http://localhost:8000/docs#/
#
--------------------
#
### HolidayChecker
This application helps to coordinate and record colleagues' vacations in the database. It can also be used for any other schedules.

It has a limitation on overlapping intervals (by default, 3 are allowed; this can be changed in the file `scheme/migration_0.sql` in the variable `max_vacation_allowed`).

To run the application, you need to:

1. Install Docker.
2. Rename `docker-compose copy.yml` to `docker-compose.yml`.
3. Specify any values for these fields in the file:

```   
environment:
      - POSTGRES_USER=
      - POSTGRES_PASSWORD=
      - POSTGRES_DB=
```

4. Create a `.env` file and copy the variable values into it as follows:

```
POSTGRES_USER = 
POSTGRES_PASSWORD = 
POSTGRES_DB = 

POSTGRES_DIALECT_DRIVER = "postgresql+psycopg2"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
```

5. Run the following command in the terminal:

```
docker-compose build
```

6. Run the following command in the terminal:

```
docker-compose up
```

You can test the endpoint at [http://localhost:8000/docs#/](http://localhost:8000/docs#/)
