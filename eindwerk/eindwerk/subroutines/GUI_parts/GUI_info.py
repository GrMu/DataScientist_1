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

# Image paths
example_light = "resources/Graphics/Data_aggregation_example_light.png"
example_dark = "resources/Graphics/Data_aggregation_example_dark.png"

# Other paths
# --
# Settings
def title_font():
    return ctk.CTkFont(family="Flexo Medium", size=16,
	        weight="normal", slant="roman", underline=False, overstrike=False)
            #weight bold/normal, slant=italic/roman
def italic_font():
    return ctk.CTkFont(family="Flexo Medium", size=14, weight="normal",
            slant="roman", underline=False, overstrike=False)
            #weight bold/normal, slant=italic/roman
'''
GUI
'''
def Place_frame1(frame_):
    label_0_1 = ctk.CTkLabel(frame_, text=f"Plot and aggregate data.", font=title_font())
    label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)
    label_0_1_2 = ctk.CTkLabel(frame_, font=italic_font(), \
                    text=f"An example of data aggregation: the average of every weekday in a year :")
    label_0_1_2.grid(column=0, row=1, sticky="nw", padx=2, pady=10)
    label_0_2 = ctk.CTkLabel(frame_, font=italic_font(), \
            text=f"average electricity consumption in Flanders for every weekday (S21 profile).")
    label_0_2.grid(column=0, row=2, sticky="nw", padx=2, pady=10)

    # Load the image
    look = ctk.get_appearance_mode()
    image_path = example_light if look == "Light" else example_dark
    image = ctk.CTkImage(Image.open(image_path), size=(250, 270))  # Adjust size as needed

        # Create a label to display the image without text
    image_label = ctk.CTkLabel(frame_, image=image, text="")
    image_label.grid(column=1, row=0, sticky="nw", padx=2, pady=2, rowspan=8, columnspan=3)

    # Create label to indicate status (read header, read file)
    frame_.label_0_1_status = ctk.CTkLabel(frame_, text=f" ")  # empty when no action happens
    frame_.label_0_1_status.grid(column=0, row=4, sticky="nw", padx=2, pady=2)
    frame_.pack_propagate(True)

    # Configure the grid to allow resizing
    frame_.grid_columnconfigure(1, weight=1)
    frame_.grid_rowconfigure(0, weight=1)

if __name__ == '__main__':
    # In this way GUI_file_handling can run stand-alone for debugging

    # Overwrite paths
    # Image paths
    example_light = "../../resources/Graphics/Data_aggregation_example_light.png"
    example_dark = "../../resources/Graphics/Data_aggregation_example_dark.png"

    frame_ = ctk.CTk()
    ctk.set_appearance_mode("dark")
    frame_.title('Test Info Frame')
    # frame_.geometry("300x150")  # width x height
    frame_.minsize(400, 440)
    Place_frame1(frame_)
    frame_.label_0_1_status.configure(text='.')

    # Run the main loop
    frame_.mainloop()
