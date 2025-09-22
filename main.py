import tkinter as tk
from data.user_data import get_user_data, get_user_id
from data.database import user_repo, UserRepository
import datetime

def add_btn():
    root = tk.Tk()
    root.title("Add User")
    root.geometry("300x300")
    name_label = tk.Label(root, text="Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)
    add_button = tk.Button(root, text="Add User", command=lambda: get_user_data(name_entry.get(), email_entry.get()), bg="lightblue")
    add_button.pack(pady=20)
    root.mainloop()





def user_operation():
    root = tk.Tk()
    root.title("user")
    root.geometry("300x600")

    recents_label = tk.Label(root, text="Recent Users:")
    recents_label.pack(pady=5)
    recent_users_list = tk.Listbox(root)
    recent_users_list.pack(pady=5)

    add = tk.Button(root, text="Add a new user", width=20, bg="lightgreen", command=add_btn)
    add.pack(pady=20)
    delete = tk.Button(root, text="Delete a user", width=20, bg="red")
    delete.pack(pady=20)
    update = tk.Button(root, text="Update a user", width=20, bg="coral")
    update.pack(pady=20)
    find = tk.Button(root, text="Find a user", width=20, bg="pink")
    find.pack(pady=20)
    
    root.mainloop()


user_operation()