"""
This is the main module of a distributed GUI based on classes.

Approach:
main module creates the main GUI frames.
It calls another module that places an interactive frame.
Once data is generated in that module, it is sent back to the main module with help
of a callback functionality.
"""

# Libraries
import customtkinter as ctk
import DataScientist_1.GUIs.Distributed_GUI_methods.Distributed_GUI.Frame1_class_based_1 as frame1

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Data handling and visualisation')
        self.root.geometry("1000x600")  # width x height
        self.root.minsize(400, 400)

        # Create two vertical frames (i) and two horizontal ones (j)
        rows, cols = 2, 2
        self.frame_hor = [0 for i in range(rows)]
        self.frame_vert = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            self.frame_hor[i] = ctk.CTkFrame(self.root, height=20)
            self.frame_hor[i].pack(side="top", fill="both", expand=True, padx=5, pady=5)
            for j in range(cols):
                hulp = self.frame_hor[i]
                self.frame_vert[i][j] = ctk.CTkFrame(master=hulp, width=(100 if j == 0 else 600))
                self.frame_vert[i][j].pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Label to show data
        self.data_label = ctk.CTkLabel(self.frame_vert[0][0], text=f" Data (empty)")
        self.data_label.pack(side=ctk.TOP, padx=2, pady=2)

        # Initialise/ start the subframe and
        # pass the callback function to the frame
        self.frame1 = frame1.Frame1(self.frame_vert[0][1], self.receive_data)

    # Callback function to handle data that comes out of subframe!
    def receive_data(self, data):
        print("data received:", data)
        self.data_label.configure(text=f"data: {data}")

if __name__ == '__main__':
    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()
