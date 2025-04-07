import sqlite3
from pathlib import Path


def connect_to_database():
    """Подключение к SQLite базе данных"""
    db_path = Path("C:/Real_estate_agency.db")  # Укажите полный путь если файл в другой папке

    try:
        conn = sqlite3.connect(db_path)
        print("Успешное подключение к базе данных!")
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None


if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        # Проверка подключения - выводим список таблиц
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        print("\nСписок таблиц в базе:")
        for table in tables:
            print(f"- {table[0]}")

        connection.close()