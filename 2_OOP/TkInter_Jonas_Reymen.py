import tkinter as tk

root = tk.Tk()

root.minsize(width=1050, height=500)

page = tk.Frame(root)

# layout all of the main containers
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

page.grid(sticky="nsew")

title_frame = tk.Frame(page, bg="red", height=75)
stretch_frame = tk.Frame(page, bg='yellow', width=750)
fixed_frame = tk.Frame(page, bg='green', width=300)

# Configure the grid to allow stretching
page.grid_rowconfigure(0, weight=0)
page.grid_rowconfigure(1, weight=1)
page.grid_columnconfigure(0, weight=1, minsize=750)
page.grid_columnconfigure(1, weight=0, minsize=300)

title_frame.grid(row=0, sticky="nsew", columnspan=2)
stretch_frame.grid(row=1, column=0, sticky="nsew")
fixed_frame.grid(row=1, column=1, sticky="nsew")

root.mainloop()
