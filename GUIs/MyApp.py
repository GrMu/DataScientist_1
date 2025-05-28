from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
import matplotlib.pyplot as plt

class MyApp(App):
    def build(self):
        # Load the .kv file
        Builder.load_file('myapp.kv')
        root = FloatLayout()

        # Add Background Image
        background = Image(source='Background_snake.png', allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        # Add a semi-transparent black overlay
        with root.canvas:
            Color(0, 0, 0, 0.7)  # RGBA: black with 70% opacity
            self.rect = Rectangle(size=root.size, pos=root.pos)
            root.bind(size=self._update_rect, pos=self._update_rect)

        # Add the main layout from the .kv file
        layout = Builder.load_file('myapp.kv').children[0]
        root.add_widget(layout)

        return root

    def on_start(self):
        layout = self.root.children[1]

        # Generate and Add Graphs Horizontally
        graph_layout = layout.ids.graph_layout
        for i in range(3):
            fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size
            ax.plot([0, 1, 2, 3], [i, i + 1, i + 2, i + 3])
            graph_path = f'graph_{i + 1}.png'
            fig.savefig(graph_path)
            graph_layout.add_widget(Image(source=graph_path, size_hint=(1, 1)))  # Increase image size

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyApp().run()
