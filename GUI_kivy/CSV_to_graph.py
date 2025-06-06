import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import pandas as pd


class ScatterPlotApp(App):
    def build(self):
        self.title = 'Scatter Plot GUI'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # File chooser button
        self.file_button = Button(text='Select Data File', size_hint=(1, 0.1))
        self.file_button.bind(on_release=self.show_file_chooser)
        layout.add_widget(self.file_button)

        # Combobox for plot type selection
        self.plot_spinner = Spinner(
            text='Select Plot Type',
            values=('Scatter', 'Line', 'Bar'),
            size_hint=(1, 0.1)
        )
        self.plot_spinner.bind(text=self.update_plot)
        layout.add_widget(self.plot_spinner)

        # Placeholder for the plot
        self.plot_widget = Label(text='Select a file to display the plot', size_hint=(1, 0.8))
        layout.add_widget(self.plot_widget)

        return layout

    def show_file_chooser(self, instance):
        content = FileChooserIconView()
        content.bind(on_submit=self.load_data)
        self.popup = Popup(title='Select Data File', content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def load_data(self, filechooser, selection, touch):
        if selection:
            self.data_file = selection[0]
            self.popup.dismiss()
            self.file_button.text = f'Selected: {self.data_file}'
            self.update_plot()

    def update_plot(self, *args):
        if hasattr(self, 'data_file'):
            df = pd.read_csv(self.data_file)
            plt.clf()
            if self.plot_spinner.text == 'Scatter':
                plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
            elif self.plot_spinner.text == 'Line':
                plt.plot(df.iloc[:, 0], df.iloc[:, 1])
            elif self.plot_spinner.text == 'Bar':
                plt.bar(df.iloc[:, 0], df.iloc[:, 1])
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title(self.plot_spinner.text + ' Plot')
            self.plot_widget.canvas.clear()
            self.plot_widget.canvas.add(FigureCanvasKivyAgg(plt.gcf()))
        else:
            self.plot_widget.text = 'Select a file to display the plot'


if __name__ == '__main__':
    ScatterPlotApp().run()
