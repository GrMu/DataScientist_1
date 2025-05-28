import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from PIL import Image

# Create the main window
app = ctk.CTk()
app.geometry("800x600")
app.title("CustomTkinter GUI")

# Load images for buttons and logo
button_image = Image.open("images/tab_image-glasses.png")
logo_image = Image.open("images/vito-logo_blue_1.png")

# Resize the logo image to make it bigger
logo_image = logo_image.resize((200, 100), Image.LANCZOS)

# Create a frame for the scrollbars
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)

# Create a canvas and scrollbars
canvas = ctk.CTkCanvas(frame)
v_scrollbar = ctk.CTkScrollbar(frame, orientation="vertical", command=canvas.yview)
v_scrollbar.pack(side="right", fill="y")
h_scrollbar = ctk.CTkScrollbar(frame, orientation="horizontal", command=canvas.xview)
h_scrollbar.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Create another frame inside the canvas
inner_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Update scroll region
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

inner_frame.bind("<Configure>", update_scroll_region)

# Add logo at the top
logo_label = ctk.CTkLabel(inner_frame, image=ctk.CTkImage(logo_image))
logo_label.grid(row=0, columnspan=6, pady=10)

# Create a frame for the top part (buttons and comboboxes)
top_frame = ctk.CTkFrame(inner_frame)
top_frame.grid(row=1, columnspan=6, pady=10)

# Create labels and widgets in the top frame using a grid layout
label1 = ctk.CTkLabel(top_frame, text="Button Section")
label1.grid(row=0, column=0, pady=10, sticky="w")

button1 = ctk.CTkButton(top_frame, text="Button 1", image=ctk.CTkImage(button_image))
button1.grid(row=1, column=0, pady=5, sticky="w")

combobox_label1 = ctk.CTkLabel(top_frame, text="Combobox 1")
combobox_label1.grid(row=1, column=1, pady=5, padx=5)
combobox1 = ctk.CTkComboBox(top_frame, values=["Option 1", "Option 2", "Option 3"])
combobox1.grid(row=1, column=2, pady=5, padx=5)

combobox_label2 = ctk.CTkLabel(top_frame, text="Combobox 2")
combobox_label2.grid(row=1, column=3, pady=5, padx=5)
combobox2 = ctk.CTkComboBox(top_frame, values=["Option 1", "Option 2", "Option 3"])
combobox2.grid(row=1, column=4, pady=5, padx=5)

button2 = ctk.CTkButton(top_frame, text="Button 2", image=ctk.CTkImage(button_image))
button2.grid(row=2, column=0, pady=5, sticky="w")

combobox_label3 = ctk.CTkLabel(top_frame, text="Combobox 3")
combobox_label3.grid(row=2, column=1, pady=5, padx=5)
combobox3 = ctk.CTkComboBox(top_frame, values=["Option 1", "Option 2", "Option 3"])
combobox3.grid(row=2, column=2, pady=5, padx=5)

radiobutton_var = ctk.StringVar(value="Choice 1")
radiobutton_label = ctk.CTkLabel(top_frame, text="Radiobuttons")
radiobutton_label.grid(row=2, column=3, pady=5)
radiobutton1 = ctk.CTkRadioButton(top_frame, text="Choice 1", variable=radiobutton_var, value="Choice 1")
radiobutton1.grid(row=2, column=4, pady=5)

radiobutton2 = ctk.CTkRadioButton(top_frame, text="Choice 2", variable=radiobutton_var, value="Choice 2")
radiobutton2.grid(row=3, column=4, pady=5)

radiobutton3 = ctk.CTkRadioButton(top_frame, text="Choice 3", variable=radiobutton_var, value="Choice 3")
radiobutton3.grid(row=4, column=4, pady=5)

button3 = ctk.CTkButton(top_frame, text="Button 3", image=ctk.CTkImage(button_image))
button3.grid(row=3, column=0, pady=5, sticky="w")

combobox_label4 = ctk.CTkLabel(top_frame, text="Combobox 4")
combobox_label4.grid(row=3, column=1, pady=5, padx=5)
combobox4 = ctk.CTkComboBox(top_frame, values=["Option 1", "Option 2", "Option 3"])
combobox4.grid(row=3, column=2, pady=5, padx=5)

combobox_label5 = ctk.CTkLabel(top_frame, text="Combobox 5")
combobox_label5.grid(row=4, column=1, pady=5)
combobox5 = ctk.CTkComboBox(top_frame, values=["Option 1", "Option 2", "Option 3"])
combobox5.grid(row=4, column=2, pady=5, padx=5)

label4 = ctk.CTkLabel(inner_frame, text="Filepath Control Section")
label4.grid(row=2, columnspan=6, pady=10)

filepath_entry = ctk.CTkEntry(inner_frame)
filepath_entry.grid(row=3, columnspan=6, pady=5)

# Create a frame for the table section
table_frame = ctk.CTkFrame(inner_frame)
table_frame.grid(row=4, columnspan=6, pady=10)

label5 = ctk.CTkLabel(table_frame, text="Table Section")
label5.grid(row=0, columnspan=6, pady=10)

# Create a sample table using pandas DataFrame
data = {
    "Column 1": ["Row 1 1234567890", "Row 2", "Row 3"],
    "Column 2": ["Data A", "Data B &é'(§è!çà", "Data C"],
    "Column 3": ["Value X", "Value Y", "Value Z |@#{[^{}"]
}
df = pd.DataFrame(data)
table_label = ctk.CTkLabel(table_frame, text=df.to_string(index=False, col_space=20))
table_label.grid(row=1, columnspan=6)

label6 = ctk.CTkLabel(inner_frame, text="Graphs Section")
label6.grid(row=5, columnspan=6)

# Create sample graphs using matplotlib
fig1, ax1 = plt.subplots()
ax1.plot([0, 1, 2], [0, 1, 4])
ax1.set_title("Graph 1")

fig2, ax2 = plt.subplots()
ax2.plot([0, 1, 2], [0, -1, -4])
ax2.set_title("Graph 2")

fig3, ax3 = plt.subplots()
ax3.plot([0, 1, 2], [0, -0.5, -0.25])
ax3.set_title("Graph 3")

# Display graphs in the GUI horizontally
canvas1 = FigureCanvasTkAgg(fig1, master=inner_frame)
canvas1.get_tk_widget().grid(row=6, column=0, pady=10)

canvas2 = FigureCanvasTkAgg(fig2, master=inner_frame)
canvas2.get_tk_widget().grid(row=6, column=1, pady=10)

canvas3 = FigureCanvasTkAgg(fig3, master=inner_frame)
canvas3.get_tk_widget().grid(row=6, column=2, pady=10)

# Run the application
app.mainloop()
