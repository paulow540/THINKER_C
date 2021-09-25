from tkinter import * 
class Hello:
    def __init__(self):
        self.root = Tk()
        self.lb1 = Label(self.root,text="Hello World!")
        # self.lb1.pack()
        self.lb1.grid(row=0,column=0)
        self.lb2 = Label(self.root,text="My name is Osikoya")
        self.lb2.grid(row=1 , column=0)
        Button(self.root,text="Click Me",padx=20,pady=20)#.pack()
        self.btn = Button(self.root,text="Click Me",command=self.myClick)
        self.btn.grid(row=2 , column=0)

        self.ent = Entry(self.root,width=20,bg="blue",fg="white")
        self.ent.grid(row=3 , column=0)

        self.root.mainloop()

    def myClick(self):
        self.btn.config(text="Clicked")
        self.lb1 = Label(self.root,text="Look! i Clicked A button!")
        self.lb1.grid(row=5 , column=0)

hello = Hello()
