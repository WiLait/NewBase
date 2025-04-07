import mysql.connector
from config import DB_CONFIG


def create_empty_database():
    """Создает пустую базу данных (если не существует)"""
    try:
        # Подключаемся без указания базы данных
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()

        # Создаем базу данных (если её нет)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        print(f"База данных '{DB_CONFIG['database']}' готова к использованию")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    create_empty_database()













#"""
#import mysql.connector
#import PySide6
#from config import DB_CONFIG
#
#def create_table():

#    conn = mysql.connector.connect(**DB_CONFIG)
#    cursor = conn.cursor()
    
#    cursor.execute("""
#    CREATE TABLE IF NOT EXISTS sample_data (
#        id INT AUTO_INCREMENT PRIMARY KEY,
#        item_number INT NOT NULL,
#        product_name VARCHAR(100) NOT NULL,
#        price DECIMAL(10, 2) NOT NULL
#    )
#    """)
    
    # Добавляем тестовые данные
#    sample_data = [
 #       (1, 'Ноутбук', 899.99),
  #      (2, 'Смартфон', 599.50),
   #     (3, 'Наушники', 149.99)
    #]
    
 #   cursor.executemany("""
 #   INSERT INTO sample_data (item_number, product_name, price)
  ##  VALUES (%s, %s, %s)
   ## ON DUPLICATE KEY UPDATE
#    product_name = VALUES(product_name),
 #   price = VALUES(price)
  #  """, sample_data)
    
#    conn.commit()
#    cursor.close()
#    conn.close()
#    print("Таблица создана и заполнена тестовыми данными")

#if __name__ == "__main__":
#    create_table() """