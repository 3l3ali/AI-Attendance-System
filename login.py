from tkinter import *
import tkinter.messagebox

class LoginFrame(Frame):
	def __init__(self,master):
		super().__init__(master)

		self.label_username = Label(self, text="Username")
		self.label_password = Label(self, text="Password")


		self.entry_username = Entry(self)
		self.entry_password = Entry(self, show="*")


		self.label_username.grid(row=0, sticky=E)
		self.label_password.grid(row=1, sticky=E)
		self.entry_username.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)


		self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
		self.logbtn.grid(columnspan = 2)

		self.pack()


	def _login_btn_clicked(self):
		username = self.entry_username.get()
		password = self.entry_password.get()


		if username == "admin" and password == "admin":
			tkinter.messagebox.showinfo("login info", "welcome admin")
		else:
			tkinter.messagebox.showerror("login error", "incorrect username")




