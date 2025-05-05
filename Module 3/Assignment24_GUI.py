# W.A.P to create GUI Frame. 
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Simple GUI")
root.geometry('200x150')
#label = ttk.Label(root, text="This is a simple GUI.")
#label.pack(padx=20, pady=20)

button = ttk.Button(root, text="Click Me")
button.pack(padx=20, pady=20)

root.mainloop()