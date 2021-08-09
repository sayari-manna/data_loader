from .db import Connect_To_Db
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import math

class save_data():
    def __init__(self):
        self.file = None

    def create_table(self):
        obj = Connect_To_Db()
        conn = obj.connect()
        c = conn.cursor()
        try:
            c.execute('''DROP TABLE IF EXISTS PRODUCTS''')
            print('table dropped')
            c.execute('''CREATE TABLE PRODUCTS (
                            NAME VARCHAR(50),
                            SKU VARCHAR(100) PRIMARY KEY,
                            DESCRIPTION VARCHAR(1000)
                        )''')
            print('table created')
        finally:
            conn.commit()

    def save_data_using_parallel_ingestion(self,data):
        try:
            list_of_df = []
            self.file = data
            for chunk in pd.read_csv(self.file, chunksize=100000):
                df = chunk
                df.drop_duplicates("sku", keep='last', inplace=True)
                list_of_df.append(df)
            with ThreadPoolExecutor(max_workers=2) as exe:
                exe.map(self.save_chunks, list_of_df)
                exe.shutdown(wait=True)
        finally:
            print('success')

    def save_chunks(self, small_df):
        object_1 = Connect_To_Db()
        con = object_1.connect()
        c = con.cursor()
        try:
            sql_query = '''DELETE FROM PRODUCTS WHERE SKU IN {}'''.format(tuple(small_df['sku']))
            c.execute(sql_query)
            small_df.to_sql('PRODUCTS', con, if_exists='append', index=False, chunksize=100000)

        except Exception as e:
            print(e)
        finally:
            pass
            con.commit()

    def check(self,query):
        obj = Connect_To_Db()
        conn = obj.connect()
        c = conn.cursor()
        try:
            c.execute(query)
            for row in c.fetchall():
                print(row)
        finally:
            conn.commit()

    def create_view(self):
        obj = Connect_To_Db()
        conn = obj.connect()
        c = conn.cursor()
        try:
            c.execute('''DROP TABLE IF EXISTS PRODUCT_COUNT''')
            c.execute('''CREATE TABLE PRODUCT_COUNT (
                                        NAME VARCHAR(50),
                                        COUNT_OF_PRODUCTS INT
                                    )''')
            c.execute('''INSERT INTO PRODUCT_COUNT (NAME,COUNT_OF_PRODUCTS)
                        SELECT NAME,COUNT(*) FROM PRODUCTS
                        GROUP BY NAME''')
        finally:
            conn.commit()

