import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()
frame_d = tk.Frame()

frame_a.    configure(relief=tk.GROOVE, borderwidth=3)
# frame_d.configure(relief=tk.RIDGE, borderwidth=3)

label_a = tk.Label(master=frame_a, text="What is your name? ")
ent_a = tk.Entry(master=frame_a, width=50)
label_b = tk.Label(master=frame_b, text="I'm in Frame B")

label_a.pack(side=tk.LEFT)
ent_a.pack()
label_b.pack()


frame_a.pack()
frame_b.pack()

window.mainloop()
