from tkinter import *
import time
class Graphics:
    def __init__(self):
        self.root = Tk()
        self.canva = Canvas(self.root,bg="Black",height=500,width=600)
        self.canva.pack()
        self.acr = self.canva.create_oval(30,100,100,170,fill="red",outline="yellow",width=10)
        self.rec = self.canva.create_rectangle(200,50,31,200,fill="red")
        self.lin = self.canva.create_line(50,300,50,200,fill="red")
        Widget.bind(self.canva,"<B1-Motion>",self.mouseMove)
        Widget.bind(self.canva,"<Button-1>",self.mouseDown)
        self.canva.move(self.acr,100,100)
        self.root.mainloop()
    def mouseDown(self,event):
        # self.canva.move(self.acr,100,100)
        self.lastx=event.x
        self.lasty=event.y
        # print(self.canva.coords(self.lin))

    def mouseMove(self,event):
        self.canva.move(CURRENT,event.x - self.lastx,event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y
graph = Graphics()        