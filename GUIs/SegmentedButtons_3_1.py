from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Desserts and Calories")
        self.geometry("400x300")
        self.D = [
            ("Doughnuts", 300),
            ("Pumpkin Pie", 243),
            ("Fudge", 411),
            ("Brownies", 466),
            ("Cheesecake", 321),
        ]
        self.selected = IntVar()
        for dessert, calories in self.D:
            self.rb = CTkRadioButton(self, text=dessert, variable=self.selected, value=calories,
                                     command=self.show_calories)
            self.rb.pack(pady=10)
        self.show = CTkLabel(self, text="")
        self.show.pack()

    def show_calories(self):
        self.show.pack_forget()
        self.show = CTkLabel(self, text=f"I have {self.selected.get()} calories!")
        self.show.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
