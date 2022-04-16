from tkinter import *
# import tkinter.ttk as ttk
from tkinter.messagebox import *
import mysql.connector
import random
import time

class Schoolportal:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x300')
        self.root.title("SCHOOLPORTAL")        
        self.welcome()
        self.myconnection()        
        self.root.mainloop()


    def myconnection(self):
        self.mycon = mysql.connector.connect(host='localhost', passwd='', user='root', database='Schoolportal')
        self.mycursor = self.mycon.cursor()
    
    def welcome(self):
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
        self.mywelcome =Label(self.mainFrame, text="WELCOME TO PAUL SCHOOL PORTAL")
        self.mywelcome.pack(side="top",padx =20,pady=10)
        self.student =Label(self.mainFrame, text="Student:")
        self.student.pack(side="left",padx =2,pady=1)
        Button(self.mainFrame,text="Student",width=10,state="normal",command=lambda: self.studenting()).pack(side="left",padx =2,pady=1)     
        self.staff =Label(self.mainFrame, text="Staff:")
        self.staff.pack(side="left",padx =2,pady=1)
        Button(self.mainFrame,text="Staff",width=10,state="normal",command=lambda: self.staffing()).pack(side="left",padx =2,pady=1)     




    def studenting(self):
        self.studen = Toplevel()
        self.studen.title('Register')
        self.studen.geometry('600x300')
        self.secondmainFrame = Frame(self.studen)
        self.secondmainFrame .pack(side="top",padx =2,pady=1)
        Label(self.secondmainFrame , text=" Login  ").pack(side="left",padx =2,pady=1)
        Button(self.secondmainFrame ,text="Login",width=10,state="normal",command=lambda: self.login()).pack(side="left",padx =2,pady=1)    
        Label(self.secondmainFrame , text="Sign Up").pack(side="left",padx =2,pady=1)
        Button(self.secondmainFrame ,text="Sign Up",width=10,state="normal",command=lambda: self.signup()).pack(side="left",padx =2,pady=1)        
        Label(self.secondmainFrame , text="Go back to Menu").pack(side="left",padx =2,pady=1)
        Button(self.secondmainFrame ,text="Back to Menu",width=10,state="normal",command=lambda: self.backtomenu()).pack(side="left",padx =2,pady=1)    

    def backtomenu(self):
        self.welcome()   
  
    def signup(self):
        self.signup = Toplevel()
        self.signup.title('Sign up')
        self.signup.geometry('300x300')
        self.signupmainFrame = Frame(self.signup)
        self.signupmainFrame.pack()  
        Label(self.signupmainFrame , text="First Name  ").grid(row=1, column=0)
        self.firstname=Entry(self.signupmainFrame, width=30)
        self.firstname.grid(row=1, column=1)    
        Label(self.signupmainFrame , text="Last Name  ").grid(row=2, column=0)
        self.lastname =Entry(self.signupmainFrame, width=30)
        self.lastname.grid(row=2, column=1)    
        Label(self.signupmainFrame , text="Email  ").grid(row=3, column=0)
        self.email=Entry(self.signupmainFrame, width=30)
        self.email.grid(row=3, column=1)
        Label(self.signupmainFrame , text="Gender  ").grid(row=4, column=0)
        self.gender =Entry(self.signupmainFrame, width=30)
        self.gender.grid(row=4, column=1)    
        Label(self.signupmainFrame , text="Password  ").grid(row=5, column=0)
        self.password =Entry(self.signupmainFrame, width=30)
        self.password.grid(row=5, column=1)
        Button(self.signupmainFrame,text="Register",width=10,state="normal",command=lambda: self.studentregister()).grid(row=6, column=1) 
        # self.welcome.destroy()
    def studentregister(self):
        self.first_name = self.firstname.get()
        self.last_name = self.lastname.get()
        self.myemail = self.email.get()
        self.mygender =self.gender.get()
        self.mypassword =self.password.get()
        query = 'INSERT INTO student(First_Name, Last_Name, Email, Gender, Password) VALUES(%s, %s, %s, %s,%s)'
        val = (self.first_name,self.last_name,self.myemail,self.mygender,self.mypassword)
        self.mycursor.execute(query, val)
        if (self.first_name !="" and self.last_name !="") and (self.mypassword !="" and self.mygender != ""):
            self.mycon.commit()
            showinfo('Registration successful', "Registration successful")
            time.sleep(5)
            self.login.destroy()
        else:
            print("you have to fill the forms")
            showinfo('fill form', "fill the form")

    
    def login(self):
        self.login = Toplevel()
        self.login.title('Login')
        self.login.geometry('300x300')
        self.loginmainFrame = Frame(self.login)
        self.loginmainFrame.pack() 
        Label(self.loginmainFrame , text="Email  ").grid(row=1, column=0)
        self.email=Entry(self.loginmainFrame, width=30)
        self.email.grid(row=1, column=1)
        Label(self.loginmainFrame , text="Password  ").grid(row=2, column=0)
        self.password =Entry(self.loginmainFrame, width=30)
        self.password.grid(row=2, column=1)
        Button(self.loginmainFrame,text="Login",width=10,state="normal",command=lambda: self.studentlogin()).grid(row=3, column=1) 

    def studentlogin(self):
        self.myemail = self.email.get()       
        self.mypassword =self.password.get()
        query = "SELECT Email, Password FROM student WHERE Email=%s AND Password=%s"
        val = (self.myemail, self.mypassword)
        self.mycursor.execute(query, val)
        myreg = self.mycursor.fetchone()
        print(myreg)
        if myreg ==None:            
            if self.mypassword !="" and self.myemail != "":            
                print(self.mycursor.rowcount, 'selected successfuly')
                self.login.destroy()
                self.signup()
            else:
                print("fill the form")
                showinfo('fill form', "fill the form")
            
        else:
            if self.mypassword !="" and self.myemail != "":            
                print(self.mycursor.rowcount, 'selected successfuly')
                showinfo('Login successful', "Login successful")
            else:
                print("fill the form")
                showinfo('fill form', "fill the form")   
            
        

    def staffing(self):
        pass



school =Schoolportal()