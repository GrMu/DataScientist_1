"""
This is the main module of a data aggregation and visualisation project.

It creates the GUI structure and receives+sends data between the subframes
Subframes are loaded depending on the user choices.
"""
'''
Import
'''

# Libraries
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from CTkTable import *
from PIL import Image
from pandas import Timestamp as pd_timestamp
import datetime

# Own routines
import subroutines.GUI_parts.GUI_file_handling as file_handl
import subroutines.GUI_parts.GUI_plot_1 as plot
import subroutines.GUI_parts.GUI_aggr_1 as GUI_aggr
import subroutines.GUI_parts.CustomTabView as CustTabView
import subroutines.GUI_parts.GUI_file_export as export

# Image paths
data_input_image = "images/VITO_iconen_datagebruik--data_3.png"  # tab_image-glasses.png"
sql_input_image = "images/sql-server2-5.png"  #fichier-sql.png"  #  serveur-sql.png
datafile_input_image = "images/csv.png"  # csv.png
data_selection_image = "images/VITO_iconen_datagebruik--inzicht_3.png"  # tab_image-export.png"
plots_image = "images/VITO_iconen_datagebruik--kracht_3.png"  # tab_image-graph.png"
tab_info_image = "images/tab_image-intro.png"
tab_graph_image = "images/tab_image-graph.png"
tab_aggr_image = "images/tab_image-input.png"
tab_export_image = "images/tab_image-export.png"
tab_help_image = "images/tab_image-help.png"

# Other paths
# --

# Settings
look = "EnergyVille"  # "VITO" or "EnergyVille"

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

# Show error to the user
'''
This does not work yet: ValueError and other ones are not captured here. 
'''

# Show error to the user
'''
This does not work yet: ValueError and other ones are not captured here. 
'''
class CustomTk(tk.Tk):
    def report_callback_exception(self, exc, val, tb):
        print("Exception caught:", val)   # Debugging print statement
        messagebox.showerror("Error", message=str(val))


# Callback function to handle data that comes out of subframe!
def receive_data(data, data_info):
    # Contents in data_info that matters here: 'datetime_column' (can be 'no datetime'), 'datetime_format'
    now_rounded = get_now()
    # print(f"Main module: data received: \n{data}\n at {now_rounded}")
    print(f"Main module: data_info received: \n{data_info}\n at {now_rounded}")
    status_label.configure(text=f"data received at {now_rounded}")
    plot.Place_frame1(tab_graph, data, data_info)
    if data_info['datetime_column'] != 'no datetime':
        GUI_aggr.Place_frame1(tab_aggr, data, data_info)
    export.Place_frame1(tab_export, data, data_info)

# Callback function to handle segmented button clicks
#  It receives (!) also a callback once data is changed within the subframe
def data_source(value):
    print("segmented button clicked:", value)
    if value == data_input_choices_list[0] :  # sql
        pass  # Not implemented to do something yet
    elif value == data_input_choices_list[1]:  # file
        # breng frame_vert[0][1] als variabele naar GUI_file_handling
        file_handl.Place_frame1(frame_vert[0][1], receive_data)

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

# Create two vertical frames. In first one two horizontal ones. In lowest frame a Tabview frame
rows= 2
frame_hor = [0 for i in range(rows)]
# Using for-loop makes it easy expandable for future
for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5, )

# Fill first frame with two subframes
cols =2
frame_vert = [[0 for j in range(cols)] for i in range(rows)]
for j in range(cols):
    hulp = frame_hor[0]
    frame_vert[0][j] = ctk.CTkFrame(master=hulp, width=(100 if j==0 else 700))
    frame_vert[0][j].pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Create Tabview in second vertical frame
tabview = CustTabView.CustomTabview(master=root, height=1000, width=1400)
tabview.pack(padx=2, pady=2)

icon_intro = ctk.CTkImage(Image.open(tab_info_image))
icon_graph = ctk.CTkImage(Image.open(tab_graph_image))
icon_aggr = ctk.CTkImage(Image.open(tab_aggr_image))
icon_export = ctk.CTkImage(Image.open(tab_export_image))
icon_help = ctk.CTkImage(Image.open(tab_help_image))

tab_intro = tabview.add("Intro", icon_intro)
tab_graph = tabview.add("Graph", icon_graph)
tab_aggr = tabview.add("Aggregate", icon_aggr)
tab_export = tabview.add("Export", icon_export)
tab_help = tabview.add("Help", icon_help)
tab_ideas = tabview.add("Ideas")
tabview.set("Intro")  # set currently visible tab

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
data_selection_label = ctk.CTkLabel(frame_hor[1], text=f" Data visualisation and handling ", \
                        image=ctk.CTkImage(data_selection_img), compound='left', font=title_font)
data_selection_label.pack(side=tk.LEFT, padx=2, pady=5)
# Label about data status
status_label = ctk.CTkLabel( master=frame_hor[1], text="No data yet ",  width=10, height=5)
status_label.pack(side="left", padx=10)
'''
3️⃣ TabView
'''
greeting = ctk.CTkLabel( master=tab_intro, text="Hello, :-) ",  width=10, height=5)
greeting.pack()
greeting2 = ctk.CTkLabel(master=tab_intro, text=" (-: Hello ", width=20)
greeting2.pack()

# Run the main loop
root.mainloop()
