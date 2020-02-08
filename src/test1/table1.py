from ttkwidgets import CheckboxTreeview
import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()
root.geometry('500x500')
root.title("Checkbox example")

f1=tk.Frame(root,width=490,height=490)
f1.grid()

can=tk.Canvas(f1,width=500)
tree=CheckboxTreeview(can,show='tree')
tree.column('#0',minwidth=350,stretch=True,width=300)
tree.insert("", "end", "1", text="1"+'2')
tree.insert("1", "end", "11", text="11")
tree.insert("1", "end", "12", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
tree.insert("11", "end", "111",text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra' )
tree.insert("", "end", "2", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
tree.grid()

xscrol=ttk.Scrollbar(can,orient=tk.HORIZONTAL,command=tree.xview)
xscrol.grid_anchor(anchor=tk.S)
xscrol.grid( sticky='ew')

tree.config(xscroll=xscrol.set)

can.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)

root.mainloop()