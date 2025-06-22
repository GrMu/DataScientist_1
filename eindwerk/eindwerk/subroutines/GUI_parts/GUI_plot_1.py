"""
Creates the frame that plots 'raw' data against time or index
It can be tested stand-alone due to creation of testdata
"""
'''
import
'''
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# global
data_pd = []
# Properties used in the code
prop = { 'nr_comboboxes': 4}


'''
Sub-functions of the module
'''
def update_plot(frame_, x_axis_, y_plots):
    global data_pd, prop
    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot()
    ax.plot(x_axis_, y_plots)
    ax.set_xlabel(x_axis_)
    ax.set_ylabel(y_plots)
    canvas = FigureCanvasTkAgg(fig, master=frame_)
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=0, sticky="nw", columnspan=4, rowspan=8, padx=2, pady=2)
    plt.close(fig)  # Close the figure after drawing
    frame_.update()

'''
Main functions of the module
'''

def start_update_plot(frame_):
    global data_pd, prop
    # print(f"update plot. The available data is: \n {data_pd} \n")
    x_axis_ = frame_.comboboxes_X.get()
    if x_axis_ == 'index':
        x_axis_ = data_pd.index
    y = [None] * prop['nr_comboboxes']  # Initialize the list with the correct size
    y_plots = []
    for i in range(prop['nr_comboboxes']):
        y[i] = frame_.comboboxes[i].get()
        if y[i] != 'no display':
            y_plots.append(y[i])

    print("y_plots ", y_plots )
    update_plot(frame_, data_pd[x_axis_], data_pd[y_plots])

def update_window(frame_):
    # if new data arrives, update window: update comboboxes and empty graph
    pass

def Place_frame1(frame_, data_in):
    data_columns = list(data_in.columns)
    label_0_1 = ctk.CTkLabel(frame_, text="Select columns to plot")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)

    frame_.comboboxes = [0 for i in range(prop['nr_comboboxes'])]
    for i in range(prop['nr_comboboxes']):
        frame_.comboboxes[i] = ctk.CTkComboBox(frame_, values=['no display']+data_columns)
        frame_.comboboxes[i]['state'] = 'readonly'
        frame_.comboboxes[i].grid(column=0, row=i+1, sticky="nw", padx=2, pady=2)

    label_0_2 = ctk.CTkLabel(frame_, text="Select X-axis to plot")
    label_0_2.grid(column=0, row=5, sticky="nw", padx=2, pady=2)
    frame_.comboboxes_X = ctk.CTkComboBox(frame_, values=['index']+data_columns)
    frame_.comboboxes_X['state'] = 'readonly'
    frame_.comboboxes_X.grid(column=0, row=6, sticky="nw", padx=2, pady=2)

    update_plot_button = ctk.CTkButton(frame_, text="Plot data", command=lambda frame_=frame_: start_update_plot(frame_))
    update_plot_button.grid(column=0, row=7, sticky="nw", padx=2, pady=2)

    update_plot(frame_, [0, 1], [2, 4])


if __name__ == '__main__':
    '''
    Create testdata, create a datetime-index and plot data
    '''
    def get_now(freq='1h'):
        # Show the moment that is clicked in status label
        now = datetime.datetime.now()
        pd_now = pd.Timestamp(now)
        pd_round = pd_now.round(freq)
        now_rounded = pd_round.to_pydatetime()
        return now_rounded


    def float_to_datetime(t_array):
        now_ = get_now('1s')
        # print(f"Now is {now_}")
        datetime_list = []
        for t in t_array:
            # Create a new datetime object with the updated minute and microseconds value based on float value
            # Change remainder (non-int) to seconds and microseconds
            remainder = (t % 1 * 60)
            seconds = int(remainder)
            microseconds = int(remainder % 1 * 1000000)
            new_datetime = now_.replace(minute=int(t), second=seconds, microsecond=microseconds)
            datetime_list.append(new_datetime)
        # print("datetime_list:", datetime_list)
        return datetime_list


    def create_testdata():
        global data_pd
        # Create some data
        t_array = [i * 0.01 for i in range(int((10 / 0.01 + 1)))]
        y1 = [2 * np.sin(2 * np.pi * t) for t in t_array]
        y2 = [2 * np.cos(2 * np.pi * t) for t in t_array]
        y3 = [1 + 1 * np.sin(3 * np.pi * t) for t in t_array]
        y4 = [0.5 + 1.5 * np.sin(4 * np.pi * t) for t in t_array]
        y5 = [2 - 1 * np.cos(2.5 * np.pi * t) for t in t_array]
        y6 = [3 - 1.5 * np.sin(4 * np.pi * t) for t in t_array]
        datetime_list = float_to_datetime(t_array)
        time_ = pd.DatetimeIndex(datetime_list)
        data_pd = pd.DataFrame({'t': time_, 'y1': y1, 'y2': y2, 'y3': y3, 'y4': y4, 'y5': y5, 'y6': y6})
        data_pd.set_index('t')
        # data_pd.index.name = 'time'
        data_columns = list(data_pd.columns)
        return data_pd, data_columns


    data_pd, data_columns = create_testdata()

    frame_ = ctk.CTk()
    frame_.title('Test Frame plot')
    frame_.minsize(100, 100)
    Place_frame1(frame_, data_pd)

    frame_.mainloop()
