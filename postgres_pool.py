from psycopg2 import pool

try:
    postgresql_pool = pool.SimpleConnectionPool(minconn=1,
                                                maxconn=20,
                                                dbname="postgres",
                                                user="me",
                                                password="qq",
                                                host="localhost",
                                                port="5432",
                                                )

except Exception as e:
    print("Error with psycopg2.connect\n", e)
# finally:
#     if postgresql_pool:
#         postgresql_pool.closeall()
#     print("PostgreSQL closed")    

