import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()
frame_d = tk.Frame()

frame_a.configure(relief=tk.SUNKEN, borderwidth=3)
frame_b.configure(relief=tk.RAISED, borderwidth=3)
frame_c.configure(relief=tk.GROOVE, borderwidth=3)
frame_d.configure(relief=tk.RIDGE, borderwidth=3)

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_c = tk.Label(master=frame_c, text="I'm in Frame C")
label_d = tk.Label(master=frame_d, text="I'm in Frame D")

label_a.pack()
label_b.pack()
label_c.pack()
label_d.pack()

frame_b.pack()
frame_a.pack(side=tk.LEFT)
frame_c.pack()
frame_d.pack()

window.mainloop()
