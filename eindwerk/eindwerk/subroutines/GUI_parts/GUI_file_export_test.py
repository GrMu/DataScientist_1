"""
This file creates the GUI for exporting data to CSV file
"""
'''
Import
'''
# Libraries
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os
import pandas as pd

# Image paths
open_folder_image = "images/dossier(1).png"
file_history_image = "images/dossier.png"
read_file_image = "images/csv(1).png"

data = []
data_info = {'orig_rows': 0, 'orig_columns': 0, 'cleaned_rows': 0, 'cleaned_columns': 0,
             'datetime_column': 'no datetime', 'datetime_format': "", 'columns': [],
             'timestep': None, 'time_deviation': None,
             'data_name': "empty", 'data_path': None}


def export_file(frame_):
    frame_.label_0_1_status.configure(text=f"Writing file: wait", text_color='red')
    frame_.label_0_1_status.update_idletasks()  # Update screen immediately
    path = frame_.entry_path.get()
    file = frame_.entry_file.get()
    filepath = os.path.join(path, file)
    data.to_csv(filepath, index=False)
    frame_.label_0_1_status.configure(text=f"Done", text_color='red')


def Place_frame1(frame_, data_in, data_info_in):
    global data, data_info
    data = data_in
    data_info = data_info_in

    label_0_1 = ctk.CTkLabel(frame_, text=f"Create path and file name to export data")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)
    label_0_1_2 = ctk.CTkLabel(frame_, text=f"Attention to use '/' (forward slashes)")
    label_0_1_2.grid(column=0, row=2, sticky="nw", padx=2, pady=2)
    label_0_2 = ctk.CTkLabel(frame_, text=f"Path: ")
    label_0_2.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

    frame_.entry_path = ctk.CTkEntry(frame_)
    frame_.entry_path.grid(column=0, row=4, sticky="nw", padx=2, pady=2, columnspan=3)
    frame_.entry_path.insert(0, data_info['data_path'])

    file_proposal = data_info['data_name'] + '_export.csv'
    label_0_3 = ctk.CTkLabel(frame_, text=f"Filename and extension")
    label_0_3.grid(column=0, row=5, sticky="nw", padx=2, pady=2)

    frame_.entry_file = ctk.CTkEntry(frame_)
    frame_.entry_file.grid(column=0, row=6, sticky="nw", padx=2, pady=2, columnspan=3)
    frame_.entry_file.insert(0, file_proposal)

    open_folder_img = ctk.CTkImage(light_image=Image.open(open_folder_image), dark_image=Image.open(open_folder_image))
    file_export_button = ctk.CTkButton(frame_, text="Export data", image=open_folder_img, compound='left',
                                       command=lambda: export_file(frame_))
    file_export_button.grid(column=0, row=7, sticky="nw", padx=2, pady=2)

    frame_.label_0_1_status = ctk.CTkLabel(frame_, text=f" ")
    frame_.label_0_1_status.grid(column=0, row=8, sticky="nw", padx=2, pady=2)


if __name__ == '__main__':
    open_folder_image = "../../images/dossier(1).png"
    file_history_image = "../../images/dossier.png"
    read_file_image = "../../images/csv(1).png"

    data_dict = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    data = pd.DataFrame(data_dict)
    data_info['data_name'] = 'testdata'
    data_info['data_path'] = 'c:/tmp'

    frame_ = ctk.CTk()
    frame_.title('Test Frame export data')
    frame_.minsize(100, 100)
    Place_frame1(frame_, data, data_info)
    frame_.label_0_1_status.configure(text='Main runs')

    frame_.mainloop()
