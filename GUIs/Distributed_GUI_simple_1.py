"""
This is the main module of a distributed GUI.
This example is 'simple', i.e. without classes and without MVC approach.

Approach:
main module creates the main GUI frames.
It calls another module that places an interactive frame.
Once data is generated in that module, it is sent back to the main module with help
of a callback functionality.
"""

# Libraries
import customtkinter as ctk

# Own routines
import Distributed_GUI.Frame1_simple_1 as frame1

'''
Functions needed before the event handling functions
'''

# Callback function to handle segmented button clicks
def receive_data(data):
    print("data received:", data)
    data_label.configure(text=f"data: {data}")

'''
Create the GUI
'''
# Initialize the main window
root = ctk.CTk()
root.title('Data handling and visualisation')
root.geometry("1000x600")  # width x height
root.minsize(400, 400)

# Create two vertical frames (i) and two horizontal ones (j)
rows, cols = 2, 2
# initialise vertical frame-array (1D) and their subframes as 2D matrix
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j == 0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Label to show data
data_label = ctk.CTkLabel(frame_vert[0][0], text=f" Data (empty)")
data_label.pack(side=ctk.TOP, padx=2, pady=2)

# Unnecessary label in another frame
data_label2 = ctk.CTkLabel(frame_vert[1][0], text=f" Data (empty)")
data_label2.pack(side=ctk.TOP, padx=2, pady=2)

# Call the function to place a subframe in the submodule and
# pass the callback function to the frame
frame1.Place_frame1(frame_vert[0][1], receive_data)

# Run the main loop
root.mainloop()
