import customtkinter as ctk

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter GUI")
root.geometry("600x400")


# Function to handle button click
def button_click():
    label.configure(text="Button Clicked!")


# Create three vertical frames
frame1 = ctk.CTkFrame(root)
frame1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame2 = ctk.CTkFrame(root)
frame2.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame3 = ctk.CTkFrame(root)
frame3.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Create two horizontal frames in each vertical frame and add elements
for frame in [frame1, frame2, frame3]:
    h_frame1 = ctk.CTkFrame(frame)
    h_frame1.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    h_frame2 = ctk.CTkFrame(frame)
    h_frame2.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    # Add elements to the horizontal frames
    label = ctk.CTkLabel(h_frame1, text="Label in Frame")
    label.pack(padx=10, pady=10)

    button = ctk.CTkButton(h_frame2, text="Click Me", command=button_click)
    button.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
