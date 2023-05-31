#Connecting python with postgres locally
import os

from psycopg2 import connect
from repository import pg_rep

class pgrepo(pg_rep):
    def __init__(self) -> None:
        super().__init__()
     
    
    def insert_passwords(self,site, password):
        with connect(os.getenv("LOCAL_POSTGRES") ) as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    sql_query = f"""
                                INSERT INTO pass_gen(
                                site,
                                password
                                )
                            VALUES(site, password) 

                            """
                    
                    try:
                         cur.execute(sql_query,
                                     (site,
                                      password) 
                                     )

                    except Exception as e:
                        print(e)     










