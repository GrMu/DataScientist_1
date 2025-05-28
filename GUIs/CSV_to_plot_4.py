
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add Comboboxes
        for i in range(5):
            spinner = Spinner(text=f'Option {i+1}', values=('Option 1', 'Option 2', 'Option 3'))
            layout.add_widget(spinner)

        # Add Labels
        for i in range(3):
            label = Label(text=f'Label {i+1}')
            layout.add_widget(label)

        # Add Buttons
        for i in range(3):
            button = Button(text=f'Button {i+1}')
            layout.add_widget(button)

        # Add Table
        table_layout = GridLayout(cols=3)
        for i in range(9):  # 3x3 table
            table_layout.add_widget(Label(text=f'Cell {i+1}'))
        layout.add_widget(table_layout)

        # Add Graphs
        for i in range(3):
            fig, ax = plt.subplots()
            ax.plot([0, 1, 2, 3], [i, i+1, i+2, i+3])
            layout.add_widget(FigureCanvasKivyAgg(fig))

        return layout

if __name__ == '__main__':
    MyApp().run()
