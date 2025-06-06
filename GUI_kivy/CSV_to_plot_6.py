
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import matplotlib.pyplot as plt

class MyApp(App):
    def build(self):
        root = FloatLayout()

        # Add Background Image
        background = Image(source='Background_snake.png', allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        # Add a semi-transparent black overlay
        with root.canvas:
            Color(0, 0, 0, 0.7)  # RGBA: black with 50% opacity
            self.rect = Rectangle(size=root.size, pos=root.pos)
            root.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        layout.add_widget(Widget(size_hint_y=0.1))  # Wat lege ruimte bovenaan

        # Add Comboboxes with space between them
        combo_layout1 = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        for i in range(3):
            spinner = Spinner(text=f'Option { i +1}', values=('Option 1', 'Option 2', 'Option 3'), size_hint_y=None, height=30)
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
            label = Label(text=f'Label { i +1}', size_hint_y=None, height=30)
            label_layout1.add_widget(label)
        layout.add_widget(label_layout1)
        i = 2
        label = Label(text=f'Label {i + 1}', size_hint_y=None, height=30)
        layout.add_widget(label)

        # Add Buttons with images
        for i in range(3):
            button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
            image = Image(source=f'images/tab_image-{ i +1}.png', size_hint_x=0.1 )  # width=30
            button = Button(text=f'Button { i +1}', size_hint_x=0.6, size_hint_y=None, height=30)
            button_layout.add_widget(image)
            button_layout.add_widget(button)
            button_layout.add_widget(Widget(size_hint_x=0.2))  # Voeg lege ruimte rechts toe
            layout.add_widget(button_layout)

        # Add Table
        table_layout = GridLayout(cols=3, size_hint_y=0.3)
        for i in range(9):  # 3x3 table
            table_layout.add_widget(Label(text=f'Cell { i +1}', size_hint_y=None, height=30))
        layout.add_widget(table_layout)

        # Generate and Add Graphs Horizontally
        graph_layout = BoxLayout(orientation='horizontal', size_hint_y=1)
        for i in range(3):
            fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size
            ax.plot([0, 1, 2, 3], [i, i+ 1, i + 2, i + 3])
            graph_path = f'graph_{i + 1}.png'
            fig.savefig(graph_path)
            graph_layout.add_widget(Image(source=graph_path, size_hint=(1, 1)))  # Increase image size
        layout.add_widget(graph_layout)

        root.add_widget(layout)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MyApp().run()

