from tkinter import *

window = Tk()
window.title("ENABLE REGISTRIES AND MEASURES")
window.geometry('400x400')
mainframe=Frame(window)
mainframe.pack(side=TOP)
frame1=Frame(mainframe)


def clicked():
    #lbl.configure(text="Button was clicked !!")
    txt.insert(10,"Button was clicked !!")



lbl = Label(frame1, text="CLIENT Mnemonic ", relief = RAISED)
lbl.place(x=10,y=20)

txt = Entry(frame1,width=10)
#txt.grid(column=1, row=0)
txt.place(x=10,y=60)
fetch_btn = Button(frame1, text="FETCH", command=clicked)
#fetch_btn.grid(column=2, row=0)
fetch_btn.place(x=10,y=90)
frame1.pack(side=LEFT)
window.mainloop()


rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print (col.get()),
        print()

Button(text='Fetch', command=onPress).grid()