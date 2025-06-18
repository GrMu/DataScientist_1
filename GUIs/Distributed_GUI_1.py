"""
This is the main module of a distributed GUI.
"""
'''
Import
'''
import tkinter as tk

# Libraries
import customtkinter as ctk
from CTkTable import *
from PIL import Image

# Own routines
import Distributed_GUI.Frame1 as frame1

# Image paths
iconpath = "images/vito-logo_blue_text_2.ico"
data_input_image = "images/tab_image-glasses.png"
data_selection_image = "images/tab_image-export.png"
plots_image = "images/tab_image-graph.png"  # tab_image-graph.png"

# Other paths
# --

# Settings
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
sgmntd_bttn_fg_color = "#2CC985"  # fg_color="#3A7EBF")
data_input_choices_list = ["SQL", "File"]

'''
Functions needed before the event handling functions
'''

# Callback function to handle segmented button clicks
def data_source(value):
    print("segmented button clicked:", value)
    if value == data_input_choices_list[0] :  # sql
        pass  # Not implemented to do something yet
    elif value == data_input_choices_list[1]:  # file
        # breng frame_vert[0][1] als variabele naar GUI_file_handling
        pass

# Function to handle button : temporary decoration
def button_click(label):
    label.configure(text="Button Clicked!")

'''
Create the GUI
'''
# Initialize the main window
root = ctk.CTk()
root.title('Data aggregation and visualisation')
root.iconbitmap(iconpath)  # ("images/smiley3.ico")  # ('images/codemy.ico')
root.geometry("1000x600")  # width x height
root.minsize(400, 400)

# More settings (that can not be defined before initializing the window)
# Interesting fonts: "Flexo Medium", "Lato", "Biome", Century Gothic", "Miso", "Rockwell Nova"
title_font = ctk.CTkFont(family="Flexo Medium", size=20,
	weight="normal", slant="roman", underline=False, overstrike=False) #weight bold/normal, slant=italic/roman

# Create two vertical frames (i) and two horizontal ones (j)
rows, cols = 2,2
# initialise vertical frame-array (1D) and their subframes as 2D matrix
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5, )
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j==0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=True, padx=5, pady=5)

'''
Add elements to the frames
'''
'''
1️⃣ First row
'''
# First column
# Frame-titel
data_input_img = Image.open(data_input_image)
data_input_label = ctk.CTkLabel(frame_vert[0][0], text=f" Data input ", \
                    image=ctk.CTkImage(data_input_img), compound='left', font=title_font)
data_input_label.pack(side=tk.TOP, padx=2, pady=2)

'''
2️⃣ Second row
'''
# Frame-titel
data_selection_img = Image.open(data_selection_image)
# data_input_img = data_input_img.resize((500, 500), Image.LANCZOS)
data_selection_label = ctk.CTkLabel(frame_vert[1][0], text=f" Data selection ", \
                        image=ctk.CTkImage(data_selection_img), compound='left', font=title_font)
data_selection_label.pack(side=tk.TOP, padx=2, pady=5)

frame1.Place_frame1(frame_vert[0][1])

# Run the main loop
root.mainloop()
