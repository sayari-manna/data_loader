import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connect_To_Db():

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect('test.db',timeout=40)
        print("Processing......")
        return self.conn