import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.graphics.texture import Texture

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# kivy.require('2.0.0')

# --- Data inlezen
df = pd.read_csv('personeeldata.csv')


from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout

class TableView(RecycleView):
    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)

        self.layout = RecycleBoxLayout(default_size=(None, 30),
                                       default_size_hint=(1, None),
                                       size_hint=(1, None),
                                       orientation='vertical')
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.add_widget(self.layout)

        self.viewclass = 'Label'  # Belangrijk: gebruik standaard Label voor elk item

        self.data = []

    def update_table(self, dataframe):
        rows = dataframe.values.tolist()
        headers = dataframe.columns.tolist()

        # Data mooi maken: header + elke rij als string
        table_data = [', '.join(headers)]
        for row in rows:
            row_str = ', '.join(str(cell) for cell in row)
            table_data.append(row_str)

        self.data = [{'text': row, 'size_hint_y': None, 'height': 30} for row in table_data]



class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(orientation='vertical', **kwargs)

        # Data kopiëren
        self.df = df.copy()

        # Dropdown menu
        afdelingen = ["Alle afdelingen"] + sorted(self.df['afdeling'].dropna().unique().tolist())
        self.spinner = Spinner(
            text='Alle afdelingen',
            values=afdelingen,
            size_hint=(1, None),
            height=44
        )
        self.spinner.bind(text=self.update_filter)
        self.add_widget(self.spinner)

        # Tabel
        self.table = TableView()
        self.add_widget(self.table)

        # Layout voor grafieken
        self.graphs = BoxLayout(orientation='horizontal', size_hint=(1, 0.7))
        self.add_widget(self.graphs)

        # Grafiek placeholders
        self.graph1 = Image()
        self.graph2 = Image()
        self.graph3 = Image()

        self.graphs.add_widget(self.graph1)
        self.graphs.add_widget(self.graph2)
        self.graphs.add_widget(self.graph3)

        self.update_display(self.df)

    def update_filter(self, spinner, text):
        if text == "Alle afdelingen":
            filtered = self.df
        else:
            filtered = self.df[self.df['afdeling'] == text]

        self.update_display(filtered)

    def update_display(self, data):
        # Update de tabel
        self.table.update_table(data)

        # Update de grafieken
        self.update_graphs(data)

    def fig_to_texture(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)

        import PIL.Image
        pil_image = PIL.Image.open(buf).convert('RGBA')  # Open als RGBA
        img_data = pil_image.tobytes()

        texture = Texture.create(size=pil_image.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        texture.flip_vertical()
        plt.close(fig)
        return texture

    def update_graphs(self, data):
        # 1: Gemiddelde lonen
        fig1, ax1 = plt.subplots(figsize=(4,3))
        gemiddelde_lonen = data.groupby('afdeling')['maandloon'].mean()
        gemiddelde_lonen.plot(kind='bar', ax=ax1, color='skyblue')
        ax1.set_title('Gemiddelde Lonen')
        ax1.set_ylabel('Loon')
        self.graph1.texture = self.fig_to_texture(fig1)

        # 2: Bedrijfswagen
        fig2, ax2 = plt.subplots(figsize=(4,3))
        bedrijfswagen_counts = data['bedrijfwagen'].value_counts()
        bedrijfswagen_counts.plot(kind='bar', ax=ax2, color=['green', 'red'])
        ax2.set_title('Bedrijfswagen (Wel/Niet)')
        ax2.set_ylabel('Aantal')
        self.graph2.texture = self.fig_to_texture(fig2)

        # 3: Geslacht
        fig3, ax3 = plt.subplots(figsize=(4,3))
        gender_counts = data['geslacht'].value_counts()
        ax3.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'pink'])
        ax3.set_title('Geslacht Verdeling')
        self.graph3.texture = self.fig_to_texture(fig3)


class PersoneelsApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    PersoneelsApp().run()
