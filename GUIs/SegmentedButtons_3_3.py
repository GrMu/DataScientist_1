# Importing necessary module
from customtkinter import CTk, CTkSegmentedButton, CTkLabel

# Creating an App class that inherits from CTk (Custom Tkinter)
class App(CTk):
    def __init__(self):
        super().__init__() # Calling the constructor of the superclass (CTk)
        self.title("Color the text")
        self.colors = {"Pink": "#FFC0CB", "Yellow": "#BED754", "Orange": "#E3651D"}

        self.color_me = CTkLabel(self, text="Color Me!")
        self.color_me.pack(pady=10)
        # Creating a CTkSegmentedButton instance within the window, specifying values, callback function, text_color, and unselected_color.
        self.se = CTkSegmentedButton(self, values=["Pink", "Yellow", "Orange"],
                                                    command=self.callback,unselected_color="White", text_color="Black")
        self.se.pack(padx=20, pady=20)

    # Callback function to handle segmented button clicks
    def callback(self, value):
        self.se.configure(selected_color=self.colors[value], selected_hover_color=self.colors[value])
        self.color_me.configure(text_color=self.colors[value])

app = App()
app.mainloop()
