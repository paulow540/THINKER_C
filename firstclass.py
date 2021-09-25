# def newPage(eve="ax"):
#     print(a + b)

# # addition()


# state = True
# def changeText():
#     # global state
#     if state:
#         lb.config(text='First GUI class')
#         state = False
#     else:
#         lb.config(text='Hello Wolrd')  
#         state= True
from tkinter import Tk, Label, Button
container = Tk()
container.geometry('800x400')
container.title('First Gui')
container.iconbitmap('icons8_Ok.ico')
lb = Label(container,text="Hello World")
lb.pack(side="left")
Button(container,text="Click Me", command=changeText).pack(side="left")

container.mainloop()

def calc(operator):
    val1 = txt1.get()
    val2= txt2.get()
    lb.config(text=operator)
    if val1 !="" and val2 != "":
        val1 = float(val1)
        val2 = float(val2)
        if operator == '+':
            result = val1 + val2
        elif operator == '-':
            result = val1 - val2
        elif operator == '/':
            result = val1 - val2
        elif operator == '*':
            result = val1 * val2
        res.config(text=result)    
    else:
        showinfo('Error Information',  "Both textbox cannot be empty")           

from tkinter import *
from tkinter.messagebox import *
con = Tk()
# con.geometry('800x400')
con.title('Simple Calculator')
con.iconbitmap('icons8_Ok.ico')
fm1 = Frame(con)
fm1.pack()
txt1 = Entry(fm1)
txt1.pack(side="left")
lb = Label(fm1,text="")
lb.pack(side="left",padx=5)
txt2 = Entry(fm1)
txt2.pack(side="left",padx=5)
Label(fm1,text='=')
res = Label(fm1,text='')
res.pack(side="left",padx=5)
bmf=Frame(con)
bmf.pack(pady=5)
Button(bmf,text="+",width=7,command=lambda: calc('+')).pack(side="left",padx=5)
Button(bmf,text="-",width=7,command=lambda: calc('-')).pack(side="left",padx=5)
Button(bmf,text="/",width=7,command=lambda: calc('/')).pack(side="left",padx=5)
Button(bmf,text="*",width=7,command=lambda: calc('*')).pack(side="left",padx=5)

con.mainloop()