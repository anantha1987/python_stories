import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.geometry("1500x800")
        self.configure(background="#303030")


class Table(tk.Frame):

    def __init__(self, master, rows=2, columns=2):

        tk.Frame.__init__(self, master, background="#36363d")

        # Set table as list of rows
        self.table = []
        for row in range(rows):

            # Create list to store cell info in a rows
            current_row = []
            for column in range(columns):

                label = tk.Label(self, text="", borderwidth=0, width=columns, bg="#474756", )
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1, )

                # Append cell (column) into rows
                current_row.append(label)

            # Append rows into whole table
            self.table.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


class ScrollablePage(tk.Frame):

    def __init__(self, master, *args, **kw):
        super().__init__(master)

        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="red")    # THIS TO EMPHASIZE THE CANVAS,

        self.frame = tk.Frame(self.canvas, *args, **kw)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.frame, anchor="nw", tags="self.frame")

        # Dynamic frame setup
        self.frame.bind("<Configure>", self.frame_conf)
        self.canvas.bind("<Configure>", self.frame_width)

        # Bind canvas to mousewheel
        self.canvas.bind("<Enter>", self.bound_to_mousewheel)
        self.canvas.bind("<Leave>", self.unbound_to_mousewheel)

    def frame_conf(self, event):
        """
        Reset the scroll region to encompass the inner frame
        """

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def frame_width(self, event):
        """
        Function to adjust canvas's frame upon expand (can't use pack)
        """

        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def mouse_wheel(self, event):
        """
        Capture mouse wheel changes to scroll page
        """
        if self.vsb.get() != (0.0, 1.0):
            self.canvas.yview_scroll(-1 * int(event.delta / 60), "units")

    def bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.mouse_wheel)

    def unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")


class PageTwo(ScrollablePage):

    def __init__(self, master):

        # Create page
        super().__init__(master, bg="#36363d")

        # EXAMPLE CONTENT
        controller = tk.Frame(self.frame, bg="#474756", width=0.9 * 1500, height=200, bd=0,)
        controller.pack(side="top", fill="x", padx=20, pady=10)

        self.table = Table(self.frame, rows=20, columns=10)
        self.table.pack(side="top", fill="both", padx=20, expand=1)


class MainContent(tk.Frame):

    # Setup main content's stacked-frame
    frames = {}

    # main_content_classes = [PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageDefault]  # << ORIGINAL ONE
    main_content_classes = [PageTwo]

    def __init__(self, master):

        # Create main content's frame
        super().__init__(master)

        # Place main content's frame in main window
        self.place(x=150, y=130, relwidth=0.9, relheight=0.83)

        # Create grid inside main content frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Stacking pages in main content
        for FrameClass in MainContent.main_content_classes:
            page_name = FrameClass.__name__
            frame = FrameClass(self)
            frame.grid(row=0, column=0, sticky="nsew")
            MainContent.frames[page_name] = frame


class Datalab:

    def __init__(self, *args, **kwargs):

        main_window = MainWindow()
        MainContent(main_window)
        main_window.mainloop()

if __name__ == "__main__":
    app = Datalab()