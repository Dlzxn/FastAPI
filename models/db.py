import sqlite3

def insert_post(title, link, description):
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()


    cursor.execute("INSERT INTO posts (title, link, descriptions) VALUES (?, ?, ?)", (title, link, description))
    conn.commit()

def read_posts() -> list:
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    users = cursor.fetchall()
    first_ten = []
    for user in users:
        first_ten.append({"title": user[0], "link": user[1], "descriptions": user[2]})

    conn.close()
    return first_ten


def insert_project(title, description, link, download):
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO projects (title, descriptions, link, download) VALUES ( ?, ?, ?, ?)",
                   (title, description, link, download))
    conn.commit()


def read_project() -> list:
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    users = cursor.fetchall()
    first_ten = []
    for user in users:
        first_ten.append({"id": user[0], "title": user[1], "descriptions": user[2], "link": user[3], "download": user[4]})

    conn.close()
    return first_ten


def read_admin() -> list:
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin")
    users = cursor.fetchall()
    first_ten = []
    for user in users:
        first_ten.append({"username": user[0], "pswd": user[1], "is_admin": user[2]})

    conn.close()
    return first_ten
