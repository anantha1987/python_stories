import tkinter as tk


class Cbuttons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checklist")
        self.CheckVar0 = tk.IntVar()
        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.CheckVar4 = tk.IntVar()
        self.CheckVar5 = tk.IntVar()
        self.CheckVar6 = tk.IntVar()
        self.main()

    def group(self):
        if self.CheckVar0.get():
            print("group slected")
            self.CheckVar1.set(1)
            self.CheckVar4.set(1)
        else:
            self.CheckVar1.set(0)
            self.CheckVar4.set(0)
        if self.CheckVar1.get() and self.CheckVar4.get():
            print('Both boxes checked')
            self.CheckVar0.set(1)
        else:
            self.CheckVar0.set(0)

        if self.CheckVar1.get():
            print("group sleected")
            self.CheckVar2.set(1)
            self.CheckVar3.set(1)
        else:
            self.CheckVar2.set(0)
            self.CheckVar3.set(0)

        if self.CheckVar4.get():
            print("group sleected")
            self.CheckVar5.set(1)
            self.CheckVar6.set(1)
        else:
            self.CheckVar5.set(0)
            self.CheckVar6.set(0)

    def confirm(self):

        if self.CheckVar2.get() and self.CheckVar3.get():
            print('Both boxes checked')
            self.CheckVar1.set(1)
        else:
            self.CheckVar1.set(0)
        if self.CheckVar5.get() and self.CheckVar6.get():
            print('Both boxes checked')
            self.CheckVar4.set(1)
        else:
            self.CheckVar4.set(0)


    def main(self):
        C0 = tk.Checkbutton(self.root, text="Underwear", variable=self.CheckVar1, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.group)
        C0.grid(row=0, column=1)
        C1 = tk.Checkbutton(self.root, text="Underwear", variable=self.CheckVar1, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.group)
        C2 = tk.Checkbutton(self.root, text="T-shirts", variable=self.CheckVar2, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.confirm)
        C1.grid(row=1,column=2)
        C2.grid(row=2,column=3)
        C3 = tk.Checkbutton(self.root, text="T-shirts", variable=self.CheckVar3, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.confirm)
        C3.grid(row=3,column=3)
        C4 = tk.Checkbutton(self.root, text="Underwear", variable=self.CheckVar4, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.group)
        C5= tk.Checkbutton(self.root, text="T-shirts", variable=self.CheckVar5, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10, command=self.confirm)
        C4.grid(row=4, column=2)
        C5.grid(row=5, column=3)
        C6 = tk.Checkbutton(self.root, text="T-shirts", variable=self.CheckVar6, anchor='w', onvalue=1,
                            offvalue=0, height=1, width=10,command=self.confirm)
        C6.grid(row=6, column=3)
        self.root.mainloop()


if __name__ == '__main__':
    Cbuttons()