import sqlite3

from models.db import read_admin

def insert_admin(username: str, hashed_password, is_admin):
    conn = sqlite3.connect("models/base.db")
    cursor = conn.cursor()


    cursor.execute("INSERT INTO admin (username, password, is_admin) VALUES (?, ?, ?)", (username, hashed_password, is_admin))
    conn.commit()

insert_admin("User", "aaaa", True)