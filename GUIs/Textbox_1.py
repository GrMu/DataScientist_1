import customtkinter as ctk
import tkinter as tk
import pandas as pd

# Init customtkinter window
ctk.set_appearance_mode("system")  # 'dark' of 'light'
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("900x300")
root.title("Textbox over meerdere kolommen")

# Lees grote dataset om in textbox te plaatsen
FileWithPath = fr"C:\Users\mulderg\Downloads\1_January.csv"
column_name_datetime = 'Date'
time_format = "%Y-%m-%d %H:%M:%S"
data = pd.read_csv(FileWithPath, sep=";", decimal=".")
sample = data[:1024]

# Maak hoofdframe aan en gebruik grid
main_frame = ctk.CTkFrame(root)
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Zorg dat het hoofdvenster en frame meeschalen
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
for i in range(3):
    main_frame.grid_columnconfigure(i, weight=1, uniform="col")

# Plaats textbox over 3 kolommen
textbox = ctk.CTkTextbox(main_frame, wrap="none", height=150)
textbox.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

# Voeg wat inhoud toe
textbox.insert("1.0", "Deze textbox strekt zich uit over drie kolommen.\n"
                      "Gebruik grid(), columnspan en configureer je kolommen goed.\n\n"
                      "Voeg hier je data, logging of outputs toe...")
textbox.delete("1.0", "end")
textbox.insert("1.0", sample)

# Je kunt ook andere widgets in andere kolommen zetten ter controle
for col in range(3):
    button = ctk.CTkButton(main_frame, text=f"Knop {col+1}")
    button.grid(row=1, column=col, padx=5, pady=10, sticky="ew")

# Start de app
root.mainloop()
