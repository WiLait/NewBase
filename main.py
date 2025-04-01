#print("word")

from getpass import getpass
from _mysql_connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        printf(connection)
except Error as e:
    printf(e)