import tkinter as tk

LABEL_BG = "#ccc"  # Light gray.
ROWS, COLS = 10, 3  # Size of grid.
ROWS_DISP = 5  # Number of rows to display.
COLS_DISP = 3  # Number of columns to display.

class MyApp(tk.Tk):
    def trace_func_result(self):
        print(self.x)

    def trace_func(self, *args):
        #self.radioVar.trace("w", self.tracer)
        self.x= self.int_var.get()

    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(title)
        self.geometry('400x400')
        self.configure(background="Gray")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        master_frame = tk.Frame(self, bg="Light Blue", bd=3, relief=tk.RIDGE)
        master_frame.grid(sticky=tk.NSEW)
        master_frame.columnconfigure(0, weight=1)

        label1 = tk.Label(master_frame, text="Frame1 Contents", bg=LABEL_BG)
        label1.grid(row=0, column=0, pady=5, sticky=tk.NW)

        frame1 = tk.Frame(master_frame, bg="Green", bd=2, relief=tk.GROOVE)
        frame1.grid(row=1, column=0, sticky=tk.NW)

        cb_var1 = tk.IntVar()
        checkbutton1 = tk.Checkbutton(frame1, text="StartCheckBox", variable=cb_var1)
        checkbutton1.grid(row=0, column=0, padx=2)

        label2 = tk.Label(master_frame, text="Frame2 Contents", bg=LABEL_BG)
        label2.grid(row=2, column=0, pady=5, sticky=tk.NW)

        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(master_frame)
        frame2.grid(row=3, column=0, sticky=tk.NW)

        # Add a canvas in that frame.
        canvas = tk.Canvas(frame2, bg="Yellow")
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="white", bd=2)

        # Add the buttons to the frame.
        self.int_var = int_var = tk.IntVar()
        int_var.trace("w", self.trace_func)
        int_var.set(1)

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                if(j == COLS):
                    self.rbutton = tk.Radiobutton(buttons_frame,value=i,variable=self.int_var, padx=7, pady=7, relief=tk.RIDGE)
                    self.rbutton.grid(row=i, column=j, sticky='news')
                else:
                    button = tk.Label(buttons_frame, padx=7, pady=7, relief=tk.RIDGE,
                                   #text="[%d, %d]" % (i, j))
                                      text="Anantha                 Kumar                                Kondra")
                    button.grid(row=i, column=j, sticky='news')

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        #print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width='375', height=dh)

        label3 = tk.Label(master_frame, text="Frame3 Contents", bg=LABEL_BG)
        label3.grid(row=4, column=0, pady=5, sticky=tk.NW)

        frame3 = tk.Frame(master_frame, bg="Blue", bd=2, relief=tk.GROOVE)
        frame3.grid(row=5, column=0, sticky=tk.NW)

        cb_var2 = tk.IntVar()
        checkbutton2 = tk.Checkbutton(frame3, text="EndCheckBox", variable=cb_var2)
        checkbutton2.grid(row=0, column=0, padx=2)
        bt1=tk.Button(frame3,text='get',command=self.trace_func_result)
        bt1.grid(row=1,column=2)

if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()