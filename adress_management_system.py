import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.geometry("1000x600")
root.title("Address Management System")

title_label = ttk.Label(root, text = "Address Management System", font = (None, 40))
title_label.pack()

name_label = ttk.Label(root, text = "Name:", font = (None, 20), compound = "left")
name_label.place(x = 10, y = 80)

firstname_label = ttk.Label(root, text = "First Name:", font = (None, 20), compound = "left")
firstname_label.place(x = 10, y = 110)

email_address_label = ttk.Label(root, text = "E-Mail:", font = (None, 20), compound = "left")
email_address_label.place(x = 10, y = 140)

birthday_label = ttk.Label(root, text = "Birthday:", font = (None, 20), compound = "left")
birthday_label.place(x = 10, y = 170)

root.mainloop()
