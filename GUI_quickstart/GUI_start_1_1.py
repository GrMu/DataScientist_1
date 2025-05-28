import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import time

imgpath = "../GUIs/images/smiley3.png"

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter", background="#34A2FE", foreground='purple', width=10, height=5)
greeting.pack()
greeting2 = ttk.Label(text="Hello, TTkinter", background='#F08080', foreground='#581845', width=20)
greeting2.pack()

# image = ImageTk.PhotoImage(Image.open(r'imgpath'))
image = ImageTk.PhotoImage(file=imgpath)
tctimg = tk.Label(text=' Hello', image=image, compound='left').pack()

button_tk = tk.Button(text='Hello').pack()
button_ttk = ttk.Button(text='Hello').pack()
button_img_ttk = ttk.Button(text='Hello', image=image, compound='left').pack()
emptyline = tk.Label(text='').pack()
entrylabel = tk.Label(text='Name: ')
entrylabel.pack()
entry = tk.Entry(fg="grey", bg="lightgrey", width=50)
entry.insert(0, "Python")
entry.pack()
entry['foreground'] = "darkblue"
entry_ttk = ttk.Entry(foreground="darkblue", background="lightgrey", width=50).pack()


text_box = tk.Text()
text_box.insert("1.0", "Hoh hoi")
text_box.pack()
hulp = text_box.get("1.0", tk.END)
entrylabel.config(text = hulp)
text_box.insert(tk.END, "\nPut me on a new line!")

# Run the main loop
window.mainloop()
