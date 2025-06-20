"""
This file creates the subframe for data creation
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

# Image paths
open_folder_image = "Distributed_GUI/smiley3.png"

'''
Functions needed before the event handling functions
'''
def create_data(masterframe, callback):
    data = [[1, 2, 3], ['A', 'B', 'C'], [4, 5, 6]]
    # Show the moment that is clicked in status label
    now = datetime.datetime.now()
    pd_now = pd.Timestamp(now)
    freq = '1s'
    pd_round = pd_now.round(freq)
    now_rounded = pd_round.to_pydatetime()
    masterframe.label_0_1_clicked.configure(text=f"Data loaded at {now_rounded}")
    masterframe.label_0_1_status.configure(text=str(data))
    # Call the callback function with the generated data
    callback(data)

'''
1️⃣ Fill frame
'''
def Place_frame1(masterframe, callback):
    # Create a (sub)frame with a button and two labels
    label_0_1 = ctk.CTkLabel(masterframe, text=f"Click button to create data")
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)
    # Create a "Create data" button
    open_folder_img = ctk.CTkImage(light_image=Image.open(open_folder_image), \
                                   dark_image=Image.open(open_folder_image))
    file_import_button = ctk.CTkButton(masterframe, text="Create data", image=open_folder_img, \
                                       compound='left', command=lambda: create_data(masterframe, callback))
    file_import_button.grid(column=0, row=1, sticky="nw", padx=2, pady=2)

    # Create label in (sub)frame with created data
    masterframe.label_0_1_clicked = ctk.CTkLabel(masterframe, text=f" ..waiting..")
    masterframe.label_0_1_clicked.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

    # Create label in (sub))frame to indicate status
    masterframe.label_0_1_status = ctk.CTkLabel(masterframe, text=f" .. no status.. ")  # empty when no action happens
    masterframe.label_0_1_status.grid(column=0, row=4, sticky="nw", padx=2, pady=2)

if __name__ == '__main__':
    # In this way Frame1 can run stand-alone for debugging
    def callback(data):
        # Nothing is done with the received data
        pass

    masterframe = ctk.CTk()
    masterframe.title('Test Frame 1')
    # masterframe.geometry("300x150")  # width x height
    masterframe.minsize(100, 100)
    open_folder_image = "../Distributed_GUI/smiley3.png" # '../' was added
    Place_frame1(masterframe, callback)
    masterframe.label_0_1_status.configure(text='Main runs')

    # Run the main loop
    masterframe.mainloop()
