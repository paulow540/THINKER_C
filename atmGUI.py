from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import *
import mysql.connector
import random
import time

class Atm():
	def __init__(self):
		self.root = Tk()
		# self.root.iconbitmap('icons8_Calculator.ico')
		self.root.title('ATM App')
		self.mainFrame = Frame(self.root)
		self.mainFrame.grid(row=1, column=0)
		self.main()
		self.connection()
		self.root.mainloop()

	def connection(self):
		self.mycon = mysql.connector.connect(host='localhost', passwd='', user='root', database='bank')
		self.mycursor = self.mycon.cursor()

	def main(self):
		self.screen = Text(self.mainFrame, width=53, height=5)
		self.screen.insert(1.0,'Welcome to my bank\n Press the register button to register or Enter your pin to continue transactions')
		self.screen.grid(row=1, column=0, columnspan=5)
		self.pinScreen = Entry(self.mainFrame, width=50, show='*')
		self.pinScreen.grid(row=2, column=0, columnspan=5)
		# self.screen.delete(1.0, 'end')
		# self.screen.insert(1.0, 'Enter your pin to continue transactions')
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=4, column=0)
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=5, column=0)
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=6, column=0)

		Button(self.mainFrame, text=7, width=7, height=3, command=lambda: self.pin('7')).grid(row=4, column=1)
		Button(self.mainFrame, text=8, width=7, height=3, command=lambda: self.pin('8')).grid(row=4, column=2)
		Button(self.mainFrame, text=9, width=7, height=3, command=lambda: self.pin('9')).grid(row=4, column=3)

		Button(self.mainFrame, text=4, width=7, height=3, command=lambda: self.pin('4')).grid(row=5, column=1)
		Button(self.mainFrame, text=5, width=7, height=3, command=lambda: self.pin('5')).grid(row=5, column=2)
		Button(self.mainFrame, text=6, width=7, height=3, command=lambda: self.pin('6')).grid(row=5, column=3)

		Button(self.mainFrame, text=1, width=7, height=3, command=lambda: self.pin('1')).grid(row=6, column=1)
		Button(self.mainFrame, text=2, width=7, height=3, command=lambda: self.pin('2')).grid(row=6, column=2)
		Button(self.mainFrame, text=3, width=7, height=3, command=lambda: self.pin('3')).grid(row=6, column=3)

		Button(self.mainFrame, text='Enter', width=7, height=3, command=self.enter).grid(row=4, column=4)
		Button(self.mainFrame, text='Delete', width=7, height=3, command=self.delete).grid(row=5, column=4)
		Button(self.mainFrame, text='Cancel', width=7, height=3, command=lambda: self.cancel('')).grid(row=6, column=4)

		Button(self.mainFrame, text='Register', font=(20), width=50, height=5, command=self.register).grid(row=7, column=0, columnspan=5)

	def delete(self):
		self.onScreen = self.pinScreen.get()
		self.pinScreen.delete(0, len(self.pinScreen.get()))
		self.pinScreen.insert(0, self.onScreen[:-1])


	def pin(self, var):
			self.onScreen = self.pinScreen.get()
			if self.onScreen != '':
				self.pinScreen.delete(0, len(self.onScreen))
				self.pinScreen.insert(0, self.onScreen + var)
			else:
				self.pinScreen.insert(0, var)

	def enter(self):
		# showinfo('pin', self.pinScreen.get())
		query = 'SELECT * FROM customers WHERE Account_Pin=%s'
		val = (int(self.pinScreen.get()),)
		self.mycursor.execute(query, val)
		myreg = self.mycursor.fetchall()
		if myreg:
			showinfo('Successful', 'Login successful')
			self.changeAll()
		else:
			showinfo('Error', 'Incorrect pin')


	def changeAll(self):
		return

	def register(self):
		self.reg = Toplevel()
		self.reg.title('Register')
		self.reg.geometry('300x300')
		self.newMainFrame = Frame(self.reg)
		self.newMainFrame.pack()
		# self.reg.iconbitmap('icons8_Add_User_Male.ico')
		Label(self.newMainFrame, text='First Name').grid(row=0, column=0)
		self.fName = Entry(self.newMainFrame, width=30)
		self.fName.grid(row=0, column=1)
		Label(self.newMainFrame, text='Last Name').grid(row=1, column=0)
		self.lName = Entry(self.newMainFrame, width=30)
		self.lName.grid(row=1, column=1)
		Label(self.newMainFrame, text='Sex').grid(row=2, column=0)
		self.sex = Entry(self.newMainFrame, width=30)
		self.sex.grid(row=2, column=1)
		Label(self.newMainFrame, text='Phone Number').grid(row=3, column=0)
		self.phone = Entry(self.newMainFrame, width=30)
		self.phone.grid(row=3, column=1)
		Label(self.newMainFrame, text='Address').grid(row=4, column=0)
		self.address = Entry(self.newMainFrame, width=30)
		self.address.grid(row=4, column=1)
		Label(self.newMainFrame, text='pin').grid(row=5, column=0)
		self.pin = Entry(self.newMainFrame, width=30)
		self.pin.grid(row=5, column=1)
		Button(self.newMainFrame, text='Register', command=self.newUser).grid(row=6, column=1)

	def acctNo(self):
		return random.randint(1000000,9999999)

	def newUser(self):
		self.no = '101' + str(self.acctNo())
		self.uPin = self.pin.get()
		self.first_name = self.fName.get()
		self.last_name = self.lName.get()
		self.gender = self.sex.get()
		self.phone_number = self.phone.get()
		self.adres = self.address.get()
		amount = 0
		query = 'INSERT INTO customers(Account_Number, First_Name, Last_Name, Sex, Phone_Number, Address, Account_Pin, Amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
		val = (self.no, self.first_name, self.last_name, self.gender, self.phone_number, self.adres, self.uPin, amount)
		self.mycursor.execute(query, val)
		self.mycon.commit()
		showinfo('Registration successful', 'Registration successful, Your account number is ' + str(self.no))
		time.sleep(5)
		self.reg.destroy()

me = Atm()