# DATABASE Operations With OOP
import sqlite3
from user_data.user_data import get_user_data, get_user_id

DB_PATH = "database.db"

class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

    # create (C)
    def create(self, user_data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO users (name, email) VALUES (?, ?)"
            cursor.execute(query, (user_data['name'], user_data['email']))
            conn.commit()
            return cursor.lastrowid
        conn.close()

    # select/read (R)
    def find(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = ?"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()
        conn.close()

    # update (U)
    def update(self, user_id, user_data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
            cursor.execute(query, (user_data['name'], user_data['email'], user_id))
            conn.commit()
            conn.close()

    # delete (D)
    def delete(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM users WHERE id = ?"
            cursor.execute(query, (user_id,))
            conn.commit()

    # clear all records
    def clear_all(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM users"
            cursor.execute(query)
            conn.commit()
            return True

