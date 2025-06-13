import customtkinter as ctk
import tkinter as tk
import time

def update():
    columns = ['aaa', 'bbb', 'ccc']
    combo.configure(values=columns)
    combo.set(columns[0])  # Set the first value of the updated list
    combo.update_idletasks()  # Force the GUI to update

initial = ["empty"]
master = tk.Tk()

combo = ctk.CTkComboBox(master, values=initial)
combo.pack(padx=10, pady=10)
combo.set(initial[0])  # Set the initial value

time.sleep(1)
update()

master.mainloop()
