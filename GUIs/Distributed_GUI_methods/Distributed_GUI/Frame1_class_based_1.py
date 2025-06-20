"""
This file creates the subframe for data creation
"""

# Libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import datetime
import pandas as pd

class Frame1:
    def __init__(self, masterframe, callback):
        self.masterframe = masterframe
        self.callback = callback
        if __name__ != '__main__':
            self.open_folder_image = "Distributed_GUI/smiley3.png"
        else:  # for testing/debugging the file must be able to run stand-alone: the paths must be adapted.
            self.open_folder_image = "../Distributed_GUI/smiley3.png"

        # Intro label in (sub)frame
        label_0_1 = ctk.CTkLabel(masterframe, text=f"Click button to create data")
        label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)

        # Create a "Create data" button
        open_folder_img = ctk.CTkImage(light_image=Image.open(self.open_folder_image), \
                                       dark_image=Image.open(self.open_folder_image))
        file_import_button = ctk.CTkButton(masterframe, text="Create data", image=open_folder_img, \
                                           compound='left', command=self.create_data)
        file_import_button.grid(column=0, row=1, sticky="nw", padx=2, pady=2)

        # Create label in (sub)frame with created data
        self.label_0_1_clicked = ctk.CTkLabel(masterframe, text=f" ..waiting..")
        self.label_0_1_clicked.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

        # Create label in (sub)frame to indicate status
        self.label_0_1_status = ctk.CTkLabel(masterframe, text=f" .. no status.. ")  # empty when no action happens
        self.label_0_1_status.grid(column=0, row=4, sticky="nw", padx=2, pady=2)

    def create_data(self):
        data = [[1, 2, 3], ['A', 'B', 'C'], [4, 5, 6]]
        # Show the time when clicked for animation
        now = datetime.datetime.now()
        pd_now = pd.Timestamp(now)
        freq = '1s'
        pd_round = pd_now.round(freq)
        now_rounded = pd_round.to_pydatetime()
        self.label_0_1_clicked.configure(text=f"Data loaded at {now_rounded}")
        self.label_0_1_status.configure(text=str(data))
        self.callback(data)  # Call the callback function with the generated data

if __name__ == '__main__':
    # In this way Frame1 can run stand-alone for debugging

    def callback(data):
        # Nothing is done with the received data
        pass

    masterframe = ctk.CTk()
    masterframe.title('Test Frame 1')
    # masterframe.geometry("300x150")  # width x height
    masterframe.minsize(100, 100)
    app = Frame1(masterframe, callback)
    app.label_0_1_status.configure(text='Main runs')

    # Run the main loop
    masterframe.mainloop()
