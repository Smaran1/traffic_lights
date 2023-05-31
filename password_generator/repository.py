#Creating connection with the local postgres
import psycopg2
import os


class pg_rep():
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.logger = None
        super().__init__()

    def connect(self) -> object:
        pg_conn = os.getenv("LOCAL_POSTGRES")    
        if self.connection is None:
            self.connection = psycopg2.connect(pg_conn)
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True
            return self.connection
