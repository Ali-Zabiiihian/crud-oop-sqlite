import tkinter as tk
from data.user_data import get_user_data, get_user_id
from data.database import user_repo, UserRepository

def user_operation():
    root = tk.Tk()
    root.title("user")
    root.geometry("300x300")

    add = tk.Button(root, text="Add a new user", width=20, bg="lightgreen")
    add.pack(pady=20)
    delete = tk.Button(root, text="Delete a user", width=20, bg="red")
    delete.pack(pady=20)
    find = tk.Button(root, text="Find a user", width=20, bg="pink")
    find.pack(pady=20)
    update = tk.Button(root, text="Update a user", width=20, bg="lightcoral")
    update.pack(pady=20)
    root.mainloop()


user_operation()