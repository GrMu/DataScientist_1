"""
Create pop-up to select a row (filepath) and return this
"""
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

def select_filepath(history):
    def wrap_text(text, width):
        words = text.split('/')
        wrapped_text = ''
        line = ''
        for word in words:
            if len(line) + len(word) + 1 > width:
                wrapped_text += line + '/' + '\n'
                line = word
            else:
                if line:
                    line += '/'
                line += word
        wrapped_text += line
        return wrapped_text

    def calculate_row_height(text):
        return (text.count('\n') + 1) * 20  # Adjust multiplier as needed

    def on_doubleclick(event):
        item = tree.identify_row(event.y)
        if item:  # Check if a row was identified
            index = int(item.replace('item', '')) - 1
            original_filepath = history[index][0]
            bottom_label.configure(text=f"Filepath: {original_filepath}")
            root.after(1500, lambda: root.quit())
        else:
            bottom_label.config(text="Clicked on empty space.")

    def on_enter(event):
        on_doubleclick(event)

    def on_resize(event):
        new_width = tree.winfo_width()
        tree.column('Name', width=new_width - 40)
        for i, row in enumerate(history):
            for item in row:
                wrapped_item = wrap_text(item, new_width // 8)
                tree.item(f'item{i+1}', values=((i+1), wrapped_item))

    def search_and_highlight():
        search_term = search_entry.get().lower()
        for item in tree.get_children():
            values = tree.item(item, 'values')
            if search_term in values[1].lower():
                tree.item(item, tags=('highlight',))
            else:
                tree.item(item, tags=('normal',))
    '''
    Create the UI elements
    '''
    root = ctk.CTk()
    root.title("Select a file from the file history")
    root.geometry("500x600")
    root.minsize(200, 200)
    root.resizable(width=1, height=1)
    root.bind('<Configure>', on_resize)
    root.bind('<Return>', on_enter)

    # Create label at top and bottom
    top_label = ctk.CTkLabel(root, text="Double click on a filepath:")
    bottom_label = ctk.CTkLabel(root, text=f"Filepath: ")

    # Create the table with help of Treeview
    tree_frame = tk.Frame(root)
    tree = ttk.Treeview(tree_frame, columns=('Item', 'Name'), show='headings', selectmode="browse")
    tree.heading('Item', text='Item')
    tree.heading('Name', text='Filepath')
    tree.column('Item', width=40)
    tree.column('Name', width=150)
    style = ttk.Style()
    style.configure("Treeview", rowheight=50)
    for i, row in enumerate(history):
        for item in row:
            wrapped_item = wrap_text(item, 8)
            row_height = calculate_row_height(wrapped_item)
            tree.insert('', 'end', iid=f'item{i+1}', values=((i+1), wrapped_item), tags=('normal',))
    tree.tag_configure('highlight', background='light yellow')
    tree.tag_configure('normal', background='white')
    tree.bind('<Double-1>', on_doubleclick)
    scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)

    # Create a search possibility
    search_frame = tk.Frame(root)
    search_label = ctk.CTkLabel(search_frame, text="Search:")
    search_entry = ctk.CTkEntry(search_frame)
    search_button = ctk.CTkButton(search_frame, text="Search", command=search_and_highlight)

    # Place the elements
    top_label.pack(side='top', pady=10)
    tree_frame.pack(side='top', fill='x')
    scroll.pack(side='right', fill='y')
    tree.pack(side='top', fill='both', expand=True)
    search_frame.pack(side='top', fill='x')
    search_label.pack(side='left')
    search_entry.pack(side='left', fill='x', expand=True)
    search_button.pack(side='left')
    bottom_label.pack(side='top', fill='x', pady=10)

    root.mainloop()

    return bottom_label.cget("text").replace("Filepath: ", "")

# Example usage:
if __name__ == "__main__":
    history = [['C:/Users/mulderg/Downloads/10_October5.csv'], ['C:/Users/mulderg/Downloads/10_October4.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv']]
    selected_filepath = select_filepath(history)
    print(f"Selected filepath: {selected_filepath}")
