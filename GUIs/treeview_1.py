import tkinter as tk
import tkinter.ttk as ttk

def on_click(event):
    item = tree.identify_row(event.y)
    if item:  # Check if a row was identified
        print(f"Clicked on item: {item}")
        # Now you can do something with the item ID
        # For example, get its values:
        values = tree.item(item, 'values')
        print(f"Values: {values}")
    else:
        print("Clicked on empty space.")

root = tk.Tk()
tree = ttk.Treeview(root, columns=('Name', 'Age'))
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# Insert some sample data
tree.insert('', 'end', iid='item1', values=('Alice', 25))
tree.insert('', 'end', iid='item2', values=('Bob', 30))
tree.insert('', 'end', iid='item3', values=('Charlie', 22))

tree.bind('<Button-1>', on_click)  # Bind left mouse click

tree.pack()
root.mainloop()