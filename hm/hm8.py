
import sqlite3
connect = sqlite3.connect('users.db')
cursor = connect.cursor()
# Создание базы данных и таблиц с различными связями
# Один к одному, Один ко многим, Многие к одному, Многие ко многим
# Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор пользователя
                fio VARCHAR(100) NOT NULL,                -- ФИО пользователя
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')
    # Создание таблицы 'grades'
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор записи о оценке
                userid INTEGER,                            -- Внешний ключ, который ссылается на userid из таблицы 'users'
                subject VARCHAR(100) NOT NULL,             -- Название предмета
                grade INTEGER NOT NULL,                    -- Оценка
                FOREIGN KEY (userid) REFERENCES users(userid) -- Определяем связь с таблицей 'users'
            )
        ''')
    connect.commit()
create_db()
# CRUD - Create Read Update Delete
def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")
#add_user(' ким ', 21, 'фехтование')
#add_user('йохан', 17, 'копирование')
#add_user('гон', 20, 'карате')
#add_user('васко', 18, 'муай-тай')
#add_user('сину', 20, 'быстрые атаки')
#add_user('хобин', 19, 'кудо')
def delete_user_by_id(user_id):
    cursor.execute('DELETE FROM users WHERE userid = ?', (user_id,))
    connect.commit()
    print(f"Пользователь с ID {user_id} удален")
# delete_user_by_id(3)
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print("Список пользователей пуст")
# get_all_users()
def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()
    print(f"Пользователи с возрастом {age}:")
    for user in users:
        print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
# get_user_by_age(25)
def update_user_age_by_id(user_id, fio):
    cursor.execute('UPDATE users SET fio = ? WHERE userid = ?', (fio, user_id))
    connect.commit()
    print(f"ФИО пользователя с ID {user_id} обновлено")
# update_user_age_by_id(4, "Арзыбек Абды")
# get_all_users()
def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)', (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}")
#add_grade(1, "Алгебра", 4)
#add_grade(2, "Геометрия", 5)
#add_grade(3, "Физика", 5)
def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    INNER JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    print("Пользователи с их оценками:")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, SUBJECT: {row[2]}, GRADE: {row[3]}")
def get_users_with_left_join():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    LEFT JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    print("Пользователи с их оценками (LEFT JOIN):")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, SUBJECT: {row[2]}, GRADE: {row[3]}")
# Агрегационные функции и группировка данных
def get_average_age():
    cursor.execute('SELECT SUM(age) FROM users')
    avg_age = cursor.fetchone()[0]
    print(f"Средний воозраст юзера {avg_age}")

#Вложенные запросы
def get_users_with_highest_grade():
    cursor.execute("""
        SELECT fio, subject, grade
        FROM users JOIN grades ON users.userid = grades.userid
        WHERE grade = (SELECT MAX(grade) FROM grades)
    """)
    users = cursor.fetchall()
    print(f"Пользователи с максимальным баллом")
    for i in users:
        print(f"FIO: {i[0]}, SUB: {i[1]}, GR: {i[2]}")
print(f"--------Вложенные запросы---------")
get_users_with_highest_grade()
# Views (Представления)
def create_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_view AS
        SELECT fio, age, hobby
        FROM users
        WHERE age < 20
    """)
    connect.commit()
    print("Представление user_view создано")
def get_young_users():
    cursor.execute('SELECT * FROM user_view')
    young_users = cursor.fetchall()
    print("Молодые пользователи (моложе 20 лет):")
    for user in young_users:
        print(f"FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    create_users_view()
    get_young_users
    user = cursor.fetchall()
    print("молодые пользователи")
print('наше Views (Представления)')
create_users_view()
get_young_users()

def create_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_view AS
        SELECT fio, age, hobby
        FROM users
        WHERE age < 20
    """)
    connect.commit()
    print("Представление user_view создано")
def get_grade_statistics():
    cursor.execute('''
    SELECT subject, AVG(grade) as avg_grade, MAX(grade) as max_grade, MIN(grade) as min_grade
    FROM grades
    GROUP BY subject
    ''')
    stats = cursor.fetchall()
    print(f"Статистика по Оценкам: \n")
    print(stats)
    for stat in stats:
        print(f"SUBJECT: {stat[0]}, AVG: {stat[1]}, MAX: {stat[2]}, MIN: {stat[3]}")
print("\n--- Агрегационные функции ---")
get_average_age()
get_grade_statistics()
def get_statistic():
    cursor.execute("""
    SELECT subject, COUNT(grade) as count_grade, SUM(grade) as sum_grade
    FROM grades
    GROUP BY subject
""")
    mrak = cursor.fetchall()
    print(f"общая оценка и количество строк: \n")
    print(mrak)
    for mark in mrak:
        print(f"SUBJECT: {mark[0]}, COUNT: {mark[1]}, SUM: {mark[2]}")
get_statistic()