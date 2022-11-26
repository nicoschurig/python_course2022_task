import tkinter as tk
import pickle
from tkinter import ttk, messagebox
from tkinter import *
from tkinter.messagebox import showinfo
import os

# ================================= Classes ======================================================
class Person():
    def __init__(self, name, first_name, email, day, month, year):
        self._name = name
        self._first_name = first_name
        self._email = email
        self._day = day
        self._month = month
        self._year = year

# ================================ Functions ===================================================
person_list = []

if (os.stat("data.bin").st_size != 0):
    person_pickle = open("data.bin", "rb")
    person_list = pickle.load(person_pickle)
    person_pickle.close()

def add():
    
    if (len(name_entry.get()) != 0 and 
        len(firstname_entry.get()) != 0 and  
        len(email_address_entry.get()) != 0 and 
        len(birthday_entry.get()) != 0):
        
        new_birthday = birthday_entry.get()
        new_day = str(new_birthday[0:2])
        new_month = str(new_birthday[3:5])
        new_year = str(new_birthday[6:10])
        person_list.append(Person(str(name_entry.get()), str(firstname_entry.get()), str(email_address_entry.get()), new_day, new_month, new_year))

        person_pickle = open("Data.bin", "wb")
        pickle.dump(person_list, person_pickle)
        person_pickle.close()

        show()

        name_entry.delete(0, 'end')
        firstname_entry.delete(0, 'end')
        email_address_entry.delete(0, 'end')
        birthday_entry.delete(0, 'end')

    else:
        print("You have to enter a value in each entry field!")

def delete(): 

    selected_iid = listBox.focus()
    item_index = listBox.index(selected_iid)

    del person_list[item_index]

    person_pickle = open("Data.bin", "wb")
    pickle.dump(person_list, person_pickle)
    person_pickle.close()

    show()

def show():
    if (os.stat("data.bin").st_size != 0):
        person_pickle = open("data.bin", "rb")
        person_list = pickle.load(person_pickle)
        person_pickle.close()

        for item in listBox.get_children():
            listBox.delete(item)

        for person in person_list:
            listBox.insert("", tk.END, values = (str(person._name), str(person._first_name), str(person._email), str(person._day) + "." + str(person._month) + "." + str(person._year)))



# ================================== GUI =======================================================
root = tk.Tk()
root.geometry("830x600")
root.title("Address Management System")
root.resizable(0, 0)

title_label = ttk.Label(root, text = "Address Management System", font = (None, 40))
title_label.place(x = 175)

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
add_button = ttk.Button(root, text = "Add", width = 10, command = add)
add_button.place(x = 30, y = 220)

Update_button = ttk.Button(root, text = "Update", width = 10)
Update_button.place(x = 170, y = 220)

Delete_button = ttk.Button(root, text = "Delete", width = 10, command = delete)
Delete_button.place(x = 310, y = 220)

# Listbox
columns_tupel = ("Name", "First Name", "E-Mail", "Birthday" )
listBox = ttk.Treeview(root, columns = columns_tupel, show = "headings")


for col in columns_tupel:
    listBox.heading(col, text = col)
    listBox.grid(row = 1, column = 0, columnspan = 2)
    listBox.place(x = 10, y = 300)

def item_selected(event):
    for selected_item in listBox.selection():
        item = listBox.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

listBox.bind('<<TreeviewSelect>>', item_selected)

show()  



root.mainloop()
