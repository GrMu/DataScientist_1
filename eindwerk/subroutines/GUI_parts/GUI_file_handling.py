"""
This file creates the GUI for file handling and calls the file_handling functions
"""
'''
Import
'''
# Libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from CTkTable import *
import numpy as np

import os
import pandas as pd
import time

# Own routines
import  subroutines.File_handling.Datafile_history_v2 as hist
import subroutines.File_handling.Read_csv_data_file as rd_csv

# Image paths
open_folder_image = "images/dossier(1).png"
file_history_image = "images/dossier.png"
read_file_image = "images/csv(1).png"

# Other paths
history_file = 'resources/Files/datafile_history.txt'

# Settings
datetime_format_list = ["%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M"]

'''
Functions needed before the event handling functions
'''

def calculate_avg_timestep(data):
    # Calculate the difference between consecutive timestamps
    time_deltas = data.index.to_series().diff().dropna()
    # Get the most common timestep (mode) in the dataframe
    timestep = time_deltas.mode()[0]
    print("timestep: ", timestep, "type: ", type(timestep))
    #time step_seconds = timestep.total_seconds()  # Does not function anymore: strange
    # print(f"The timestep is: {timestep} and in seconds: {timestep_seconds}")
    return timestep


def get_data_header_and_dialect(filepath):
    # Call header_csv... to receive headerinfo with 'sample', 'dialect', 'file_path', 'raw columns'.
    header_info = rd_csv.header_csv_file_with_method(filepath, 'auto2')
    # print("columns ", columns)
    columns = ['no datetime']+ header_info['raw columns']
    combobox_dt['state'] = 'normal'
    combobox_dt.set(columns[0])  # The visible entry in combobox
    combobox_dt.configure(values=columns)
    file_import_button.configure(state="normal")
    # combobox_dt.update_idletasks()
    combobox_dt['state'] = 'readonly'  # avoids writing by user in combobox
    sample_textbox.delete("1.0", "end")
    sample_textbox.insert("1.0", header_info['sample'])

# A filepath is selected: read header of file and update widgets
def start_read_header_file(file_path):
    print("Selected file:", file_path)
    # Write the last 30 datafiles in a file
    hist.add_to_history(history_file, file_path)
    file_ = os.path.basename(file_path)
    label_0_1_2.configure(text=f"File: {file_}")
    label_0_1_status.configure(text=f"Reading header: wait", text_color='red')
    label_0_1_2.update_idletasks()  # Update screen immediately
    get_data_header_and_dialect(file_path)
    label_0_1_status.configure(text=f" ")
    # Remove info about previous file label_0_1_rows.configure(text=f"# rows: {data_info['orig_rows']}")
    label_0_1_rows.configure(text=f"..")
    label_0_1_columns.configure(text=f"..")
    label_0_1_cleaned.configure(text=f" . ")
    label_0_1_clnd_rows.configure(text=f"..")
    label_0_1_clnd_columns.configure(text=f"..")
def read_file(): # file_path, dialect are stored in the module
    label_0_1_status.configure(text=f"Reading file: wait", text_color='red')
    label_0_1_status.update_idletasks()  # Update screen immediately
    datetime_column = combobox_dt.get()
    print("Selected datetime_column: ", datetime_column)
    datetime_format = combobox_dtfor.get()
    print("Selected datetime_format: ", datetime_format)
    data, data_info = rd_csv.read_file(datetime_column, datetime_format)
    print("Data: ", data)
    label_0_1_rows.configure(text=f"# rows: {data_info['orig_rows']}")
    label_0_1_columns.configure(text=f"# columns: {data_info['orig_columns']}")
    label_0_1_cleaned.configure(text=f"Cleaned data:")
    label_0_1_clnd_rows.configure(text=f"# rows: {data_info['cleaned_rows']}")
    label_0_1_clnd_columns.configure(text=f"# columns: {data_info['cleaned_columns']}")
    if datetime_column != 'no datetime':
        timestep = calculate_avg_timestep(data)
        label_0_1_step.configure(text=f"avg. step: {timestep}")
    else:
        label_0_1_step.configure(text=f"--")
    label_0_1_status.configure(text=f"  ")

# Callback function to handle 'File history' button click
def file_history():
    # Read file history, show pop-up and return the selected filepath
    history = hist.read_history(history_file)
    file_path = hist.select_history_filepath(history)  # No value is returned, therefore another read action below
    file_path2 = hist.selected_filepath
    if file_path:
        # Process the selected file (you can replace this with your own logic)
        start_read_header_file(file_path)

'''
Create the GUI
'''

'''
Add elements to the frames
'''
'''
1️⃣ First row
'''
# Intro label in second frame
# Assume a grid of 6 columns
label_0_1 = ctk.CTkLabel(frame_vert[0][1], text=f"Select a data file")
label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)
# the last 4 columns must have same width: this to try that textbox get same width
for k in range(4):
    label_0_1.grid_columnconfigure(k+2, weight=1, uniform="col")  # offset beyond first 2 columns (k+2)

