import tkinter as tk
from datamanager import DataManager
from addressmanager import AddressManager
from person import Person

root = tk.Tk()                                      #new main-window named root
root.geometry("830x600")                            #sets size of window (recommended "830x600")
root.title("Address Management System")             #sets title in the head of the window
root.resizable(0, 0)                                #window is not resizable -> size can't be changed by dragging with coursor

address_manager = AddressManager(root, DataManager("data.bin"))  #new Object of type AddressManager containing the main window an a DataManager instance as arguments

root.mainloop()                                     #lets tkinter run the application in loop, until window gets closed
address_manager.data_manager.write_data(address_manager.person_list)    #at the end of the program the data gets written indo the data file