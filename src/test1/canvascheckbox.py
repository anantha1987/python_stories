from ttkwidgets import CheckboxTreeview
import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()
root.geometry('600x600')
root.title("Checkbox example")

f1=tk.Frame(root,width=595,height=595,background='blue',bd=1)
f1.grid(row=0,column=0)
checkingFrame=tk.Frame(f1,width=590,height=590,background='yellow',bd=1)
checkingFrame.grid(row=0,column=0,padx=5,pady=5)
canvas_tree=tk.Canvas(checkingFrame,bg='white')
canvas_tree.grid(row=0,column=0)

main_tree=CheckboxTreeview(canvas_tree,show='tree')
main_tree.column("#0",width=500,minwidth=600,stretch=True)
main_tree.configure(height=10)


main_tree.insert("", "end", "1", text="1"+'2')
main_tree.insert("1", "end", "11", text="11")
main_tree.insert("1", "end", "12", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("11", "end", "111",text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra' )
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')

main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')

main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')

main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra'+"Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra'+"Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')

main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
main_tree.insert("", "end",  text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')



vsbar=tk.Scrollbar(checkingFrame,orient=tk.VERTICAL,command=main_tree.yview)
vsbar.grid(row=0,column=1,sticky=tk.NS)

hsbar=tk.Scrollbar(checkingFrame,orient=tk.HORIZONTAL,command=main_tree.xview)
hsbar.grid(row=1,column=0,sticky=tk.EW)

main_tree.config(xscroll=hsbar.set,yscroll=vsbar.set)
main_tree.grid(row=0,column=0)
canvas_tree.create_window((0,0),window=main_tree,anchor=tk.NW)
canvas_tree.configure(yscrollcommand=vsbar.set,xscrollcommand=hsbar.set)

main_tree.update_idletasks()
bbox=canvas_tree.bbox(tk.ALL)
canvas_tree.configure(scrollregion=bbox,width=400,height=400)

# can=tk.Canvas(f1,width=500)
# tree=CheckboxTreeview(can,show='tree')
# tree.column('#0',minwidth=350,stretch=True,width=300)
# tree.insert("", "end", "1", text="1"+'2')
# tree.insert("1", "end", "11", text="11")
# tree.insert("1", "end", "12", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
# tree.insert("11", "end", "111",text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra' )
# tree.insert("", "end", "2", text="Anantha"+"kumar"+'Kondra'+'Anantha Kumar Kondra')
# tree.grid()
#
# xscrol=ttk.Scrollbar(can,orient=tk.HORIZONTAL,command=tree.xview)
# xscrol.grid_anchor(anchor=tk.S)
#
# xscrol.grid( sticky='ew')
# tree.config(xscroll=xscrol.set)
#
# can.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)

root.mainloop()