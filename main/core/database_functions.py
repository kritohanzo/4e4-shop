import psycopg2
from random import randint
from datetime import datetime

def connect_control(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        connection = psycopg2.connect(
            host="localhost",
            database="project",
            user="postgres",
            password="123456"
        )
        cursor = connection.cursor()
        result = func(cursor = cursor, *args, **kwargs)
        connection.commit()
        connection.close()
        return result
    return wrapper

@connect_control
def register_user(name, email, password, cursor):
    confirm_code = randint(111111, 999999)
    confirmed = False
    cursor.execute(f"""INSERT INTO users_user(name_surname, email, password, confirm_code, confirmed) VALUES('{name}', '{email}', '{password}', {confirm_code}, {confirmed});""")


@connect_control
def login_user(email, password, cursor):
    cursor.execute(f"""SELECT confirmed FROM users_user WHERE email = '{email}' AND password = '{password}';""")
    cursor = cursor.fetchone()
    if cursor:
        if cursor[0]:
            return True
        return False
    return False

@connect_control
def check_confirm_code(username, confirm_code, cursor):
    cursor.execute(f"""SELECT confirm_code FROM users_user WHERE username = '{username}';""")
    cursor = cursor.fetchone()
    db_code = int(cursor[0])
    if int(confirm_code) == db_code:
        return True
    return False

@connect_control
def accept_user(username, cursor):
    cursor.execute(f"""UPDATE users_user SET confirmed = true WHERE username = '{username}';""")


@connect_control
def get_all_objects(table, cursor):
    cursor.execute(f"""SELECT * FROM {table} ORDER BY id;""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results                

get_all_objects('ready_products')