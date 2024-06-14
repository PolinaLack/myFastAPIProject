

from datetime import datetime as dt
from typing import NoReturn

from models.holiday import Holiday_base
from psycopg2 import DatabaseError, IntegrityError
from repositories.Holiday.proto import DateIsBusyError, HolidayIdNotFoundError


class HolidayRepo:
    def __init__(self, postgresql_pool) -> None:
        self.postgresql_pool = postgresql_pool
    
        
    def get_all_holidays(self) -> dict[int, Holiday_base]:
        
        with self.postgresql_pool.getconn() as connection, connection.cursor() as cur:
            cur.execute("SELECT * FROM holis_table;")
            
            response: dict[int, Holiday_base] = {row[0]:
                                                Holiday_base(
                                                user_name = row[1],
                                                start = dt.strftime(row[2], "%d.%m.%Y"),
                                                end_date = dt.strftime(row[3], "%d.%m.%Y")
                                                ) for row in cur.fetchall()}
            return response

    
    def get_holidays_by_user_name(self, user_name) -> dict[int, Holiday_base]:
        
        with self.postgresql_pool.getconn() as connection, connection.cursor() as cur:
            cur.execute("SELECT * FROM holis_table WHERE user_name = %s;",
                        (user_name,))
                
            response: dict[int, Holiday_base] = {row[0]:
                                                Holiday_base(
                                                user_name = row[1],
                                                start = dt.strftime(row[2], "%d.%m.%Y"),
                                                end_date = dt.strftime(row[3], "%d.%m.%Y")
                                                ) for row in cur.fetchall()}
            return response
        
                                              
    def post_holidays(self, holis_in: Holiday_base) -> str | NoReturn: # type: ignore
        try:
            with self.postgresql_pool.getconn() as connection, connection.cursor() as cur:
                cur.execute("INSERT INTO holis_table (user_name, start, end_date) VALUES (%s, %s, %s);",
                            (holis_in.user_name,
                            dt.strptime(holis_in.start, "%d.%m.%Y").date(), 
                            dt.strptime(holis_in.end_date, "%d.%m.%Y").date()
                            ))            
            return str(cur.fetchone())
        
        except DatabaseError as e:
            if e.pgcode == 'P0001':
                raise DateIsBusyError(holis_in=holis_in) from e
                
    
    def put_holidays(self, holis_id: int, holis_in: Holiday_base)-> str | NoReturn: # type: ignore
        try:
            with self.postgresql_pool.getconn() as connection, connection.cursor() as cur:
                cur.execute("""UPDATE holis_table 
                                SET start=%s, end_date=%s
                                WHERE id = %s AND user_name=%s
                                RETURNING *
                                ;""",
                            (dt.strptime(holis_in.start, "%d.%m.%Y").date(), 
                            dt.strptime(holis_in.end_date, "%d.%m.%Y").date(),
                            holis_id,
                            holis_in.user_name,
                            ))            
                return "Error" if cur.fetchall() == [] else "Success"
        
        except IntegrityError as e:
            if e.pgcode == '23505':
                raise HolidayIdNotFoundError(holis_id=holis_id) from e
            
        except DatabaseError as e:
            if e.pgcode == 'P0001':
                raise DateIsBusyError(holis_in=holis_in) from e
    
    
    def delete_holidays(self, holis_id: int, user_name: str)-> str | NoReturn: # type: ignore
        try:
            with self.postgresql_pool.getconn() as connection, connection.cursor() as cur:
                cur.execute("""
                            DELETE FROM holis_table WHERE id = %s AND user_name = %s RETURNING * ;
                            """, (holis_id, user_name))           
            
                return "Error" if cur.fetchall() == [] else "Success"
        
        except IntegrityError as e:
            if e.pgcode == '23505':
                raise HolidayIdNotFoundError(holis_id=holis_id) from e
    
