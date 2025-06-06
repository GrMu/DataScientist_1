"""
This is the main vi of a data aggregation and visualisation project.
"""

# Import
import customtkinter as ctk
import tkinter as tk
from PIL import Image

# Paths
iconpath = "images/vito-logo_blue_text_2.ico"

# Settings
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Initialize the main window
root = ctk.CTk()
root.title('Data aggregation and visualisation')
root.iconbitmap(iconpath)  # ("images/smiley3.ico")  # ('images/codemy.ico')
root.geometry("600x600")
root.minsize(400, 400)


# Function to handle button click
def button_click(label):
    label.configure(text="Button Clicked!")


# Create three horizontal frames
rows, cols = 3,2
# initialise vertical frame-array (1D) and their subframes as 2D matrix
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]
print("frame_hor: ", frame_hor)
print("frame_vert: ", frame_vert)

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5, )
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j==0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=False, padx=5, pady=5)

    # Add elements to the vertical frames
    label = ctk.CTkLabel(frame_vert[i][1], text=f"Label in Frame {frame_hor[i]} {i}")
    label.pack(side=tk.LEFT, padx=10, pady=10)
    label2 = ctk.CTkLabel(frame_vert[i][1], text=f"Label in Frame {frame_hor[i]} {i}")
    label2.pack(side=tk.RIGHT, padx=10, pady=10)
    button = ctk.CTkButton(frame_vert[i][0], text="Click Me", command=lambda l=label: button_click(l))
    button.pack(padx=10, pady=10)

# Add an entry widget to the first vertical frame of the first horizontal frame
entry = ctk.CTkEntry(frame_vert[2][0])
entry.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
