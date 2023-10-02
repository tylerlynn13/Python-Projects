



from tkinter import *
import tkinter as tk


# make sure to import other modules

import phonebook_gui
import phonebook_func


# Frame is tkinter frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame config.
        self.master = master
        self.master.minsize(500,300) # (height, width)
        self.master.maxsize(500,300)
        # this CenterWindow method will center app on user screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        # this protocol method is a tkinter built-in method to
        # catch if user clicks x on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in GUI widgets from seperate module
        phonebook_gui.load_gui(self)





if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
