# DATABASE Operations With OOP
import sqlite3

DB_PATH = "database.db"

class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path
    
    # create (C)
    def create(self, user_data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO users (name, email) VALUES (?, ?)"
            cursor.execute(query, (user_data['name'], user_data['email']))

            return cursor.lastrowid

    # select/read (R)
    def find(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = ?"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()

    # update (U)
    def update(self, user_id, user_data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
            cursor.execute(query, (user_data['name'], user_data['email'], user_id))

    # delete (D)
    def delete(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM users WHERE id = ?"
            cursor.execute(query, (user_id,))


user_repo = UserRepository(DB_PATH)