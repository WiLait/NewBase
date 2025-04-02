
import mysql.connector
from create import create_movies_table
from drop import drop_movies_table
from config import DB_CONFIG


class DatabaseManager:
    def __init__(self, db_config):
        self.host = db_config['host']
        self.user = db_config['user']
        self.password = db_config['password']
        self.database = db_config['database']
        self.connection = None #Инициализация подключения

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Успешно подключено к MySQL")
                return True
            return False
        except mysql.connector.Error as err:
            print(f"Ошибка подключения: {err}")
            return False

    def execute_query(self, query):
        if not self.connection or not self.connection.is_connected():
            print("Ошибка: Нет активного подключения к базе данных.")
            return False

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                return True
        except mysql.connector.Error as err:
            print(f"Ошибка при выполнении запроса: {err}")
            self.connection.rollback()
            return False

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Соединение с базой данных закрыто")


if __name__ == "__main__":
    # Создаем БД с настройками из config.py
    BD_DM = DatabaseManager(DB_CONFIG)

    if BD_DM.connect():

        #create_movies_table(BD_DM)
        #drop_movies_table(BD_DM)

        BD_DM.close()
"""Нужно сделать так чтобы не появлялись ошибки при создании уже созданного БД"""