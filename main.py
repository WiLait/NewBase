

import mysql.connector
from config import DB_CONFIG
from link import test_connection
#from vir_win import DatabaseTestWindow
from app import f

class DatabaseManager:
    def __init__(self, db_config):
        self.host = db_config['host']
        self.user = db_config['user']
        self.password = db_config['password']
        self.database = db_config['database']
        self.connection = None #Инициализация подключения

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection

if __name__ == "__main__":
    BD_DM = DatabaseManager(DB_CONFIG)
    f()
"""Нужно сделать так чтобы не появлялись ошибки при создании уже созданного БД"""