# Create a "Select File" button
open_folder_img = ctk.CTkImage(light_image=Image.open(open_folder_image), \
                               dark_image=Image.open(open_folder_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="Select file", image=open_folder_img, \
                                   compound='left', command=import_file)
file_import_button.grid(column=0, row=1, sticky="nw", padx=2, pady=2)

# Create a "File history" button
open_folder_img = ctk.CTkImage(light_image=Image.open(file_history_image), \
                               dark_image=Image.open(file_history_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="File history", image=open_folder_img, \
                                   compound='left', command=file_history)
file_import_button.grid(column=0, row=2, sticky="nw", padx=2, pady=2)

# Create label in second frame with selected filepath
label_0_1_2 = ctk.CTkLabel(frame_vert[0][1], text=f" Filepath: (empty)")
label_0_1_2.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

# Create label in second frame to indicate status (read header, read file)
label_0_1_status = ctk.CTkLabel(frame_vert[0][1], text=f" ")  # empty when no action happens
label_0_1_status.grid(column=0, row=4, sticky="nw", padx=2, pady=2)

# Combobox to know datetime column
combobox_label_dt = ctk.CTkLabel(frame_vert[0][1], text="Choose datetime column")
combobox_label_dt.grid(column=1, row=0, sticky="nw", padx=2, pady=2)
combobox_dt_var = tk.StringVar(frame_vert[0][1], "empty")  # The visible entry in combobox
combobox_dt = ctk.CTkComboBox(frame_vert[0][1], values=["empty"])
combobox_dt['state'] = 'readonly'
combobox_dt.grid(column=1, row=1, sticky="nw", padx=2, pady=2)

# Combobox to know datetime format
combobox_label_dtfor = ctk.CTkLabel(frame_vert[0][1], text="Select or write datetime format")
combobox_label_dtfor.grid(column=1, row=2, sticky="nw", padx=5, pady=0)
combobox_dtfor = ctk.CTkComboBox(frame_vert[0][1], values=datetime_format_list)
combobox_dtfor.grid(column=1, row=3, sticky="nw", padx=2, pady=0)

# Create a "Read file" button
read_file_img = ctk.CTkImage(light_image=Image.open(file_history_image), dark_image=Image.open(read_file_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="Read file", image=open_folder_img, compound='left', \
                                   state= "disabled", command=read_file)
file_import_button.grid(column=1, row=4, sticky="nw", padx=2, pady=4)

# Create label in second frame at the right to indicate sample data
#  First row in frame
label_0_1_smpl = ctk.CTkLabel(frame_vert[0][1], text=f"Sample data fom the file")
label_0_1_smpl.grid(column=2, row=0, sticky="nw", padx=2, pady=2)
label_0_1_rows = ctk.CTkLabel(frame_vert[0][1],     text=f" .          .", width=100)
label_0_1_columns = ctk.CTkLabel(frame_vert[0][1],  text=f" ..        ..", width=100)
label_0_1_rows.grid(column=3, row=0, sticky="nw", padx=2, pady=2)
label_0_1_columns.grid(column=4, row=0, sticky="nw", padx=2, pady=2)

# Create textbox in second frame at the right with sample data and scrollbars
sample_textbox = ctk.CTkTextbox(frame_vert[0][1], wrap="none", height=100)  # , state="disabled" means read-only , height=140
sample_textbox.grid(column=2, row=1, sticky="nw", columnspan=4, rowspan=3)  #
# sample_textbox.grid_rowconfigure(0, weight=1)
# sample_textbox.grid_columnconfigure(0, weight=1)
# Create a Text widget
sample_textbox.insert("1.1", f"empty")
#  Bottom row in frame
label_0_1_cleaned = ctk.CTkLabel(frame_vert[0][1], text=f" . ")  # This serves to show cleaned data statistics later
label_0_1_cleaned.grid(column=2, row=4, sticky="nw", padx=2, pady=2)
label_0_1_clnd_rows = ctk.CTkLabel(frame_vert[0][1],     text=f" .          .", width=100)
label_0_1_clnd_columns = ctk.CTkLabel(frame_vert[0][1],  text=f" ..        ..", width=100)
label_0_1_step = ctk.CTkLabel(frame_vert[0][1],     text=f" ...      ...", width=100)
label_0_1_clnd_rows.grid(column=3, row=4, sticky="nw", padx=2, pady=2)
label_0_1_clnd_columns.grid(column=4, row=4, sticky="nw", padx=2, pady=2)
label_0_1_step.grid(column=5, row=4, sticky="nw", padx=2, pady=2)
# label_0_1_empty2.update_idletasks()  # No influence on textbox width

