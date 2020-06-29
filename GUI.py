from project import *
import sys
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

window=tkinter.Tk()
window.title('Attendance')
window.geometry("1280x720")
window.resizable(0,0) #restricting size change
window.configure(background='white')

class LoginFrame(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.label_username = Label(self, text="Username ",font=("Ubuntu", 20),fg="#005fae", bg="white")
		self.label_password = Label(self, text="Password ",font=("Ubuntu", 20),fg="#005fae", bg="white")


		self.entry_username = Entry(self, bg="white")
		self.entry_password = Entry(self, show="*", bg="white")


		self.label_username.grid(row=0, sticky=E)
		self.label_password.grid(row=1, sticky=E)
		self.entry_username.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)

		self.loginBtn = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/loginBtn.gif")
		self.logbtn = Button(self, text="Login", command=self._login_btn_clicked,image= self.loginBtn,activebackground = "white", border="0", bg="white",highlightbackground="white")
		self.logbtn.grid(rowspan=5,columnspan = 2)
		
		self.configure(background="white")
		self.pack()

		#JUST logo
		self.justLogo = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/justLogo.gif")
		self.just=tkinter.Button(window,image= self.justLogo, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.1,rely=0.1,anchor= CENTER)
		#JUST text
		self.justText = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/justText.gif")
		self.just2=tkinter.Button(window,image= self.justText, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.22,rely=0.1,anchor= CENTER)

	def _login_btn_clicked(self):
		username = self.entry_username.get()
		password = self.entry_password.get()


		if username == "admin" and password == "admin":
			tkinter.messagebox.showinfo("login info", "welcome admin")
			self.destroy()
			hp = HomePage(window)

		else:
			tkinter.messagebox.showerror("login error", "incorrect username/password")




class HomePage(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.runBtn = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/runBtn.gif")
		self.Run=tkinter.Button(window,text="Run",command= main_loop,image= self.runBtn, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.5,rely=0.3,anchor= CENTER)
		
		self.databaseBtn = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/databaseBtn.gif")
		self.DataBase=tkinter.Button(window,text="Faces Database",command = self._database,image= self.databaseBtn, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.5, rely=0.5, anchor= CENTER)

		self.logsBtn = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/logsBtn.gif")
		self.LogFiles=tkinter.Button(window,text="Attendance Logs",command= self._logs,image= self.logsBtn, border="0", bg="white",highlightbackground="white",activebackground = "white").place(relx=0.5, rely=0.7, anchor= CENTER)
		#self.Logout=tkinter.Button(window,text="Log Out",command= self._logout, width=15, height=2 ).place(relx=0.5, rely=0.8, anchor= CENTER)



		#JUST logo
		self.justLogo = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/justLogo.gif")
		self.just=tkinter.Button(window,image= self.justLogo, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.1,rely=0.1,anchor= CENTER)
		#JUST text
		self.justText = tkinter.PhotoImage(file="/home/grad-project/Desktop/GraduationProject/Graphics/justText.gif")
		self.just2=tkinter.Button(window,image= self.justText, border="0", bg="white",activebackground = "white",highlightbackground="white").place(relx=0.22,rely=0.1,anchor= CENTER)


	
	def _database(self):
		os.system("xdg-open /home/grad-project/Desktop/GraduationProject/Students")
	def _logs(self):
		os.system("xdg-open /home/grad-project/Desktop/GraduationProject/Attendance")
	#def _logout(self):
	#	self.destroy()
	#	lf = LoginFrame(window).place(relx=0.5,rely=0.5,anchor= CENTER)
		


	




lf = LoginFrame(window).place(relx=0.5,rely=0.5,anchor= CENTER)


	
window.mainloop()

