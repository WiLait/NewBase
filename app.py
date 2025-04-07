import sqlite3
from pathlib import Path

#  Измените путь к файлу
db_path = Path("C:/Users/User/Documents/Real_estate_agency.db")

con = sqlite3.connect(db_path)

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT, year INTEGER, score REAL)") # Добавил IF NOT EXISTS и типы данных
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

# Проверка существования таблицы
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='movie'")
table_exists = cur.fetchone()

if table_exists:
    print("Таблица 'movie' существует.")

    # Проверка наличия данных в таблице
    cur.execute("SELECT COUNT(*) FROM movie")
    row_count = cur.fetchone()[0]

    if row_count > 0:
        print(f"В таблице 'movie' есть {row_count} строк.")

        # Вывод данных из таблицы (опционально)
        cur.execute("SELECT * FROM movie")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("В таблице 'movie' нет данных.")
else:
    print("Таблица 'movie' не существует.")

con.close()
