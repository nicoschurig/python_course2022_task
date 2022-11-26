import tkinter as tk
from tkinter import ttk


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


root.mainloop()
