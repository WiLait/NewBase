import mysql.connector
from config import DB_CONFIG

def test_connection():
    """Чистое подключение к MySQL без проверок"""
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Подключение установлено!")
    print("Блинчики установлены")
    return conn  # Возвращаем объект соединения


