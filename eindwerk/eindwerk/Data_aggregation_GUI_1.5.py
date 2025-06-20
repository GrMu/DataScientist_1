"""
This is the main module of a data aggregation and visualisation project.

It creates the GUI structure and receives+sends data between the subframes
Subframes are loaded depending on the user choices.
"""
'''
Import
'''
import tkinter as tk

# Libraries
import customtkinter as ctk
from CTkTable import *
from PIL import Image
from pandas import Timestamp as pd_timestamp
import datetime

# Own routines
import subroutines.GUI_parts.GUI_file_handling as file_handl

# Image paths
data_input_image = "images/VITO_iconen_datagebruik--data_3.png"  # tab_image-glasses.png"
sql_input_image = "images/sql-server2-5.png"  #fichier-sql.png"  #  serveur-sql.png
datafile_input_image = "images/csv.png"  # csv.png
data_selection_image = "images/VITO_iconen_datagebruik--inzicht_3.png"  # tab_image-export.png"
plots_image = "images/VITO_iconen_datagebruik--kracht_3.png"  # tab_image-graph.png"

# Other paths
# --

# Settings
look = "VITO"  # "VITO" or "EnergyVille"

if look == "VITO":
    ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    sgmntd_bttn_fg_color = "#3A7EBF"  # fg_color="#3A7EBF"), "#2CC985"
    iconpath = "images/vito-logo_blue_text_2.ico"  # tab_image-glasses.ico"  # vito-logo_blue_text_2.ico"
else:
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
    sgmntd_bttn_fg_color = "#2CC985"  # fg_color="#3A7EBF")
    iconpath = "images/EnergyVille.ico"  # tab_image-glasses.ico"  # vito-logo_blue_text_2.ico"

data_input_choices_list = ["SQL", "File"]

'''
Functions needed before the event handling functions
'''

def get_now():
    # Show the moment that is clicked in status label
    now = datetime.datetime.now()
    pd_now = pd_timestamp(now)
    freq = '1s'
    pd_round = pd_now.round(freq)
    now_rounded = pd_round.to_pydatetime()
    return now_rounded

# Callback function to handle data that comes out of subframe!
def receive_data(data):
    now_rounded = get_now()
    print(f"data received: {data} at {now_rounded}")
    label_1_1.configure(text=f"data received at {now_rounded}")

# Callback function to handle segmented button clicks
#  It receives (!) also a callback once data is changed within the subframe
def data_source(value):
    print("segmented button clicked:", value)
    if value == data_input_choices_list[0] :  # sql
        pass  # Not implemented to do something yet
    elif value == data_input_choices_list[1]:  # file
        # breng frame_vert[0][1] als variabele naar GUI_file_handling
        file_handl.Place_frame1(frame_vert[0][1], receive_data)

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
label_0_0 = ctk.CTkLabel(frame_vert[0][0], text=f"Select the data source")
label_0_0.pack(side=tk.TOP, padx=2, pady=2)

# Data-inputkeuze (frame[0][0])
data_input_choices = data_input_choices_list  # ["SQL", "File"]
sql_input_img = ctk.CTkImage(light_image=Image.open(sql_input_image), dark_image=Image.open(sql_input_image))
datafile_input_img = ctk.CTkImage(light_image=Image.open(datafile_input_image), \
                                  dark_image=Image.open(datafile_input_image))
#sql_input_img = sql_input_img.resize((100, 100), Image.LANCZOS)
#datafile_input_img = datafile_input_img.resize((100, 100), Image.LANCZOS)
data_input_segbut = ctk.CTkSegmentedButton(frame_vert[0][0], values=data_input_choices, command=data_source, \
                        dynamic_resizing=True, fg_color=sgmntd_bttn_fg_color)  # fg_color="#3A7EBF")
data_input_segbut._buttons_dict["SQL"].configure(image=sql_input_img)
data_input_segbut._buttons_dict["File"].configure(image=datafile_input_img)
# data_input_segbut.configure(state="disabled")  # to be removed later
data_input_segbut.pack( padx=5, pady=5)

'''
2️⃣ Second row
'''
# Frame-titel
data_selection_img = Image.open(data_selection_image)
# data_input_img = data_input_img.resize((500, 500), Image.LANCZOS)
data_selection_label = ctk.CTkLabel(frame_vert[1][0], text=f" Data selection ", \
                        image=ctk.CTkImage(data_selection_img), compound='left', font=title_font)
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
'''
3️⃣ Third row
'''
# Frame-titel
plots_img = Image.open(plots_image)
plots_label = ctk.CTkLabel(frame_vert[2][0], text=f" Plotting ", image=ctk.CTkImage(plots_img), \
                           compound='left', font=title_font)
plots_label.pack(side=tk.TOP, padx=2, pady=5)


# OLD
label2 = ctk.CTkLabel(frame_vert[2][1], text=f"Label in Frame {frame_hor[2]} {1}")
label2.pack(side=tk.RIGHT, padx=10, pady=10)
button = ctk.CTkButton(frame_vert[2][0], text="Click Me", command=lambda l=label2: button_click(l))
button.pack(padx=10, pady=10)

# Add an entry widget to the first vertical frame of the first horizontal frame
entry = ctk.CTkEntry(frame_vert[2][0])
entry.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
