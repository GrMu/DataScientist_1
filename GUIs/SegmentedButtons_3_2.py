# Importing necessary module
from customtkinter import CTk, CTkSegmentedButton

# Creating an App class that inherits from CTk (Custom Tkinter)
class App(CTk):
    def __init__(self):
        super().__init__() # Calling the constructor of the superclass (CTk)
        self.title("SegmentedButton Example")

        # Creating a CTkSegmentedButton instance within the window, specifying values and a callback function
        self.se = CTkSegmentedButton(self, values=["Value 1", "Value 2", "Value 3"],
                                                     command=self.callback)
        self.se.pack(padx=20, pady=20)

    # Callback function to handle segmented button clicks
    def callback(self, value):
        print("segmented button clicked:", value)

app = App()
app.mainloop()
