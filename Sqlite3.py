# Python
# Sqlite3

import sqlite3
from random import randint


global db
global sql
db=sqlite3.connect('Example.db')
sql=db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT)
""")

db.commit()


def reg():
    user_login=input('login:')
    user_password=input('Passowrd:')

    sql.execute(f"SELECT * FROM users WHERE login='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login,user_password,0))
        db.commit()

        print('Зарегестрировано!')
    else:
        print('Такая запись уже есть')

    for value in sql.execute("SELECT * FROM users"):
        print(value)

def casino():
    user_login=input('log in:')
    number=randint(1,2)

    sql.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    if sql.fetchone() is None:
        print("Такого логина не существует.Зарегестрируйтесь")
        reg()
    else:
        if number==1:
            sql.execute(f'UPDATE users SET cash={1000} WHERE login="{user_login}"')
            db.commit()
        else:
            print("вы проиграли")

def enter():
    for i in sql.execute('SELECT login,cash FROM users'):
        print(i)

def main():
    casino()
    enter()

main()
