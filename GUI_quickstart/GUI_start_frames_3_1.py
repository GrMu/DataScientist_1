import tkinter as tk

window = tk.Tk()
window.minsize(75*3, 50*3)

for i in range(3):
    window.columnconfigure(i, weight=(1+i), minsize=75)
    window.rowconfigure(i, weight=(1+i), minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5, sticky="se")
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
