#Connecting python with postgres locally
import os

from psycopg2 import connect
from repository import pg_rep

class pgrepo(pg_rep):
    def __init__(self) -> None:
        super().__init__()
     
     
    
    def insert_passwords(self, pass_):

        with connect(self.pg_conn) as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    sql_query = f"""
                                INSERT INTO pass_gen(pass_) VALUES(%s) 

                            """
                    
                    try:
                        cur.execute(sql_query,
                                     (
                                      pass_) 
                                     )

                    except Exception as e:
                        print(e)     










