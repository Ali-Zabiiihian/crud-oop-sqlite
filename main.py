# DATABASE Operations With OOP
import sqlite3
import tkinter as tk
from data.user_data import get_user_data, get_user_id

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


def user_operation():
    root = tk.Tk()
    root.title("user")
    root.geometry("300x300")

    add = tk.Button(root, text="Add a new user", width=20, bg="lightgreen")
    add.pack(pady=20)
    delete = tk.Button(root, text="Delete a user", width=20, bg="red")
    delete.pack(pady=20)
    find = tk.Button(root, text="Find a user", width=20, bg="lightcoral")
    find.pack(pady=20)
    root.mainloop()


user_operation()