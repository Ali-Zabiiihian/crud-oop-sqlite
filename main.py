import tkinter as tk
from tkinter import messagebox
from database.database import UserRepository, DB_PATH


def add_btn():
    root = tk.Tk()
    root.title("Add User")
    root.geometry("300x500")
    name_label = tk.Label(root, text="Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    user_repo = UserRepository(DB_PATH)

    def on_add():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        # basic validation
        if not name or not email:
            error_label = tk.Label(root, text="Please enter name and email", fg="red")
            error_label.pack(pady=5)
            return
        user_id = user_repo.create({"name": name, "email": email})
        if user_id:
            success_label = tk.Label(root, text="User added successfully! (id={})".format(user_id), fg="green")
            success_label.pack(pady=5)
            # clear fields after successful add
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)

    add_button = tk.Button(root, text="Add User", command=on_add, bg="lightblue")
    add_button.pack(pady=20)

    root.mainloop()


def delete_user():
    root = tk.Tk()
    root.title("Delete User")
    root.geometry("300x200")
    label = tk.Label(root, text="Enter User ID to delete:")
    label.pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    user_repo = UserRepository(DB_PATH)

    def on_delete():
        user_id = entry.get().strip()
        if not user_id:
            error_label = tk.Label(root, text="Please enter a user ID", fg="red")
            error_label.pack(pady=5)
            return
        user_repo.delete(user_id)
        success_label = tk.Label(root, text="User deleted successfully!", fg="green")
        success_label.pack(pady=5)

    delete_button = tk.Button(root, text="Delete User", command=on_delete, bg="lightcoral")
    delete_button.pack(pady=20)

    root.mainloop() 


def clear_database():
    root = tk.Tk()
    root.title("Clear Database")
    root.geometry("300x200")
    
    warning_label = tk.Label(root, text="⚠️ Warning: This will delete ALL users!", fg="red")
    warning_label.pack(pady=10)
    
    user_repo = UserRepository(DB_PATH)
    
    def on_clear():
        confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to delete ALL users?\nThis cannot be undone!")
        if confirm:
            user_repo.clear_all()
            success_label = tk.Label(root, text="Database cleared successfully!", fg="green")
            success_label.pack(pady=5)
            root.after(2000, root.destroy)  # close window after 2 seconds
        
    clear_button = tk.Button(root, text="Clear All Data", command=on_clear, bg="red", fg="white")
    clear_button.pack(pady=20)
    
    cancel_button = tk.Button(root, text="Cancel", command=root.destroy)
    cancel_button.pack(pady=10)
    
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
    delete = tk.Button(root, text="Delete a user", width=20, bg="red", command=delete_user)
    delete.pack(pady=20)
    update = tk.Button(root, text="Update a user", width=20, bg="coral")
    update.pack(pady=20)
    find = tk.Button(root, text="Find a user", width=20, bg="pink")
    find.pack(pady=20)
    clear = tk.Button(root, text="Clear Database", width=20, bg="darkred", fg="white", command=clear_database)
    clear.pack(pady=20)
    
    root.mainloop()


user_operation()