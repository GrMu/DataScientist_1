"""from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
print(dir(btn))
print(btn)
#print(btn.keys())
#print(set(btn.configure().keys()))
root.mainloop()
"""
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
# here are method calls to the window manager class
#

root = tk.Tk()
myapp = App(root)
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

myapp.mainloop()