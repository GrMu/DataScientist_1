import csv
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

max_nr_files = 30
history = [[]]
folder_iconpath = "images/filemap_3b.ico"
selected_filepath = None  # Global variable to store the selected filepath

def read_history(history_file):
    with open(history_file, mode='r', newline='', encoding='utf-8') as file:
        file_content = csv.reader(file)
        history = [row for row in file_content]
        print("history :", history)
    return history

def select_history_filepath(history):
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
        global selected_filepath
        item = tree.identify_row(event.y)
        if item:
            index = int(item.replace('item', '')) - 1
            original_filepath = history[index][0]
            width = poproot.winfo_screenwidth()
            wrapped_item = wrap_text(f"Filepath: {original_filepath}", width//20)
            bottom_label.configure(text=wrapped_item)
            selected_filepath = original_filepath  # Set the global variable
            poproot.after(1500, lambda: poproot.destroy())

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

    poproot = ctk.CTkToplevel()  # Use Toplevel instead of Tk
    poproot.title("Select a file from the file history")
    poproot.geometry("500x600")
    poproot.minsize(200, 200)
    poproot.resizable(width=True, height=True)
    poproot.iconbitmap(folder_iconpath)  # This does not work since overwritten by CTk after 200ms
    poproot.after(250, lambda: poproot.iconbitmap(folder_iconpath))
    poproot.bind('<Configure>', on_resize)
    poproot.bind('<Return>', on_enter)
    # Ensure the popup appears in front
    poproot.lift()
    poproot.attributes('-topmost', True)
    # poproot.after_idle(poproot.attributes, '-topmost', False)  # This most be omitted!

    top_label = ctk.CTkLabel(poproot, text="Double click on a filepath:")
    bottom_label = ctk.CTkLabel(poproot, text=f"Filepath: ")

    tree_frame = ctk.CTkFrame(poproot)
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

    search_frame = ctk.CTkFrame(poproot)
    search_label = ctk.CTkLabel(search_frame, text="Search:")
    search_entry = ctk.CTkEntry(search_frame)
    search_button = ctk.CTkButton(search_frame, text="Search", command=search_and_highlight)

    top_label.pack(side='top', pady=10)
    tree_frame.pack(side='top', fill='x', pady=10)
    scroll.pack(side='right', fill='y')
    tree.pack(side='top', fill='both', expand=True)
    search_frame.pack(side='top', fill='x')
    search_label.pack(side='left')
    search_entry.pack(side='left', fill='x', expand=True)
    search_button.pack(side='left')
    bottom_label.pack(side='top', fill='x', pady=10)

    poproot.wait_window()  # Wait for the popup window to be closed

    return selected_filepath  # Return the global variable

def add_to_history(history_file, filepath):
    history = read_history(history_file)
    if [filepath] not in history:
        history.insert(0, [filepath])
        surplus = len(history) - max_nr_files
        if surplus > 0:
            del history[-surplus:]
        with open(history_file, "w", newline="", encoding="utf-8") as csvfile:
            write = csv.writer(csvfile)
            write.writerows(history)

if __name__ == "__main__":
    history_file = '../../Resources/Files/datafile_history.txt'
    folder_iconpath = "../../images/filemap_3b.ico"
    if True:
        filepath = 'C:/Users/mulderg/Downloads/10_October5.csv'
        add_to_history(history_file, filepath)
    if True:
        history = read_history(history_file)
        selected_filepath = select_history_filepath(history)
        print(f"Selected filepath: {selected_filepath}")
