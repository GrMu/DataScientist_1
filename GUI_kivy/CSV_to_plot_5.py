
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import matplotlib.pyplot as plt

# create a background class which inherits the boxlayout class (trial)
class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    BoxLayout.source = r"C:\Users\mulderg\OneDrive - VITO\Documents\eigen\fotos_2025\IMG_20250526_092610.jpg"

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add Comboboxes with space between them
        combo_layout1 = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        for i in range(3):
            spinner = Spinner(text=f'Option {i+1}', values=('Option 1', 'Option 2', 'Option 3'), size_hint_y=None, height=30)
            combo_layout1.add_widget(spinner)
            if i < 2:  # Add space between comboboxes
                combo_layout1.add_widget(Widget(size_hint_x=0.1))
        layout.add_widget(combo_layout1)
        
        combo_layout2 = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        for j in range(2):
            i = j + 3
            spinner = Spinner(text=f'Option {i + 1}', values=('Option 1', 'Option 2', 'Option 3'), size_hint_y=None, height=30)
            combo_layout2.add_widget(spinner)
            if j < 1:  # Add space between comboboxes
                combo_layout2.add_widget(Widget(size_hint_x=0.1))
        layout.add_widget(combo_layout2)

        # Add Labels
        label_layout1 = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        for i in range(2):
            label = Label(text=f'Label {i+1}', size_hint_y=None, height=30)
            label_layout1.add_widget(label)
        layout.add_widget(label_layout1)
        i = 2
        label = Label(text=f'Label {i + 1}', size_hint_y=None, height=30)
        layout.add_widget(label)

        # Add Buttons
        for i in range(3):
            button = Button(text=f'Button {i+1}', size_hint_y=None, height=30)
            layout.add_widget(button)

        # Add Table
        table_layout = GridLayout(cols=3, size_hint_y=0.3)
        for i in range(9):  # 3x3 table
            table_layout.add_widget(Label(text=f'Cell {i+1}', size_hint_y=None, height=30))
        layout.add_widget(table_layout)

        # Generate and Add Graphs Horizontally
        graph_layout = BoxLayout(orientation='horizontal', size_hint_y=0.6)
        for i in range(3):
            fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size
            ax.plot([0, 1, 2, 3], [i, i+1, i+2, i+3])
            graph_path = f'graph_{i+1}.png'
            fig.savefig(graph_path)
            graph_layout.add_widget(Image(source=graph_path, size_hint=(1, 1), ))  # size=(800, 480); Increase image size
        layout.add_widget(graph_layout)

        return layout

if __name__ == '__main__':
    MyApp().run()
