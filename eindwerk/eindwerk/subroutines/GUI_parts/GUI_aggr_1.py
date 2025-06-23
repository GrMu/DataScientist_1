"""
Creates the frame that plots aggregated data.
It can only work with datetime index!
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

# own modules
import subroutines.Data_handling.aggregation as aggr

'''
global
'''
# data_pd and data_info must come from main module
# prop are properties internal to this plot module
data_pd = []
data_info = {'orig_rows': 0, 'orig_columns': 0, 'cleaned_rows': 0, 'cleaned_columns': 0,
             'datetime_column': 'no datetime', 'datetime_format': "", 'columns': [],
             'timestep': None, 'time_deviation': None,
             'data_name': "empty", 'data_path': None }
prop = {'Datetime_as_index': False, 'nr_comboboxes': 1, 'resampled': False,
        'plot_exists': False, 'figure_ref': None,
        'lightmode': 'ggplot', 'darkmode': "dark_background"}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

'''
Sub-functions of the module
'''

def adapt_fig_color():
    # adapt to app look (dark/ light)
    look = ctk.get_appearance_mode()
    plot_style = prop['lightmode']  if look == "Light" else prop['darkmode']  # e.g. ggplot classic Solarize_Light2 seaborn-v0_8
    plt.style.use(plot_style)


def update_plot(frame_, y_plots, aggregation, nr_days_to_discern):
    global prop
    # aggregation['average', 'minimum', 'maximum']
    adapt_fig_color()
    # Create a figure and a grid of subplots
    fig, axs = plt.subplots(1, 3, figsize=(14, 5), sharey=False)
    prop['plot_exists'] = True
    prop['figure_ref'] = fig
    # Plot with minimum
    column_name_plot = y_plots[0]
    parameter =  y_plots[0] # Can be overwritten later with help of a user entry
    for day in range(nr_days_to_discern):
        axs[0].plot(aggregation['minimum'].index.get_level_values(0) + aggregation['minimum'].index.get_level_values(1) / 60,
                    aggregation['minimum'][column_name_plot].iloc[:, day], label=days[day])
    # axs[0].set_ylim(min_y_value, max_y_value)
    axs[0].set_title(f'Minimum {parameter} found over each day')
    axs[0].set_xlabel('Hour of the Day')
    axs[0].set_ylabel(parameter)
    axs[0].set_xticks(np.arange(0, 25, 2))  # Set x-axis ticks to show every hour
    # axs[0].legend()
    # Plot with average
    for day in range(nr_days_to_discern):
        axs[1].plot(aggregation['average'].index.get_level_values(0) + aggregation['average'].index.get_level_values(1) / 60,
                    aggregation['average'][column_name_plot].iloc[:, day], label=days[day])
    # axs[1].set_ylim(min_y_value, max_y_value)
    axs[1].set_title(f'Average {parameter} over each day')
    axs[1].set_xlabel('Hour of the Day')
    axs[1].set_ylabel(parameter)
    axs[1].set_xticks(np.arange(0, 25, 2))  # Set x-axis ticks to show every hour
    # axs[1].legend()
    # Plot with maximum
    for day in range(nr_days_to_discern):
        axs[2].plot(aggregation['maximum'].index.get_level_values(0) + aggregation['maximum'].index.get_level_values(1) / 60,
                    aggregation['maximum'][column_name_plot].iloc[:, day], label=days[day])
    # axs[2].set_ylim(min_y_value, max_y_value)
    # axs[2].set_title('Maximum power found over each day')
    axs[2].set_title(f'Maximum {parameter} found over each day')
    axs[2].set_xlabel('Hour of the Day')
    axs[2].set_ylabel(parameter)
    axs[2].set_xticks(np.arange(0, 25, 2))  # Set x-axis ticks to show every hour
    # axs[2].legend()
    # Get the limits of the axes of the plots and derive the min. and max. value.
    limits = []
    for i, _ in enumerate(axs):
        print("i", i)
        limits.append(axs[i].get_ylim())
    # print("limits: ", limits)
    # Extract all values from the list of tuples
    lim_values = [item for sublist in limits for item in sublist]
    min_value = min(lim_values)
    max_value = max(lim_values)
    lim_new = (min_value, max_value)
    plt.setp(axs, ylim=lim_new)
    plt.tight_layout()  # Adjust layout to prevent overlap

    canvas = FigureCanvasTkAgg(fig, master=frame_)
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=0, sticky="nsew", columnspan=4, rowspan=8, padx=2, pady=2)
    # Make the canvas expandable
    frame_.grid_rowconfigure(0, weight=1)
    frame_.grid_columnconfigure(1, weight=1)
    plt.close(fig)  # Close the figure after drawing
    frame_.update()
    # toolbar = NavigationToolbar2Tk(canvas, frame_, pack_toolbar=False)
    # toolbar.grid(column=1, row=8, sticky="sw")

'''
Main functions of the module
'''

def start_update_plot(frame_):
    global data_pd
    y = [None] * prop['nr_comboboxes']  # Initialize the list with the correct size
    y_plots = []
    for i in range(prop['nr_comboboxes']):
        y[i] = frame_.comboboxes[i].get()
        if y[i] != 'no display':
            y_plots.append(y[i])
    print("y_plots ", y_plots )
    nr_days_to_discern = int(frame_.combobox_days.get())

    # Aggregate the data
    # aggregation['average', 'minimum', 'maximum']
    aggregation = aggr.aggregate(data_pd, data_info, nr_days_to_discern)

    if y_plots != []: # Cannot be empty in principle, but who knows
        update_plot(frame_, y_plots, aggregation, nr_days_to_discern)


def update_window(frame_):
    # if new data arrives, update window: update comboboxes and empty graph
    pass

def Place_frame1(frame_, data_in, data_info_in):
    global data_pd, data_info, prop
    data_info = data_info_in
    # Index of data_pd must have datetime format
    # This is checked normally before calling this function
    # Resample data if needed fo better aggregation, data_in must be Dataframe with datetime as index
    one_minute = pd.Timedelta(minutes=1)
    if data_info['timestep']< one_minute:
        data_pd = aggr.resample_data(data_in)
        prop['resampled'] = True
    else:
        data_pd = data_in  # must be DataFrame
        prop['resampled'] = False
    print(f"GUI_aggr: data resamples {prop['resampled']}")
    data_columns = list(data_in.columns)
    # print(f"GUI_aggr: data_columns : {data_columns}")
    label_0_1 = ctk.CTkLabel(frame_, text="Select columns to plot")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)

    # Combobox with column names
    # Now 1 combobox, but can easily be increased due to for-loop
    frame_.comboboxes = [0 for i in range(prop['nr_comboboxes'])]
    for i in range(prop['nr_comboboxes']):
        frame_.comboboxes[i] = ctk.CTkComboBox(frame_, values=data_columns)
        frame_.comboboxes[i]['state'] = 'readonly'
        frame_.comboboxes[i].grid(column=0, row=i+1, sticky="nw", padx=2, pady=2)

    # Combobox with nr of days to aggregate
    label_0_2 = ctk.CTkLabel(frame_, text="Aggregate down to 1 or 7 days")
    label_0_2.grid(column=0, row=i+3, sticky="nw", padx=2, pady=2)
    frame_.combobox_days = ctk.CTkComboBox(frame_, values=['1', '7'])
    frame_.combobox_days['state'] = 'readonly'
    frame_.combobox_days.grid(column=0, row=i+4, sticky="nw", padx=2, pady=2)

    # Plot button
    update_plot_button = ctk.CTkButton(frame_, text="Plot aggregated data", command=lambda frame_=frame_: start_update_plot(frame_))
    update_plot_button.grid(column=0, row=i+5, sticky="nw", padx=2, pady=2)

    # Status label
    label_0_status = ctk.CTkLabel(frame_, text=f"( Data resampled: {prop['resampled']} )")
    label_0_status.grid(column=0, row=i+6, sticky="nw", padx=2, pady=2)

    # data_pd = pd.DataFrame({'x': [0, 1], 'y': [2, 4]})
    # update_plot(frame_, aggregation, 'X', 'no_plot')  # initial empty plot
    if prop['plot_exists'] == True:
        plt.close(prop['figure_ref'])


if __name__ == '__main__':
    '''
    Create testdata, create a datetime-index and plot data
    Not evident to create an example
    
    All code is from GUI_plot: not adapted!!
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
        data_pd.set_index('t', inplace=True)
        # data_pd.index.name = 'time'
        print(f"data_PD in testing: \n{data_pd} \n ")
        data_columns = list(data_pd.columns)
        print(f"data_columns in testing: {data_columns} \n ")
        return data_pd, data_columns


    data_pd, data_columns = create_testdata()

    frame_ = ctk.CTk()
    ctk.set_appearance_mode("dark")
    frame_.title('Test Frame plot')
    frame_.minsize(100, 100)
    data_info['datetime_column'] = "%Y-%m-%d %H:%M:%S"
    data_info['datetime_format'] = 't'
    Place_frame1(frame_, data_pd, data_info)

    frame_.mainloop()
