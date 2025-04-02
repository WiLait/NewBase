
import mysql.connector

def drop_movies_table(BD_DM):
    """Удаляет таблицу 'movies', если она существует."""
    try:
        drop_movies_table_query = "DROP TABLE IF EXISTS movies"
        success = BD_DM.execute_query(drop_movies_table_query)
        if success:
            print("Таблица 'movies' успешно удалена!")
            return True
        return False

    except Exception as err:
        print(f"Ошибка удаления таблицы: {err}")
        return False

