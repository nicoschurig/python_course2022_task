import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

# ================================= Class ======================================================
class Person():
    def __init__(self, name, first_name, email, day, month, year):
        self._name = name
        self._first_name = first_name
        self._email = email
        self._day = day
        self._month = month
        self._year = year


# ================================== GUI =======================================================
root = tk.Tk()
root.geometry("1000x600")
root.title("Address Management System")

title_label = ttk.Label(root, text = "Address Management System", font = (None, 40))
title_label.pack()

# Data Labels:
name_label = ttk.Label(root, text = "Name:", font = (None, 20), compound = "left")
name_label.place(x = 10, y = 80)

firstname_label = ttk.Label(root, text = "First Name:", font = (None, 20), compound = "left")
firstname_label.place(x = 10, y = 110)

email_address_label = ttk.Label(root, text = "E-Mail:", font = (None, 20), compound = "left")
email_address_label.place(x = 10, y = 140)

birthday_label = ttk.Label(root, text = "Birthday:", font = (None, 20), compound = "left")
birthday_label.place(x = 10, y = 170)

# Entry Widgets:
name_entry = ttk.Entry(root)
name_entry.place(x = 150, y = 80)

firstname_entry = ttk.Entry(root)
firstname_entry.place(x = 150, y = 110)

email_address_entry = ttk.Entry(root)
email_address_entry.place(x = 150, y = 140)

birthday_entry = ttk.Entry(root)
birthday_entry.place(x = 150, y = 170)

# Buttons:
add_button = ttk.Button(root, text = "Add", width = 10)
add_button.place(x = 30, y = 220)

Update_button = ttk.Button(root, text = "Update", width = 10)
Update_button.place(x = 170, y = 220)

Delete_button = ttk.Button(root, text = "Delete", width = 10)
Delete_button.place(x = 310, y = 220)

root.mainloop()
