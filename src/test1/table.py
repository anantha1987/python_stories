from tkinter import *
import tkinter as tk
window = Tk()
window.title("ENABLE REGISTRIES AND MEASURES")
window.geometry('400x400')
window.resizable(False,False)
mainframe=Frame(window)
taskcanvas=tk.Canvas()
frame1=Frame(taskcanvas)
scrollbar = tk.Scrollbar(taskcanvas, orient="vertical", command=taskcanvas.yview)
scrollbar1 = tk.Scrollbar(taskcanvas, orient="horizontal", command=taskcanvas.xview)
taskcanvas.configure(yscrollcommand=scrollbar.set)
taskcanvas.configure(xscrollcommand=scrollbar1.set)
frame1.pack()

window.mainloop()