import tkinter
def setup():
    root = tkinter.Tk()

    root.geometry('400x400')
    canvas = tkinter.Canvas(root, bg='white')
    frame_left = tkinter.Frame(canvas, bg='white')


    vertscroll = tkinter.Scrollbar(canvas, orient='vertical', command=canvas.yview)
    horscroll = tkinter.Scrollbar(canvas, orient='horizontal', command=canvas.xview)
    canvas.configure(yscrollcommand=vertscroll.set)
    canvas.configure(xscrollcommand=horscroll.set)
    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    canvas_frame = canvas.create_window((0, 0), window=frame_left, anchor="nw")
    vertscroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    horscroll.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    lable=tkinter.Label(text='Ananth')
    lable.place(x='600',y='200')
    #frame1 = tkinter.Frame(canvas_frame,width=500,height=30,background='red')
   # frame1.pack()




    return root


if __name__ == '__main__':
    root = setup()

    root.mainloop()