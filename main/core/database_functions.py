import psycopg2
from random import randint
from datetime import datetime
from core.confirm_code_generator import generate_code

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

@connect_control
def get_all_shoes(cursor):
    cursor.execute(f"""SELECT * FROM public.get_all_shoes();""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results     

@connect_control
def get_all_worker_orders(worker_id, cursor):
    cursor.execute(f"""SELECT * FROM public.get_all_worker_orders({int(worker_id)});""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results     

@connect_control
def get_all_free_orders(cursor):
    cursor.execute(f"""SELECT * FROM public.get_all_free_orders();""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results     

@connect_control
def get_shoe(shoe_id, cursor):
    cursor.execute(f"""SELECT * FROM public.get_shoe({shoe_id});""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results  


@connect_control
def create_order(order_info, client_info, cursor):
    product_id = order_info.get('product_id')
    size = order_info.get('size')
    quanity = order_info.get('quanity')
    type_id = order_info.get('type_id')
    fullname = client_info.get('full_name')
    number = client_info.get('number')
    mail_index = client_info.get('mail_index')
    client_id = client_info.get('client_id')
    time = datetime.now()
    order_ids = []
    for i in range(int(quanity)):
        cursor.execute(
            f""" SELECT public.create_order({int(product_id)}, {int(size)}, '{fullname}', '{number}', '{mail_index}', {int(type_id)}, '{time}', {False}, {int(client_id)});"""
        )
        cursor_result = cursor.fetchone()
        order_ids.append(cursor_result[0])
    return order_ids

@connect_control
def take_order(order_id, worker_id, cursor):
    cursor.execute(f"""SELECT public.take_order({int(order_id)}, {int(worker_id)});""")

@connect_control
def end_order(order_id, worker_id, cursor):
    cursor.execute(f"""SELECT public.end_order({int(order_id)}, {int(worker_id)});""")

@connect_control
def set_confirm_code(username, cursor):
    cursor.execute(f"""SELECT public.set_confirm_code('{username}', {generate_code()});""")
    cursor_result = cursor.fetchone()
    return cursor_result[0]

@connect_control
def get_all_products(cursor):
    cursor.execute(f"""SELECT * FROM public.get_all_products();""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

@connect_control
def get_all_user_orders(user_id, cursor):
    cursor.execute(f"""SELECT * FROM public.get_all_user_orders({int(user_id)});""")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

@connect_control
def add_feedback(user_id, feedback, cursor):
    cursor.execute(f"""INSERT INTO shop_feedback(client_id, feedback) VALUES ({int(user_id)}, '{feedback}');""")
    