#print("word")

from getpass import getpass
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="127.15.15.15",
        user="root",
        password="/intriga/xaxaE6",
        database="test"
    )
    if mydb.is_connected():
        print("Успешно подключено к MySQL")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT VERSION()")
        version =mycursor.fetchall()
        print("Версия MySQL:", version)

        # Создание таблицы
        try:
            create_movies_table_query = """
            CREATE TABLE movies(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100),
                release_year YEAR(4),
                genre VARCHAR(100),
                collection_in_mill INT
            )
            """
            with mydb.cursor() as cursor:
                cursor.execute(create_movies_table_query)
                mydb.commit()
                print("Таблица 'movies' успешно создана!")

        except mysql.connector.Error as err:
            print(f"Ошибка создание таблицы: {err}")


except mysql.connector.Error as err:
    print(f"Ошибка подключения: {err}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Соединение с базой данных закрыто")


