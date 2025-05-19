import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
    QTableView, QHeaderView, QSplitter
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Data inlezen
df = pd.read_csv('personeeldata.csv')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personeelsdata Overzicht")
        self.resize(1400, 800)

        self.data = df.copy()

        self.layout = QVBoxLayout(self)

        # --- Dropdown en Label
        dropdown_layout = QHBoxLayout()
        self.label = QLabel("Filter op Afdeling:")
        dropdown_layout.addWidget(self.label)

        afdelingen = ["Alle afdelingen"] + sorted(self.data['afdeling'].dropna().unique().tolist())
        self.combo = QComboBox()
        self.combo.addItems(afdelingen)
        self.combo.currentIndexChanged.connect(self.filter_data)
        dropdown_layout.addWidget(self.combo)

        self.layout.addLayout(dropdown_layout)

        # --- Splitter (boven tabel, onder grafieken)
        self.splitter = QSplitter(Qt.Vertical)

        # --- Tabel
        self.table = QTableView()
        self.model = QStandardItemModel()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table(self.data)

        self.splitter.addWidget(self.table)

        # --- Grafieken
        self.graph_splitter = QSplitter(Qt.Horizontal)

        # Grafiek 1: Gemiddelde loon
        self.figure1, self.ax1 = plt.subplots(figsize=(4, 3))
        self.canvas1 = FigureCanvas(self.figure1)

        # Grafiek 2: Bedrijfswagen
        self.figure2, self.ax2 = plt.subplots(figsize=(4, 3))
        self.canvas2 = FigureCanvas(self.figure2)

        # Grafiek 3: Geslacht
        self.figure3, self.ax3 = plt.subplots(figsize=(4, 3))
        self.canvas3 = FigureCanvas(self.figure3)

        self.graph_splitter.addWidget(self.canvas1)
        self.graph_splitter.addWidget(self.canvas2)
        self.graph_splitter.addWidget(self.canvas3)

        self.splitter.addWidget(self.graph_splitter)
        self.layout.addWidget(self.splitter)

        # Start met grafieken tekenen
        self.update_graphs(self.data)

    def load_table(self, data):
        self.model.clear()
        self.model.setColumnCount(len(data.columns))
        self.model.setHorizontalHeaderLabels(data.columns)

        for index, row in data.iterrows():
            items = [QStandardItem(str(val)) for val in row]
            self.model.appendRow(items)

    def filter_data(self):
        afdeling = self.combo.currentText()
        if afdeling == "Alle afdelingen":
            filtered_df = df
        else:
            filtered_df = df[df['afdeling'] == afdeling]

        self.data = filtered_df
        self.load_table(filtered_df)
        self.update_graphs(filtered_df)

    def update_graphs(self, data):
        # Gemiddelde lonen
        self.ax1.clear()
        gemiddelde_lonen = data.groupby('afdeling')['maandloon'].mean()
        gemiddelde_lonen.plot(kind='bar', ax=self.ax1, color='skyblue')
        self.ax1.set_title('Gemiddelde Lonen per Afdeling')
        self.ax1.set_ylabel('Loon')
        self.figure1.tight_layout()
        self.canvas1.draw()

        # Bedrijfswagen
        self.ax2.clear()
        bedrijfswagen_counts = data['bedrijfwagen'].value_counts()
        bedrijfswagen_counts.plot(kind='bar', ax=self.ax2, color=['green', 'red'])
        self.ax2.set_title('Bedrijfswagen (Wel/Niet)')
        self.ax2.set_ylabel('Aantal')
        self.figure2.tight_layout()
        self.canvas2.draw()

        # Geslacht
        self.ax3.clear()
        gender_counts = data['geslacht'].value_counts()
        self.ax3.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'pink'])
        self.ax3.set_title('Geslacht Verdeling')
        self.figure3.tight_layout()
        self.canvas3.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
