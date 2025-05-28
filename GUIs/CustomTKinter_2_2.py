import customtkinter as ctk

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter GUI")
root.geometry("800x400")


# Function to handle button click
def button_click(label):
    label.configure(text="Button Clicked!")


# Create three horizontal frames
h_frame1 = ctk.CTkFrame(root)
h_frame1.pack(side="top", fill="both", expand=True, padx=10, pady=10)

h_frame2 = ctk.CTkFrame(root)
h_frame2.pack(side="top", fill="both", expand=True, padx=10, pady=10)

h_frame3 = ctk.CTkFrame(root)
h_frame3.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# Create two vertical frames in each horizontal frame and add elements
for h_frame in [h_frame1, h_frame2, h_frame3]:
    v_frame1 = ctk.CTkFrame(h_frame, width=100)
    v_frame1.pack(side="left", fill="both", expand=False, padx=5, pady=5)

    v_frame2 = ctk.CTkFrame(h_frame, width=300)
    v_frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    # Add elements to the vertical frames
    label = ctk.CTkLabel(v_frame1, text="Label in Frame")
    label.pack(padx=10, pady=10)

    button = ctk.CTkButton(v_frame2, text="Click Me", command=lambda l=label: button_click(l))
    button.pack(padx=10, pady=10)

# Add an entry widget to the first vertical frame of the first horizontal frame
entry = ctk.CTkEntry(v_frame1)
entry.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
