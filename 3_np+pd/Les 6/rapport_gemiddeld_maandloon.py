from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

# --- DATABASE CONNECTIE EN DATA OPHALEN ---
from connect_to_db import *

db = DBConnector("personeel1")
kolom_namen = db.geef_kolomnamen("medewerkers")
data = db.return_query_data("select * from medewerkers")
df = pd.DataFrame(data)
df.columns = kolom_namen

# --- GEMIDDELD LOON BEREKENEN ---
gemiddeld_loon_per_afdeling = df.groupby("afdeling")["maandloon"].mean().round(2)

# --- PDF AANMAKEN ---
pdf_filename = "rapport_gemiddeld_loon_per_afdeling.pdf"

with PdfPages(pdf_filename) as pdf:
    # --- FIGUUR MAKEN ---
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))  # 2 rijen, 1 kolom
    fig.subplots_adjust(hspace=0.4)  # Ruimte tussen onderdelen

    # --- TITEL TOEVOEGEN ---
    fig.suptitle("Rapport: Gemiddeld Maandloon per Afdeling", fontsize=16, fontweight="bold")

    # --- EERSTE DEEL: DATAFRAME TABEL ---
    axs[0].axis("off")  # Geen assen nodig
    table_data = [["Afdeling", "Gemiddeld Loon (€)"]] + list(gemiddeld_loon_per_afdeling.items())
    table = axs[0].table(cellText=table_data, cellLoc="center", loc="center", colWidths=[0.4, 0.4])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    axs[0].set_title("Gemiddeld Maandloon per Afdeling", fontsize=12, fontweight="bold")

    # --- TWEEDE DEEL: PIE CHART ---
    axs[1].pie(
        gemiddeld_loon_per_afdeling.values,
        labels=gemiddeld_loon_per_afdeling.index,
        autopct="%1.2f%%",
        startangle=140,
        colors=plt.cm.Paired.colors,
    )
    axs[1].set_title("Verdeling Gemiddeld Maandloon", fontsize=12, fontweight="bold")

    # --- PDF OPSLAAN ---
    pdf.savefig(fig, bbox_inches="tight")
    plt.close()

print(f"PDF opgeslagen als: {pdf_filename}")
