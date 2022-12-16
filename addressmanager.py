import tkinter as tk
from tkinter import ttk
from tkinter import *
from datamanager import DataManager
from person import Person
import os

class AddressManager():
    #Constructor:
    def __init__(self, root, data_manager: DataManager):
        #count variable for iid
        self.count = 0

        self._data_manager = data_manager

        #read data from file and write it into self._person_list
        self._person_list = self._data_manager.read_data()

        #displays Headline at the center-top of the window
        self.title_label = ttk.Label(root, text = "Address Management System", font = (None, 40))
        self.title_label.place(x = 175)

        # Data Labels:
        self.name_label = ttk.Label(root, text = "Name:", font = (None, 20), compound = "left")
        self.name_label.place(x = 10, y = 80)

        self.firstname_label = ttk.Label(root, text = "First Name:", font = (None, 20), compound = "left")
        self.firstname_label.place(x = 10, y = 110)

        self.email_address_label = ttk.Label(root, text = "E-Mail:", font = (None, 20), compound = "left")
        self.email_address_label.place(x = 10, y = 140)

        self.birthday_label = ttk.Label(root, text = "Birthday:", font = (None, 20), compound = "left")
        self.birthday_label.place(x = 10, y = 170)

        # Entry Widgets:
        self.name_entry = ttk.Entry(root)
        self.name_entry.place(x = 150, y = 80)

        self.firstname_entry = ttk.Entry(root)
        self.firstname_entry.place(x = 150, y = 110)

        self.email_address_entry = ttk.Entry(root)
        self.email_address_entry.place(x = 150, y = 140)

        self.birthday_entry = ttk.Entry(root)
        self.birthday_entry.place(x = 150, y = 170)

        # Buttons:
        self.add_button = ttk.Button(root, text = "Add", width = 10, command = self.add)
        self.add_button.place(x = 30, y = 220)

        self.Update_button = ttk.Button(root, text = "Update", width = 10, command = self.update)
        self.Update_button.place(x = 170, y = 220)

        self.Delete_button = ttk.Button(root, text = "Delete", width = 10, command = self.delete)
        self.Delete_button.place(x = 310, y = 220)

        # Listbox:
        # Headlines of the table:
        self.columns_tupel = ("Name", "First Name", "E-Mail", "Birthday" )
        self.listBox = ttk.Treeview(root, columns = self.columns_tupel, show = "headings")

        #Formatting the columns of the table
        for col in self.columns_tupel:
            self.listBox.heading(col, text = col)
            self.listBox.grid(row = 1, column = 0, columnspan = 2)
            self.listBox.place(x = 10, y = 300)


        #Defines what happens, when a list record is selected
        self.listBox.bind('<ButtonRelease-1>', self.item_selected)

        self.show()

    @property
    def data_manager(self) -> DataManager:
        return self._data_manager

    @property
    def person_list(self):
        return self._person_list


    #Methods:

    def clear_entry_widgets(self):                      #deletes text out of the entry widgets
        self.name_entry.delete(0, END)
        self.firstname_entry.delete(0, END)
        self.email_address_entry.delete(0, END)
        self.birthday_entry.delete(0, END)



    def add(self):
        #check if each entry widget contains a value
        if (self.check_for_valid_entry()):
        
            #Add the new Person to the end of the person_list
            self._person_list.append(Person(self.name_entry.get(), 
                                    self.firstname_entry.get(), 
                                    self.email_address_entry.get(),
                                    self.transform_birthday(self.birthday_entry.get(), "d"),
                                    self.transform_birthday(self.birthday_entry.get(), "m"),
                                    self.transform_birthday(self.birthday_entry.get(), "y")))

            #Display the new Record
            self.listBox.insert(parent = "", index = END, iid = self.count, text = "", values = (self.name_entry.get(),
                                                                                self.firstname_entry.get(),
                                                                                self.email_address_entry.get(),
                                                                                self.birthday_entry.get()))
            self.count += 1     #increases the count for the next listBox entry/iid

            self.clear_entry_widgets()

    def delete(self):
        #Get record number
        selected_iid = self.listBox.focus()

        #Get index of changed data record
        item_index = self.listBox.index(selected_iid)

        #Remove data from file at index of changed data record
        del self._person_list[item_index]

        #Remove record
        selected_record = self.listBox.selection()[0]
        self.listBox.delete(selected_record)

        self.clear_entry_widgets()

    def update(self):
        #Get record number
        selected_iid = self.listBox.focus()

        #Update record
        self.listBox.item(selected_iid, values = (self.name_entry.get(), 
                                        self.firstname_entry.get(), 
                                        self.email_address_entry.get(), 
                                        self.birthday_entry.get()))

        #Get index of changed data record
        record_index = self.listBox.index(selected_iid)

        #Remove data from file at index of changed data record
        del self._person_list[record_index]

        #Write updated data (at the index of the changed data record) in person_list
        self._person_list.insert(record_index, Person(self.name_entry.get(), 
                                            self.firstname_entry.get(), 
                                            self.email_address_entry.get(), 
                                            self.transform_birthday(self.birthday_entry.get(), "d"),
                                            self.transform_birthday(self.birthday_entry.get(), "m"),
                                            self.transform_birthday(self.birthday_entry.get(), "y")))

        self.clear_entry_widgets()

    def transform_birthday(x, new_birthday, identifier):        #x variable not used
        #returns value of day
        if identifier == "d":
            day = new_birthday[0:2]
            return day
    
        #returns value of month
        elif identifier == "m":
            month = new_birthday[3:5]
            return month
    
        #returns value of year
        elif identifier == "y":
            year = new_birthday[6:10]
            return year
    
        else:
            return "XX"

    def item_selected(e, self):
        #Clear entry widgets
        e.name_entry.delete(0, END)
        e.firstname_entry.delete(0, END)
        e.email_address_entry.delete(0, END)
        e.birthday_entry.delete(0, END)

        #Get record number
        selected_iid = e.listBox.focus()

        #Get record values
        values = e.listBox.item(selected_iid, "values")

        #Ouput to entry widget
        e.name_entry.insert(0, values[0])
        e.firstname_entry.insert(0, values[1])
        e.email_address_entry.insert(0, values[2])
        e.birthday_entry.insert(0, values[3])

    def check_for_valid_entry(self):
        #checks if all entry widgets contain content
        if(len(self.name_entry.get()) != 0 and 
            len(self.firstname_entry.get()) != 0 and  
            len(self.email_address_entry.get()) != 0 and 
            len(self.birthday_entry.get()) != 0):
    
            return True
    
        else:
            #returns a statement in the concole, if atleast one entry widget is empty
            print("You have to enter a value in each entry field!")
            return False

    #displays data at the start of the GUI
    def show(self):
        
        if (os.stat(self._data_manager.filename).st_size != 0):
            for item in self.listBox.get_children():
                self.listBox.delete(item)

            for person in self._person_list:
                self.listBox.insert("", tk.END, values = (str(person._name), str(person._first_name), str(person._email), str(person._day) + "." + str(person._month) + "." + str(person._year)))