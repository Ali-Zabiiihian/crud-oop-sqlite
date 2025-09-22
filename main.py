import tkinter as tk
from tkinter import messagebox
from database.database import UserRepository, DB_PATH


def add_btn(update_listbox_callback=None):
    root = tk.Tk()
    root.title("Add User")
    root.geometry("300x500")
    root.configure(bg='#f0f0f0')  # Light grey background
    name_label = tk.Label(root, text="Name:", bg='#f0f0f0')
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
            error_label = tk.Label(root, text="Please enter name and email", fg="red", bg='#f0f0f0')
            error_label.pack(pady=5)
            return
        user_id = user_repo.create({"name": name, "email": email})
        if user_id:
            success_label = tk.Label(root, text="User added successfully! (id={})".format(user_id), fg="green", bg='#f0f0f0')
            success_label.pack(pady=5)
            # clear fields after successful add
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            # update the main window's listbox
            if update_listbox_callback:
                update_listbox_callback()
            # close the add window after 1 second
            root.after(1000, root.destroy)

    add_button = tk.Button(root, text="Add User", command=on_add, bg="lightblue")
    add_button.pack(pady=20)

    root.mainloop()


def delete_user():
    root = tk.Tk()
    root.title("Delete User")
    root.geometry("300x200")
    root.configure(bg='#f0f0f0')  # Light grey background
    label = tk.Label(root, text="Enter User ID to delete:", bg='#f0f0f0')
    label.pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    user_repo = UserRepository(DB_PATH)

    def on_delete():
        user_id = entry.get().strip()
        if not user_id:
            error_label = tk.Label(root, text="Please enter a user ID", fg="red", bg='#f0f0f0')
            error_label.pack(pady=5)
            return
        user_repo.delete(user_id)
        success_label = tk.Label(root, text="User deleted successfully!", fg="green")
        success_label.pack(pady=5)

    delete_button = tk.Button(root, text="Delete User", command=on_delete, bg="lightcoral")
    delete_button.pack(pady=20)

    root.mainloop() 


def clear_database(refresh_callback=None):
    root = tk.Tk()
    root.title("Clear Database")
    root.geometry("300x200")
    root.configure(bg='#f0f0f0')  # Light grey background
    
    warning_label = tk.Label(root, text="⚠️ Warning: This will delete ALL users!", fg="red", bg='#f0f0f0')
    warning_label.pack(pady=10)
    
    user_repo = UserRepository(DB_PATH)
    
    def on_clear():
        confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to delete ALL users?\nThis cannot be undone!")
        if confirm:
            user_repo.clear_all()
            success_label = tk.Label(root, text="Database cleared successfully!", fg="green")
            success_label.pack(pady=5)
            if refresh_callback:
                refresh_callback()
            root.after(2000, root.destroy)  # close window after 2 seconds
        
    clear_button = tk.Button(root, text="Clear All Data", command=on_clear, bg="red", fg="white")
    clear_button.pack(pady=20)
    
    cancel_button = tk.Button(root, text="Cancel", command=root.destroy)
    cancel_button.pack(pady=10)
    
    root.mainloop()

def user_operation():
    root = tk.Tk()
    root.title("User Management")
    root.geometry("300x600")
    root.configure(bg='#f0f0f0')  # Light grey background

    # Create frame for users list
    list_frame = tk.Frame(root, bg='#f0f0f0')
    list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    recents_label = tk.Label(list_frame, text="Recent Users:", bg='#f0f0f0')
    recents_label.pack(pady=5)
    
    recent_users_list = tk.Listbox(list_frame, width=40, height=10)
    recent_users_list.pack(fill=tk.BOTH, expand=True, pady=5)
    
    user_repo = UserRepository(DB_PATH)
    
    def refresh_users_list():
        recent_users_list.delete(0, tk.END)  # Clear current list
        users = user_repo.get_all_users()
        for user in users:
            recent_users_list.insert(tk.END, f"{user[1]} (ID: {user[0]})")  # Display name and ID
    
    # Initial population of the list
    refresh_users_list()
    
    # Button frame
    button_frame = tk.Frame(root, bg='#f0f0f0')
    button_frame.pack(fill=tk.X, padx=10, pady=5)
    
    add = tk.Button(button_frame, text="Add a new user", width=20, bg="lightgreen", 
                   command=lambda: add_btn(refresh_users_list))
    add.pack(pady=10)
    
    delete = tk.Button(button_frame, text="Delete a user", width=20, bg="red", 
                      command=delete_user)
    delete.pack(pady=10)
    
    update = tk.Button(button_frame, text="Update a user", width=20, bg="coral")
    update.pack(pady=10)
    
    find = tk.Button(button_frame, text="Find a user", width=20, bg="pink")
    find.pack(pady=10)
    
    clear = tk.Button(button_frame, text="Clear Database", width=20, bg="darkred", 
                     fg="white", command=lambda: clear_database(refresh_users_list))
    clear.pack(pady=10)
    
    root.mainloop()


user_operation()