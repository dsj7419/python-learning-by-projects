import tkinter as tk
from tkinter import filedialog

# Create main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create Text Widget
text_widget = tk.Text(root, wrap='word', undo=True)
text_widget.pack(expand='yes', fill='both')

# Create Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Functions for file operations
def new_file():
    root.title("Untitled - Simple Text Editor")
    text_widget.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        root.title(file + " - Simple Text Editor")
        text_widget.delete(1.0, tk.END)
        with open(file, "r") as file_handle:
            text_widget.insert(tk.INSERT, file_handle.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        root.title(file + " - Simple Text Editor")
        with open(file, "w") as file_handle:
            file_handle.write(text_widget.get(1.0, tk.END))

# Add file operations to File Menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Add menu bar to root window
root.config(menu=menu_bar)

# Main Loop
root.mainloop()
