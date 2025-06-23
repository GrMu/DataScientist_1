
import customtkinter as ctk
from PIL import Image

class CustomTabview(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def add(self, name: str, icon: ctk.CTkImage = None):
        ref = super().add(name)
        if icon:
            button = self._segmented_button._buttons_dict[name]
            button.configure(image=icon, fg_color=button.cget("fg_color"))
        return ref

    def update_icon(self, name: str, icon: ctk.CTkImage):
        button = self._segmented_button._buttons_dict[name]
        button.configure(image=icon, fg_color=button.cget("fg_color"))

if __name__ == "__main__":
    # Create the main application window
    app = ctk.CTk()
    ctk.set_appearance_mode("light")  # dark, light

    # Create the custom tabview
    tabview = CustomTabview(app, fg_color="lightblue")
    tabview.pack(padx=20, pady=20)

    # Load images
    icon1 = ctk.CTkImage(Image.open("images/tab_image-intro.png"), size=(16, 16))
    icon2 = ctk.CTkImage(Image.open("images/tab_image-graph.png"), size=(16, 16))
    icon3 = ctk.CTkImage(Image.open("images/tab_image-input.png"), size=(16, 16))

    # Add tabs with images
    tabview.add("Tab 1", icon1)
    tabview.add("Tab 2", icon2)
    tabview.add("Tab 3", icon3)

    app.mainloop()
