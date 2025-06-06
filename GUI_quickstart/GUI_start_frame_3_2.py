import tkinter as tk
import array as arr

"""Labels implemented as a 2D array """
'''2D array approach'''
window = tk.Tk()
window.minsize(75*3, 50*3)
window.title('Weighted grid frame')  

# label=[]
rows, cols = (3, 3)
label = [[0 for i in range(cols)] for j in range(rows)]

for i in range(rows):
    window.columnconfigure(i, weight=(1+i), minsize=75)
    window.rowconfigure(i, weight=(1+i), minsize=50)

    for j in range(0, cols):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5, sticky="se")
        label[i][j] = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label[i][j].pack(padx=5, pady=5)

label[1][2].config(text='hulp')

window.mainloop()
