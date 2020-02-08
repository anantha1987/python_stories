import tkinter as tk
from tkinter import ttk


def routine(event):
    if str(notebook.index(notebook.select())) == "0":
        print("focus")
        notebook.tab(1, state="disabled")
        print("Tab1")
        print("focus")
    else:
        print("focus")
        notebook.tab(0, state="disabled")
        print("Tab2")
        print("focus")
    # notebook.tab(0, state="normal")
    # notebook.tab(1, state="normal")

window = tk.Tk()
window.title("tabexample")
window.geometry("500x500")
frame=tk.Frame(window, width=490, height=490, background="yellow", bd=2, relief=tk.SUNKEN)
frame.grid(row=0, column=0)
notebook = ttk.Notebook(window, name="notebook")
notebook.grid(row=0,column=0)

f1=tk.Frame(notebook, width=490, height=490, background="red")
f1.grid(row=0, column=0)
f2=tk.Frame(notebook, background="green", width=490, height=490)
f2.grid(row=0, column=0)

f1_label = tk.Label(f1, text="hello")
f1_label.grid(row=0, column=0)

f2_label = tk.Label(f2, text="anantha")
f2_label.grid(row=0, column=0)



notebook.add(f1, text="First Tab")
notebook.add(f2, text="Second Tab")
notebook.enable_traversal()

notebook.bind("<<NotebookTabChanged>>", routine)


window.mainloop()
