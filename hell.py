import tkinter
from tkinter.constants import *
import os
import vlc
import time
tk = tkinter.Tk()
tk.geometry('800x400')
tk.title('First Gui')
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()




state = True
def location():
    mp3 =[] 
    mp4 =[]
    global state
    mik = os.path.dirname("C:\\Users\\D\\Documents\\")
    for root, dirs, files in os.walk(mik):    
        for file in files:
            if file.endswith(".mp3"):
                mp3.append(file)
            elif file.endswith(".mp4"):
                mp4.append(file) 
    # print(mp3) 
    if state:      
      for i in mp3:
        #   print(i)
          label.config(text=i)
    else:
       label.config(text='Hello Wolrd')  
       state= True

mp3 =tkinter.Frame(tk)
mp3.pack(fill=BOTH,expand=1)
label = tkinter.Label(mp3, text=" ")
label.pack(fill=X, expand=1)
tkinter.Button(mp3,text="click me",command=lambda: location()).pack(side="bottom")
tk.mainloop()






