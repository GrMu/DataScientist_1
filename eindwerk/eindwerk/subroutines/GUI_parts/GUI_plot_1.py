
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas as pd

def create_testdata():
    # Create some data
    t_array = [i * 0.01 for i in range(int((10 / 0.01 + 1)))]
    y1 = [2 * np.sin(2 * np.pi * t) for t in t_array]
    y2 = [2 * np.cos(2 * np.pi * t) for t in t_array]
    y3 = [1 + 1 * np.sin(3 * np.pi * t) for t in t_array]
    y4 = [0.5 + 1.5 * np.sin(4 * np.pi * t) for t in t_array]
    y5 = [2 - 1 * np.cos(2.5 * np.pi * t) for t in t_array]
    y6 = [3 - 1.5 * np.sin(4 * np.pi * t) for t in t_array]
    data_pd = pd.DataFrame({'t': t_array, 'y1': y1, 'y2': y2, 'y3': y3, 'y4': y4, 'y5': y5, 'y6': y6})
    data_columns = list(data_pd.columns)
    return data_pd, data_columns

def update_plot(frame_, value):
    print('frame: ', frame_)
    print(f"Selected value: {value}")

def update_window(frame_):
    # if new data arrives, update window: update comboboxes and empty graph
    pass

def Place_frame1(frame_, data_in):
    data_columns = list(data_in.columns)
    label_0_1 = ctk.CTkLabel(frame_, text="Select columns to plot")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)

    nr_comboboxes = 4
    frame_.comboboxes = [0 for i in range(nr_comboboxes)]
    for i in range(nr_comboboxes):
        frame_.comboboxes[i] = ctk.CTkComboBox(frame_, values=data_columns, command=lambda value, frame_=frame_: update_plot(frame_, value))
        frame_.comboboxes[i]['state'] = 'readonly'
        frame_.comboboxes[i].grid(column=0, row=i+1, sticky="nw", padx=2, pady=2)

    label_0_2 = ctk.CTkLabel(frame_, text="Select X-axis to plot")
    label_0_2.grid(column=0, row=5, sticky="nw", padx=2, pady=2)
    frame_.comboboxes_X = ctk.CTkComboBox(frame_, values=data_columns, command=lambda value, frame_=frame_: update_plot(frame_, value))
    frame_.comboboxes_X['state'] = 'readonly'
    frame_.comboboxes_X.grid(column=0, row=6, sticky="nw", padx=2, pady=2)

    fig = Figure(figsize=(8, 6))
    fig.add_subplot(111).scatter([0, 1], [2, 4])
    canvas = FigureCanvasTkAgg(fig, master=frame_)
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=0, sticky="nw", columnspan=4, rowspan=8, padx=2, pady=2)

if __name__ == '__main__':
    data_pd, data_columns = create_testdata()

    frame_ = ctk.CTk()
    frame_.title('Test Frame plot')
    frame_.minsize(100, 100)
    Place_frame1(frame_, data_pd)

    frame_.mainloop()
