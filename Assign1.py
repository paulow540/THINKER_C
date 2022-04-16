from tkinter import *
from tkinter.messagebox import *
class Speed:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x300')
        self.root.title('Speed Calculator')
        # self.root.iconbitmap('icons8_Airport.ico')
        # self.Newfm = Frame(self.root)
        # self.Newfm.pack()
        self.fm1 = Frame(self.root)
        self.fm1.pack()
        self.answ = StringVar()
        self.text1=Entry(self.fm1,textvariable=self.answ,state="disable",disabledbackground="White")
        self.text1.pack(side="left",pady=5)
        self.lb1 = Label(self.fm1,text='km/hrs=')
        self.lb1.pack(side="left")
        # self.lb2 = Label(self.fm1,text='=')
        # self.lb2.pack(side="left",padx=10)
        self.answ1=IntVar()
        self.text2=Entry(self.fm1,textvariable=self.answ1,border=3,state="disable")
        self.text2.pack(side="left",padx=4,pady=5)
        self.lb3 = Label(self.fm1,text="miles/hrs")
        self.lb3.pack(pady=5)
        # self.fm0 =Frame(self.root)
        # self.fm0.pack()
        Button(self.root,text="CE",width=10,command=lambda: self.clear()).pack()
        self.fm2 = Frame(self.root)
        self.fm2.pack()
        Button(self.fm2,text="7",width=10,command=lambda: self.number('7')).grid(row=0,column=0,padx=5,pady=5)
        Button(self.fm2,text="8",width=10,command=lambda: self.number('8')).grid(row=0,column=1,padx=5,pady=5)
        Button(self.fm2,text="9",width=10,command=lambda: self.number('9')).grid(row=0,column=2,padx=5,pady=5)
        Button(self.fm2,text="4",width=10,command=lambda: self.number('4')).grid(row=1,column=0,padx=5,pady=5)
        Button(self.fm2,text="5",width=10,command=lambda: self.number('5')).grid(row=1,column=1,padx=5,pady=5)
        Button(self.fm2,text="6",width=10,command=lambda: self.number('6')).grid(row=1,column=2,padx=5,pady=5)
        Button(self.fm2,text="1",width=10,command=lambda: self.number('1')).grid(row=2,column=0,padx=5,pady=5)
        Button(self.fm2,text="2",width=10,command=lambda: self.number('2')).grid(row=2,column=1,padx=5,pady=5)
        Button(self.fm2,text="3",width=10,command=lambda: self.number('3')).grid(row=2,column=2,padx=5,pady=5)
        Button(self.fm2,text=".",width=10,command=lambda: self.number('.')).grid(row=3,column=0,padx=5,pady=5)
        Button(self.fm2,text="0",width=10,command=lambda: self.number('0')).grid(row=3,column=1,padx=5,pady=5)

        self.menubar()

        self.root.mainloop()

    def number(self,num):
        self.res=(float(self.text1.get()+num)*0.621)
        self.answ.set(self.text1.get()+num)
        self.answ1.set(self.res)
    
    def clear(self):
        self.answ.set(" ")
        self.answ1.set(0)


    def menubar(self):
        self.menu = Menu(self.root,tearoff=0)
        self.show= Menu(self.menu,tearoff=0)

        # self.show.add_command(label="Standard",command=self.standard)
        # self.show.add_separator()
        # self.show.add_command(label="Scientific",command=self.standard)
        # self.show.add_separator()
        # self.show.add_command(label="Speed",command=self.standard)
        # self.show.add_separator()
        # self.show.add_command(label="Area",command=self.standard)
        # self.show.add_separator()
        # self.show.add_command(label="Volume",command=self.standard)


        # self.menu.add_cascade(label="More...",menu=self.show,underline=1)
        # self.root.config(menu=self.menu)
    

    
        
spe = Speed()        
