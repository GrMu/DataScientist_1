import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data inlezen
df = pd.read_csv('personeeldata.csv')

# Maak een hoofdvenster
root = tk.Tk()
root.title("Personeelsdata Overzicht")

# Frames aanmaken
top_frame = tk.Frame(root)  # Nieuw: apart frame voor dropdown + label
top_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=5)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)

frame1.grid(row=1, column=0, columnspan=3, sticky="nsew")
frame2.grid(row=2, column=0, sticky="nsew")
frame3.grid(row=2, column=1, sticky="nsew")
frame4.grid(row=2, column=2, sticky="nsew")

# Configureer kolomgewichten zodat ze zich aanpassen
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=3)
root.grid_columnconfigure((0,1,2), weight=1)

# -------- Dropdownlijst voor filteren --------
tk.Label(top_frame, text="Filter op Afdeling: ").pack(side="left", padx=5)

afdelingen = ["Alle afdelingen"] + sorted(df['afdeling'].dropna().unique().tolist())
afdeling_var = tk.StringVar(value="Alle afdelingen")

afdeling_dropdown = ttk.Combobox(top_frame, textvariable=afdeling_var, values=afdelingen, state="readonly")
afdeling_dropdown.pack(side="left")

# -------- Frame 1: DataFrame tonen + Scrollbar --------
tree_frame = tk.Frame(frame1)
tree_frame.pack(expand=True, fill='both')

tree_scrollbar_y = tk.Scrollbar(tree_frame, orient="vertical")
tree_scrollbar_x = tk.Scrollbar(tree_frame, orient="horizontal")

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar_y.set, xscrollcommand=tree_scrollbar_x.set)
tree_scrollbar_y.config(command=tree.yview)
tree_scrollbar_x.config(command=tree.xview)

tree_scrollbar_y.pack(side="right", fill="y")
tree_scrollbar_x.pack(side="bottom", fill="x")
tree.pack(expand=True, fill='both')

# Kolommen instellen
tree["columns"] = list(df.columns)
tree["show"] = "headings"

for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Functie om data te laden
def load_treeview(data):
    tree.delete(*tree.get_children())
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

# Functie voor filteren
def filter_afdeling(event):
    selectie = afdeling_var.get()
    if selectie == "Alle afdelingen":
        filtered_df = df
    else:
        filtered_df = df[df['afdeling'] == selectie]
    load_treeview(filtered_df)

afdeling_dropdown.bind("<<ComboboxSelected>>", filter_afdeling)

# Start met alle data geladen
load_treeview(df)

# -------- Frame 2: Gemiddelde lonen per afdeling --------
fig2, ax2 = plt.subplots(figsize=(4,3))
gemiddelde_lonen = df.groupby('afdeling')['maandloon'].mean()
gemiddelde_lonen.plot(kind='bar', ax=ax2, color='skyblue')
ax2.set_title('Gemiddelde Lonen per Afdeling')
ax2.set_ylabel('Loon')

canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
canvas2.draw()
canvas2.get_tk_widget().pack(expand=True, fill='both')

# -------- Frame 3: Bedrijfswagen verdeling --------
fig3, ax3 = plt.subplots(figsize=(4,3))
bedrijfswagen_counts = df['bedrijfwagen'].value_counts()
bedrijfswagen_counts.plot(kind='bar', ax=ax3, color=['green', 'red'])
ax3.set_title('Bedrijfswagen (Wel/Niet)')
ax3.set_ylabel('Aantal')

canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
canvas3.draw()
canvas3.get_tk_widget().pack(expand=True, fill='both')

# -------- Frame 4: Aantal mannen vs vrouwen --------
fig4, ax4 = plt.subplots(figsize=(4,3))
gender_counts = df['geslacht'].value_counts()
ax4.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'pink'])
ax4.set_title('Geslacht Verdeling')

canvas4 = FigureCanvasTkAgg(fig4, master=frame4)
canvas4.draw()
canvas4.get_tk_widget().pack(expand=True, fill='both')

root.mainloop()
