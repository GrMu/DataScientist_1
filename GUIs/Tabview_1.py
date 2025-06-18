import customtkinter as ctk
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

imgpath = "../GUIs/images/smiley3.png"
ctk.set_appearance_mode("dark")

window = ctk.CTk()
tabview = ctk.CTkTabview(master=window)
tabview.pack(padx=20, pady=20)

tab_1 = tabview.add("tab 1")  # add tab at the end
tab_2 = tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = ctk.CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)

greeting = tk.Label( master=tab_1, text="Hello, Tkinter", background="#34A2FE", foreground='purple', width=10, height=5)
greeting.pack()
greeting2 = ttk.Label(master=tab_2, text="Hello, TTkinter", background='#F08080', foreground='#581845', width=20)
greeting2.pack()

# image = ImageTk.PhotoImage(Image.open(r'imgpath'))
image = ImageTk.PhotoImage(file=imgpath)
tctimg = tk.Label(tab_2, text=' Hello', image=image, compound='left').pack()
'''
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

'''
'''text_box = tk.Text()
text_box.insert("1.0", "Hoh hoi")
text_box.pack()
hulp = text_box.get("1.0", tk.END)
entrylabel.config(text = hulp)
text_box.insert(tk.END, "\nPut me on a new line!")
'''
# Run the main loop
window.mainloop()

