import tkinter as tk
from tkinter import messagebox

def klik():
    print("Geklikt")
    messagebox.showerror("Gevaar", "Dit mocht niet")
root = tk.Tk()
root.title("eerste GUI")
root.geometry("1200x800")
root.minsize(300,200)
root.bell()
button_klik = tk.Button(root, text="Klik", command=klik).pack()
Naam_labl = tk.Label(root, text="Naam")
Naam_labl.pack()
Leef_labl = tk.Label(root, text="Leeftijd")
Leef_labl.pack()
input_naam=tk.Entry(root)
input_naam.pack()

# root.iconphoto()
root.mainloop()
