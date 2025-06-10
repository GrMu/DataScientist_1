import customtkinter as ctk
import tkinter as tk
from PIL import Image
from CTkTable import *
import subroutines.File_handling.Datafile_history_v2 as hist

iconpath = "images/EnergyVille.ico"
data_input_image = "images/VITO_iconen_datagebruik--data_3.png"
sql_input_image = "images/sql-server2-5.png"
datafile_input_image = "images/csv.png"
data_selection_image = "images/VITO_iconen_datagebruik--inzicht_3.png"
plots_image = "images/VITO_iconen_datagebruik--kracht_3.png"
open_folder_image = "images/dossier(1).png"
file_history_image = "images/dossier.png"

history_file = 'resources/Files/datafile_history.txt'

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def button_click(label):
    label.configure(text="Button Clicked!")

def callback(value):
    print("segmented button clicked:", value)

def import_file():
    file_path = ctk.filedialog.askopenfilename(title="Select a file",
                                           filetypes=[("Data files", "*.csv"), ("All files", "*.*")])
    if file_path:
        print("Selected file:", file_path)
        hist.add_to_history(history_file, file_path)
        label_0_1_2.configure(text=f"Filepath: {file_path}")

def file_history():
    history = hist.read_history(history_file)
    file_path = hist.select_history_filepath(history)
    print("Answer from select_history: ", file_path)
    if file_path:
        print("Selected file:", file_path)
        label_0_1_2.configure(text=f"Filepath: {file_path}")

root = ctk.CTk()
root.title('Data aggregation and visualisation')
root.iconbitmap(iconpath)
root.geometry("600x600")
root.minsize(400, 400)

title_font = ctk.CTkFont(family="Flexo Medium", size=20, weight="normal", slant="roman", underline=False, overstrike=False)

rows, cols = 3, 2
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j == 0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=False, padx=5, pady=5)

data_input_img = Image.open(data_input_image)
data_input_label = ctk.CTkLabel(frame_vert[0][0], text=f" Data input ", image=ctk.CTkImage(data_input_img), compound='left', font=title_font)
data_input_label.pack(side=tk.TOP, padx=2, pady=2)

data_input_choices = ["SQL", "File"]
sql_input_img = c