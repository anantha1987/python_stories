import tkinter as tk



class MyApp(tk.Tk):

    def getvalues(self):
        checks= self.cb_var1.get()
        print(checks)
        if(checks == 1):
            print('selected')
            self.frame2.destroy()
            # Create a frame for the canvas and scrollbar(s).
            LABEL_BG = "#ccc"  # Light gray.
            ROWS, COLS = 1000, 3  # Size of grid.
            ROWS_DISP = 5  # Number of rows to display.
            COLS_DISP = 3  # Number of columns to display.
            self.frame2 = tk.Frame(self.master_frame)
            self.frame2.grid(row=3, column=0, sticky=tk.NSEW)

            # Add a canvas in that frame.
            self.canvas = tk.Canvas(self.frame2, bg="white")
            self.canvas.grid(row=0, column=0)

            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.canvas.yview)
            vsbar.grid(row=0, column=1, sticky=tk.NS)
            self.canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL, command=self.canvas.xview)
            hsbar.grid(row=1, column=0, sticky=tk.EW)
            self.canvas.configure(xscrollcommand=hsbar.set)

            # Create a frame on the canvas to contain the buttons.
            buttons_frame = tk.Frame(self.canvas, bg="white", bd=2)

            # Add the buttons to the frame.
            self.int_var = int_var = tk.IntVar()
            int_var.trace("w", self.trace_func)
            int_var.set(1)

            for i in range(1, ROWS + 1):
                for j in range(1, COLS + 1):
                    if (j == COLS):
                        self.rbutton = tk.Radiobutton(buttons_frame, value=i, variable=self.int_var, padx=7, pady=7,
                                                      relief=tk.RIDGE)
                        self.rbutton.grid(row=i, column=j, sticky='news')
                    else:
                        button = tk.Label(buttons_frame, padx=7, pady=7, relief=tk.RIDGE,
                                          # text="[%d, %d]" % (i, j))
                                          text="Anantha                 Kumar                                Kondra "+str(i))
                        button.grid(row=i, column=j, sticky='news')

            # Create canvas window to hold the buttons_frame.
            self.canvas.create_window((0, 0), window=buttons_frame)

            buttons_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = self.canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            #w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
            #dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
            self.canvas.configure(scrollregion=(-332, -18502, 1000, 25000), width='675', height=520)

        else:
            print(' not selected')
            # Create a frame for the canvas and scrollbar(s).
            self.frame2.destroy()
            LABEL_BG = "#ccc"  # Light gray.
            ROWS, COLS = 10, 3  # Size of grid.
            ROWS_DISP = 5  # Number of rows to display.
            COLS_DISP = 3  # Number of columns to display.
            self.frame2 = tk.Frame(self.master_frame)
            self.frame2.grid(row=3, column=0, sticky=tk.NW)

            # Add a canvas in that frame.
            self.canvas = tk.Canvas(self.frame2, bg="white")
            self.canvas.grid(row=0, column=0)

            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.canvas.yview)
            vsbar.grid(row=0, column=1, sticky=tk.NS)
            self.canvas.configure(yscrollcommand=vsbar.set)

            # Create a horizontal scrollbar linked to the canvas.
            hsbar = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL, command=self.canvas.xview)
            hsbar.grid(row=1, column=0, sticky=tk.EW)
            self.canvas.configure(xscrollcommand=hsbar.set)

            # Create a frame on the canvas to contain the buttons.
            buttons_frame = tk.Frame(self.canvas, bg="white", bd=2)


            # Create canvas window to hold the buttons_frame.
            self.canvas.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

            buttons_frame.update_idletasks()  # Needed to make bbox info available.
            bbox = self.canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            # print('canvas.bbox(tk.ALL): {}'.format(bbox))

            # Define the scrollable region as entire canvas with only the desired
            # number of rows and columns displayed.
            #w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
            #dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
            self.canvas.configure(scrollregion=bbox, width='675', height=520)



    def trace_func_result(self):
        print(self.x)

    def trace_func(self, *args):
        #self.radioVar.trace("w", self.tracer)
        self.x= self.int_var.get()

    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        LABEL_BG = "#ccc"  # Light gray.
        ROWS, COLS = 10, 3  # Size of grid.
        ROWS_DISP = 5  # Number of rows to display.
        COLS_DISP = 3  # Number of columns to display.
        self.title(title)
        self.geometry('800x800')
        self.configure(background="Gray")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.master_frame = tk.Frame(self, bg="Light Blue", bd=3, relief=tk.RIDGE)
        self.master_frame.grid(sticky=tk.NSEW)
        self.master_frame.columnconfigure(0, weight=1)

        label1 = tk.Label(self.master_frame, text="Frame1 Contents", bg=LABEL_BG)
        label1.grid(row=0, column=0, pady=5, sticky=tk.NW)

        frame1 = tk.Frame(self.master_frame, bg="Green", bd=2, relief=tk.GROOVE)
        frame1.grid(row=1, column=0, sticky=tk.NW)

        self.cb_var1 = tk.IntVar()
        checkbutton1 = tk.Checkbutton(frame1, text="StartCheckBox", variable=self.cb_var1,anchor='w', onvalue=1,offvalue=0)
        checkbutton1.grid(row=0, column=0, padx=2)

        label2 = tk.Label(self.master_frame, text="Frame2 Contents", bg=LABEL_BG)
        label2.grid(row=2, column=0, pady=5, sticky=tk.NW)

        self.frame2 = tk.Frame(self.master_frame)
        self.frame2.grid(row=3, column=0, sticky=tk.NW)

        # Add a canvas in that frame.
        self.canvas = tk.Canvas(self.frame2, bg="white")
        self.canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        self.canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL, command=self.canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        self.canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(self.canvas, bg="white", bd=2)

        # Create canvas window to hold the buttons_frame.
        self.canvas.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = self.canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        # print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
        dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
        self.canvas.configure(scrollregion=bbox, width='675', height=520)

        frame3 = tk.Frame(self.master_frame,bg="Light Blue", bd=0, relief=tk.RIDGE)
        #frame3.grid(row=6, column=0, sticky=tk.NW)
        frame3.grid(row=4,column=0,sticky=tk.NW)
        cb_var2 = tk.IntVar()
        checkbutton2 = tk.Checkbutton(frame3, text="EndCheckBox", variable=cb_var2)
        checkbutton2.grid(row=2,column=0,padx=2,pady=10)
        bt1 = tk.Button(frame3, text='get', command=self.getvalues)
        bt1.grid(row=2, column=1,padx=2,pady=10)

if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()