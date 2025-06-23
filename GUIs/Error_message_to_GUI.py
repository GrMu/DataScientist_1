import tkinter as tk
from tkinter import messagebox

class CustomTk(tk.Tk):
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(val))

def on_button_click():
    raise ValueError("An example exception")

root = CustomTk()
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

root.mainloop()
