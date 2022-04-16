from tkinter import *
from tkinter.messagebox import *
from pytube import YouTube
import os

class Youtubedownloader:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('400x300')
        self.root.title('YOUTUBE DOWNLOADER')
        self.youtube=Frame(self.root)
        self.youtube.pack()
        self.myinfotube =Label(self.youtube,text="Just copy any youtube link to the Entry below")
        self.myinfotube.pack()
        self.linkinput =Entry(self.youtube,width=50,state="disabled",disabledbackground="red")
        self.linkinput.pack(side="bottom",padx =10,pady=20)
        Button(self.youtube,text="download",width=10,state="normal",command=lambda: self.mydownloading()).pack(side="bottom",padx =10,pady=20)      

        self.root.mainloop()
    
    def mydownloading(self):
        self.collectlink =self.linkinput.get()
        print(self.collectlink)
        self.thisutube = YouTube(self.collectlink)
        self.stream = self.thisutube.streams.get_highest_resolution()
        self.downloadplace()
        print("Download completed!!")
        showinfo('Error Information',  "Both textbox cannot be empty")   

    def downloadplace(self):
        self.mypathdownload = os.path.dirname(f"C:\\Users\\D\\Downloads\\{self.stream.download()}")


mytube =Youtubedownloader()