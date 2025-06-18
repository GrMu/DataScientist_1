"""
This file creates the GUI for data import
"""
'''
Import
'''
# Libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import datetime
import pandas as pd

# Own routines
# import Distributed_GUI as MainGUI


# Image paths
open_folder_image = "images/smiley3.png"

'''
Functions needed before the event handling functions
'''
def create_data(masterframe, callback):
    data = [[1,2,3], ['A','B','C'], [4, 5, 6]]
    now = datetime.datetime.now()
    pd_now = pd.Timestamp(now)
    freq = '1s'
    pd_round = pd_now.round(freq)
    now_rounded = pd_round.to_pydatetime()
    masterframe.label_0_1_clicked.configure(text=f"Data loaded at {now_rounded}")
    masterframe.label_0_1_status.configure(text=str(data))
    callback(data)  # Call the callback function with the generated data

'''
1️⃣ Fill frame
'''
def Place_frame1(masterframe, callback):
    # Intro label in second frame
    # Assume a grid of 6 columns ???
    label_0_1 = ctk.CTkLabel(masterframe, text=f"Select a data file")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)
    # Create a "Select File" button
    open_folder_img = ctk.CTkImage(light_image=Image.open(open_folder_image), \
                                   dark_image=Image.open(open_folder_image))
    file_import_button = ctk.CTkButton(masterframe, text="Select file", image=open_folder_img, \
                                       compound='left', command=lambda: create_data(masterframe))
    file_import_button.grid(column=0, row=1, sticky="nw", padx=2, pady=2)

    # Create label in second frame with selected filepath
    masterframe.label_0_1_clicked = ctk.CTkLabel(masterframe, text=f" ..waiting..")
    masterframe.label_0_1_clicked.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

    # Create label in second frame to indicate status (read header, read file)
    masterframe.label_0_1_status = ctk.CTkLabel(masterframe, text=f" .. no status.. ")  # empty when no action happens
    masterframe.label_0_1_status.grid(column=0, row=4, sticky="nw", padx=2, pady=2)

if __name__ == '__main__':
    masterframe = ctk.CTk()
    masterframe.title('Test Frame 1')
    # masterframe.geometry("300x150")  # width x height
    masterframe.minsize(100, 100)
    open_folder_image = "../images/smiley3.png"
    Place_frame1(masterframe)
    masterframe.label_0_1_status.configure(text='Main runs')

    # Run the main loop
    masterframe.mainloop()
