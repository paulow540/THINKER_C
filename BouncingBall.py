from tkinter import *
import time
class Bounce:
    def __init__(self):
        self.root =Tk()
        self.root.title("Bouncing Ball")
        self.canv = Canvas(self.root,bg="#123455",height=500,width=700)
        self.canv.pack()
        self.dim = 5,5,60,60
        self.ova = self.canv.create_oval(self.dim,fill="#999999")
        self.xa = 3
        self.ya = 5
        # self.canv.move(self.ova,self.xa,self.ya)
        while True:
            self.canv.move(self.ova,self.xa,self.ya)
            self.p = self.canv.coords(self.ova)
            print(self.p)
            if self.p[3] >= 500 or self.p[1] <= 0:
                self.ya = -self.ya 
            if self.p[2] >= 700 or self.p[0] <= 0:
                self.xa = -self.xa
            self.root.update()
            time.sleep(0.035)  

        self.root.mainloop()

bon=Bounce()        