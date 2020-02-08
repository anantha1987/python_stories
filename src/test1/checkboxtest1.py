from ttkwidgets import ItemsCanvas,frames,AutoHideScrollbar
from ttkwidgets.frames import ScrolledFrame
from ttkwidgets import CheckboxTreeview
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import ttkwidgets as twk


root=tk.Tk()
root.geometry('500x500')
root.title("Checkbox example")

f1=tk.Frame(root,width=490,height=490)
f1.pack()

can=tk.Canvas(f1)

tree=CheckboxTreeview(can)
tree.column('#0',minwidth=350,stretch=True)
tree.insert("", "end", "1", text="1"+'2')

tree.insert("1", "end", "11", text="11")
tree.insert("1", "end", "12", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
tree.insert("11", "end", "111",text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra' )

tree.insert("", "end", "2", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
tree.pack(expand=True,fill=tk.BOTH)
xscrol=ttk.Scrollbar(can,orient=tk.HORIZONTAL,command=tree.xview)
xscrol.pack(anchor=tk.S,fill=tk.X,side=tk.BOTTOM)
tree.configure(xscroll=xscrol.set)
can.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)

root.mainloop()
