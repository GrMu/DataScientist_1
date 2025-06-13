"""
This is the main vi of a data aggregation and visualisation project.
"""

'''
Import
'''
# Libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from CTkTable import *
import pandas as pd
import os
import time

# Own routines
import  subroutines.File_handling.Datafile_history_v2 as hist
import subroutines.File_handling.Read_csv_data_file as rd_csv

# Image paths
iconpath = "images/EnergyVille.ico"  # tab_image-glasses.ico"  # vito-logo_blue_text_2.ico"
data_input_image = "images/VITO_iconen_datagebruik--data_3.png"  # tab_image-glasses.png"
sql_input_image = "images/sql-server2-5.png"  #fichier-sql.png"  #  serveur-sql.png
datafile_input_image = "images/csv.png"  # csv.png
data_selection_image = "images/VITO_iconen_datagebruik--inzicht_3.png"  # tab_image-export.png"
plots_image = "images/VITO_iconen_datagebruik--kracht_3.png"  # tab_image-graph.png"
open_folder_image = "images/dossier(1).png"
file_history_image = "images/dossier.png"
read_file_image = "images/csv(1).png"

# Other paths
history_file = 'resources/Files/datafile_history.txt'

# Settings
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
sgmntd_bttn_fg_color = "#2CC985"  # fg_color="#3A7EBF")

'''
Functions needed before the event handling functions
'''
def get_data_and_show_raw(filepath):
    data, sample, dialect = rd_csv.read_csv_file_with_method(filepath, 'auto2')
    columns = list(data.columns)
    print("columns ", columns)
    columns = ['no datetime']+ columns
    combobox_dt['state'] = 'normal'
    combobox_dt.set(columns[0])  # The visible entry in combobox
    combobox_dt.configure(values=columns)
    file_import_button.configure(state="normal")
    # combobox_dt.update_idletasks()
    combobox_dt['state'] = 'readonly'  # avoids writing by user in combobox

def read_file():
    pass

def start_read_file(file_path):
    print("Selected file:", file_path)
    # Write the last 30 datafiles in a file
    hist.add_to_history(history_file, file_path)
    file_ = os.path.basename(file_path)
    label_0_1_2.configure(text=f"File: {file_}")
    label_0_1_3.configure(text=f"Reading header: wait", text_color='red')
    label_0_1_2.update_idletasks()  # Update screen immediately
    get_data_and_show_raw(file_path)
    label_0_1_3.configure(text=f" ")
    # label_0_1_3.update_idletasks()  # Update screen immediately

'''
Event handling functions
'''
# Function to handle button click
def button_click(label):
    label.configure(text="Button Clicked!")

# Callback function to handle segmented button clicks
def callback(value):
    print("segmented button clicked:", value)

# Callback function to handle 'Select file' button click
def import_file():
    file_path = ctk.filedialog.askopenfilename(title="Select a file",
                                           filetypes=[("Data files", "*.csv"), ("All files", "*.*")])
    if file_path:
        # Process the selected file (you can replace this with your own logic)
        start_read_file(file_path)

# Callback function to handle 'File history' button click
def file_history():
    # Read file history, show pop-up and return the selected filepath
    history = hist.read_history(history_file)
    file_path = hist.select_history_filepath(history)  # No value is returned, therefore another read action below
    file_path2 = hist.selected_filepath
    if file_path:
        # Process the selected file (you can replace this with your own logic)
        start_read_file(file_path)

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

# Create three vertical frames (i) and two horizontal ones (j)
rows, cols = 3,2
# initialise vertical frame-array (1D) and their subframes as 2D matrix
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5, )
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j==0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=False, padx=5, pady=5)

'''
Add elements to the frames
'''
'''
First row
'''
# Frame-titel
data_input_img = Image.open(data_input_image)
# data_input_img = data_input_img.resize((500, 500), Image.LANCZOS)
data_input_label = ctk.CTkLabel(frame_vert[0][0], text=f" Data input ", image=ctk.CTkImage(data_input_img), compound='left', font=title_font)
data_input_label.pack(side=tk.TOP, padx=2, pady=2)
label_0_0 = ctk.CTkLabel(frame_vert[0][0], text=f"Select the data source")
label_0_0.pack(side=tk.TOP, padx=2, pady=2)

# Data-inputkeuze (frame[0][0])
data_input_choices = ["SQL", "File"]
sql_input_img = ctk.CTkImage(light_image=Image.open(sql_input_image), dark_image=Image.open(sql_input_image))
datafile_input_img = ctk.CTkImage(light_image=Image.open(datafile_input_image), dark_image=Image.open(datafile_input_image))
#sql_input_img = sql_input_img.resize((100, 100), Image.LANCZOS)
#datafile_input_img = datafile_input_img.resize((100, 100), Image.LANCZOS)
data_input_segbut = ctk.CTkSegmentedButton(frame_vert[0][0], values=data_input_choices, command=callback, dynamic_resizing=True, fg_color=sgmntd_bttn_fg_color)  # fg_color="#3A7EBF")
data_input_segbut._buttons_dict["SQL"].configure(image=sql_input_img)
data_input_segbut._buttons_dict["File"].configure(image=datafile_input_img)
data_input_segbut.configure(state="disabled")  # to be removed later
data_input_segbut.pack( padx=5, pady=5)

