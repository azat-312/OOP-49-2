import sqlite3
connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    fio VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
""")
connect.commit()
# CRUD - Create Reade Update Delete
def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio}, Добавлен")
#add_user('zxzxxz', 32, 'борьба')
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print(f'Список пользователей пуст')
get_all_users()

def del_user(fio):
    cursor.execute('DELETE FROM users WHERE fio=?', (fio,))
    connect.commit()
def get_user_by_name(fio):
    cursor.execute('SELECT * FROM users WHERE fio=?', (fio,))
    users = cursor.fetchall()
    if users:
        print('Список пользователей с заданным ФИО:')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Нет пользователя с таким ФИО.')
def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age=?', (age,))
    users = cursor.fetchall()
    if users:
        print('Список пользователей с заданным возрастом:')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Нет пользователя с таким возрастом.')
get_user_by_age(39)
connect.close() 
