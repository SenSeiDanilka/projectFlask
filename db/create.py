import sqlite3
from os import path

absPath = path.join(path.dirname(path.dirname(__file__)), "base.db")
print(absPath)

connection = sqlite3.connect(absPath)
cursor = connection.cursor()

cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, title TEXT, price REAL, desc TEXT, image TEXT)")
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        login TEXT UNIQUE,
        password TEXT,
        admin INTEGER
    )
''')

dataProducts = [
    (1, "Солнцезащитыные очки", 300.00, "Защищают от солнца", "/static/img/glasses1.png"),
    (2, "Медицинские очки", 4000.00, "Улучшают зрение", "/static/img/glasses2.png"),
    (3, "Компьютерные очки", 1200.00, "Защищают от синего спектра", "/static/img/glasses3.png"),
]

# 0 - это обычный клиент сайта
# 1 - это сотрудник сайта, компании
# 2 - главный менеджер
dataUsers = [
    (1, "Олег Корпатович", "1234567890", 1),
    (2, "Владимир Центральный", "admin", 2)
]

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", dataProducts)
cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", dataUsers)
connection.commit()

connection.close()
