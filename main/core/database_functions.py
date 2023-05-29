import psycopg2
from random import randint

def connect_control(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123123"
        )
        cursor = connection.cursor()
        func(cursor = cursor, *args, **kwargs)
        connection.commit()
        connection.close()
    return wrapper

@connect_control
def register_user(name, email, password, cursor):
    confirm_code = randint(111111, 999999)
    confirmed = False
    cursor.execute(f"""INSERT INTO users_user(name_surname, email, password, confirm_code, confirmed) VALUES('{name}', '{email}', '{password}', {confirm_code}, {confirmed});""")
