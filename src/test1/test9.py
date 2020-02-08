from tkinter import *
def get():
    print(mylist.curselection())
root = Tk()
root.geometry('400x200')
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
#scrollbar.pack( side = BOTTOM, fill = X )
#mylist = Listbox(root, scrollcommand = scrollbar.set , width='30')
mylist = Listbox(root, yscrollcommand = scrollbar.set ,width='50',relief=RIDGE)
#rows = []
for i in range(100):
    mylist.insert(END, "hello"+str(i))
    #col=[]
    #for j in range(2):
        #mylist.grid(row=i, column=j, sticky=NSEW)
        #mylist.insert(END, '%d.%d' % (i, j))
        #col.append()
    #rows.append()
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
bt1=Button(root,text='get',command=get)
bt1.pack(side='right')
scrollbar.config( command = mylist.xview )
mainloop()