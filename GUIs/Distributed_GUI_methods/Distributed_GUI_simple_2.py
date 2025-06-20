
# Libraries
import customtkinter as ctk

# Own routines
import DataScientist_1.GUIs.Distributed_GUI_methods.Distributed_GUI.Frame1_simple_1 as frame1

# Initialisation
masterframe = ""

# Callback function to handle data that comes out of subframe!
def receive_data(data):
    print("data received:", data)
    data_label.configure(text=f"data: {data}")

# Call the function to place a subframe in the submodule and
# pass the callback function to the frame
def open_subframe(masterframe, callback):
    frame1.Place_frame1(masterframe, callback)

# Create the GUI
root = ctk.CTk()
root.title('Data handling and visualisation')
root.geometry("1000x600")  # width x height
root.minsize(400, 400)

# Create two vertical frames (i) and two horizontal ones (j)
rows, cols = 2, 2
frame_hor = [0 for i in range(rows)]
frame_vert = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    frame_hor[i] = ctk.CTkFrame(root, height=20)
    frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for j in range(cols):
        hulp = frame_hor[i]
        frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j == 0 else 600))
        frame_vert[i][j].pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Label to open subframe and show returned data
label_0_1 = ctk.CTkLabel(frame_vert[0][0], text="Click to open subframe")
label_0_1.pack(side=ctk.TOP, padx=2, pady=2)

# Create a "Open subframe" button
open_subframe_button = ctk.CTkButton(frame_vert[0][0], text="Open subframe", \
     command=lambda: open_subframe(frame_vert[0][1], receive_data))
open_subframe_button.pack(side=ctk.TOP, padx=2, pady=2)

# Label to show returned data
data_label = ctk.CTkLabel(frame_vert[0][0], text="Data (empty)")
data_label.pack(side=ctk.TOP, padx=2, pady=2)

# Unnecessary label in another frame
data_label2 = ctk.CTkLabel(frame_vert[1][0], text="Data (empty)")
data_label2.pack(side=ctk.TOP, padx=2, pady=2)

# Run the main loop
root.mainloop()
