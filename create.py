"""
import mysql.connector

def create_movies_table(BD_DM):
        create_movies_table_query =
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mill INT
        )

        # Используем метод execute_query из db_manager
        success = BD_DM.execute_query(create_movies_table_query)
        if success:
            print("Таблица 'movies' успешно создана!")
            return True
        return False

    except Exception as err:
        print(f"Ошибка создания таблицы: {err}")
        return False
"""
