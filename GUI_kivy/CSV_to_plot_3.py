import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivymd.uix.label import MDLabel
from plyer import filechooser
import matplotlib.pyplot as plt
import pandas as pd
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--intermediate_1500.csv"

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    md_bg_color: 1, 1, 1, 1  # Set background color to white
    
    # MDButton:
    Button:
        text: "Select Data File"
        size_hint_y: None
        height: dp(48)
        bg_color: 0.9, 0.9, 0.9, 1  # Light grey button background
        on_release: app.file_manager_open()

    Spinner:
        id: plot_spinner
        text: "Select Plot Type"
        values: ["Scatter", "Line", "Bar"]
        size_hint_y: None
        height: dp(48)
        bg_color: 0.9, 0.9, 0.9, 1  # Light grey button background
        on_text: app.update_plot()

    BoxLayout:
        id: plot_widget
        size_hint_y: None
        height: dp(400)
'''

class ScatterPlotApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        filechooser.open_file(on_selection=self.select_path)

    def select_path(self, selection):
        if selection:
            self.data_file = selection[0]
            self.root.ids.plot_spinner.text = "Scatter"
            self.update_plot()

    def update_plot(self, *args):
        if hasattr(self, 'data_file'):
            df = pd.read_csv(self.data_file)
            plt.clf()
            plot_type = self.root.ids.plot_spinner.text
            if plot_type == 'Scatter':
                plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
            elif plot_type == 'Line':
                plt.plot(df.iloc[:, 0], df.iloc[:, 1])
            elif plot_type == 'Bar':
                plt.bar(df.iloc[:, 0], df.iloc[:, 1])
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title(plot_type + ' Plot')
            plot_widget = self.root.ids.plot_widget
            plot_widget.clear_widgets()
            plot_widget.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        else:
            self.root.ids.plot_widget.clear_widgets()
            self.root.ids.plot_widget.add_widget(MDLabel(text='Select a file to display the plot'))

if __name__ == '__main__':
    ScatterPlotApp().run()
