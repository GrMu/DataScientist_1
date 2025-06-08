
import tkinter as tk
import tkinter.ttk as ttk

history = [['C:/Users/mulderg/Downloads/10_October5.csv'], ['C:/Users/mulderg/Downloads/10_October4.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/1_January.csv'],
               ['C:/Users/mulderg/Downloads/10_October5.csv'], ['C:/Users/mulderg/Downloads/10_October4.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/1_January.csv'],
               ['C:/Users/mulderg/Downloads/10_October5.csv'], ['C:/Users/mulderg/Downloads/10_October4.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/10_October3.csv'], ['C:/Users/mulderg/Downloads/1_January.csv']]
'''
Sub routines
'''
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
        print(f"Clicked on item: {item}")
        # Extract the index from the item ID
        index = int(item.replace('item', '')) - 1
        # Retrieve the original file path from the history list
        original_filepath = history[index][0]
        print(f"Filepath: {original_filepath}")
        # Update the label with the original file path
        bottom_label.config(text=f"Filepath: {original_filepath}", foreground="Blue", )
        # Close the window after 3 seconds
        root.after(1500, root.destroy)
    else:
        print("Clicked on empty space.")
        bottom_label.config(text="Clicked on empty space.")

def on_enter(event):
    on_doubleclick(event)

def on_resize(event):
    # Get the new width of the Treeview
    new_width = tree.winfo_width()
    # Update the column width dynamically
    tree.column('Name', width=new_width - 40)  # Subtract the width of the first column
    # Re-wrap the text in column 2 based on the new width
    for i, row in enumerate(history):
        for item in row:
            wrapped_item = wrap_text(item, new_width // 8)  # Adjust the width parameter as needed
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
Main routine: show pop-up to select a filepath
'''
root = tk.Tk()
root.title("Select a file from the file history")
root.geometry("500x650")  # Set initial size of the window to make everything visible
root.minsize(200, 100)  # Set minimum size of the window
root.resizable(width=1, height=1)
# Bind the resize event to dynamically adjust column width and re-wrap text
root.bind('<Configure>', on_resize)
# Bind Enter key to select an item after clicking once
root.bind('<Return>', on_enter)

# Create label at top and bottom
top_label = ttk.Label(root, text="Double click on a filepath:")
bottom_label = ttk.Label(root, text="")  # background="lightgrey"

# Create table with wrapped filepaths and a scrollbar
tree_frame = tk.Frame(root)
tree = ttk.Treeview(tree_frame, columns=('Item', 'Name'), show='headings', selectmode="browse")
tree.heading('Item', text='Item')
tree.heading('Name', text='Filepath')
# Set column widths
tree.column('Item', width=40)  # Small width for column 1
tree.column('Name', width=150)  # Set initial width for column 2
style = ttk.Style()
style.configure("Treeview", rowheight=50)  # Row height to contain 3 wrapped lines
# Insert data with wrapped text and adjust row height
for i, row in enumerate(history):
    for item in row:
        wrapped_item = wrap_text(item, 8)  # Adjust the width parameter as needed
        row_height = calculate_row_height(wrapped_item)
        tree.insert('', 'end', iid=f'item{i+1}', values=((i+1), wrapped_item), tags=('normal',))
tree.tag_configure('highlight', background='light yellow')
tree.tag_configure('normal', background='white')
tree.bind('<Double-1>', on_doubleclick)  # Bind left mouse click
scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)

# Add search entry and button
search_frame = tk.Frame(root)
search_label = ttk.Label(search_frame, text="Search:")
search_entry = tk.Entry(search_frame)
search_button = tk.Button(search_frame, text="Search", command=search_and_highlight)

# Position the elements
top_label.pack(side='top', pady=10)
tree_frame.pack(side='top', fill='x')
scroll.pack(side='right', fill='y')  # Pack scrollbar first
tree.pack(side='top', fill='both', expand=True)  # Pack Treeview with expand and fill options
search_frame.pack(side='top', fill='x')
search_label.pack(side='left')
search_entry.pack(side='left', fill='x', expand=True)
search_button.pack(side='left')
bottom_label.pack(side='top', fill='x', pady=10)

root.mainloop()
