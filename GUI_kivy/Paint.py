from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
import kivy

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):
    def build(self):
        self.theme_cls.primary_palette = "Azure"
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()