# Intro label in second frame
# Assume a grid of 2 small columns and a wide one
label_0_1 = ctk.CTkLabel(frame_vert[0][1], text=f"Select a data file")
label_0_1.grid(column=0, row=0, sticky="nw", padx=2, pady=2)

# Create an "Import File" button
open_folder_img = ctk.CTkImage(light_image=Image.open(open_folder_image), dark_image=Image.open(open_folder_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="Select file", image=open_folder_img, compound='left', command=import_file)
file_import_button.grid(column=0, row=1, sticky="nw", padx=2, pady=2)

# Create a "File history" button
open_folder_img = ctk.CTkImage(light_image=Image.open(file_history_image), dark_image=Image.open(file_history_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="File history", image=open_folder_img, compound='left', command=file_history)
file_import_button.grid(column=0, row=2, sticky="nw", padx=2, pady=2)

# Create label in second frame with selected filepath
label_0_1_2 = ctk.CTkLabel(frame_vert[0][1], text=f" Filepath: (empty)")
label_0_1_2.grid(column=0, row=3, sticky="nw", padx=2, pady=2)

# Create label in second frame to indicate status (read header, read file)
label_0_1_3 = ctk.CTkLabel(frame_vert[0][1], text=f" ")  # empty when no action happens
label_0_1_3.grid(column=0, row=4, sticky="nw", padx=2, pady=2)

# Combobox to know datetime column
combobox_label_dt = ctk.CTkLabel(frame_vert[0][1], text="Choose datetime column")
combobox_label_dt.grid(column=1, row=0, sticky="nw", padx=2, pady=2)
combobox_dt_var = tk.StringVar(frame_vert[0][1], "empty")  # The visible entry in combobox
combobox_dt = ctk.CTkComboBox(frame_vert[0][1], values=["empty"])
combobox_dt['state'] = 'readonly'
combobox_dt.grid(column=1, row=1, sticky="nw", padx=2, pady=2)

# Combobox to know datetime format
combobox_label_dtfor = ctk.CTkLabel(frame_vert[0][1], text="Select or write datetime format")
combobox_label_dtfor.grid(column=1, row=2, sticky="nw", padx=2, pady=0)
combobox_dtfor = ctk.CTkComboBox(frame_vert[0][1], values=["%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M"])
combobox_dtfor.grid(column=1, row=3, sticky="nw", padx=2, pady=0)

# Create a "Read file" button
read_file_img = ctk.CTkImage(light_image=Image.open(file_history_image), dark_image=Image.open(read_file_image))
file_import_button = ctk.CTkButton(frame_vert[0][1], text="Read file", image=open_folder_img, compound='left', state= "disabled", command=read_file())
file_import_button.grid(column=1, row=4, sticky="nw", padx=2, pady=4)



'''
Second row
'''
# Frame-titel
data_selection_img = Image.open(data_selection_image)
# data_input_img = data_input_img.resize((500, 500), Image.LANCZOS)
data_selection_label = ctk.CTkLabel(frame_vert[1][0], text=f" Data selection ", image=ctk.CTkImage(data_selection_img), compound='left', font=title_font)
data_selection_label.pack(side=tk.TOP, padx=2, pady=5)

# Combobox-voorbeeld
combobox_label1 = ctk.CTkLabel(frame_vert[1][0], text="Combobox 1")
combobox_label1.pack(side=tk.TOP, padx=2, pady=0)
combobox1 = ctk.CTkComboBox(frame_vert[1][0], values=["Option 1", "Option 2", "Option 3"])
combobox1.pack(side=tk.TOP, padx=2, pady=2)

# Arbitrary label in second frame
label_1_1 = ctk.CTkLabel(frame_vert[1][1], text=f" Lorem ypsilon ")
label_1_1.pack(side=tk.TOP, padx=2, pady=2)

# Table in second frame
value = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
table = CTkTable(master=frame_vert[1][1], row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=5, pady=5)

# Third row
# Frame-titel
plots_img = Image.open(plots_image)
# data_input_img = data_input_img.resize((500, 500), Image.LANCZOS)
plots_label = ctk.CTkLabel(frame_vert[2][0], text=f" Plotting ", image=ctk.CTkImage(plots_img), compound='left', font=title_font)
plots_label.pack(side=tk.TOP, padx=2, pady=5)


# OLD
label2 = ctk.CTkLabel(frame_vert[i][1], text=f"Label in Frame {frame_hor[i]} {i}")
label2.pack(side=tk.RIGHT, padx=10, pady=10)
button = ctk.CTkButton(frame_vert[i][0], text="Click Me", command=lambda l=label2: button_click(l))
button.pack(padx=10, pady=10)

# Add an entry widget to the first vertical frame of the first horizontal frame
entry = ctk.CTkEntry(frame_vert[2][0])
entry.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
