from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox
import tkinter
import tkinter as tk

vent = tk.Tk()
vent.title("Esta es la hora bro :D")
vent.geometry("1000x700")
vent.resizable(False,False)
vent.config(bg="#416DB2")


vent.iconbitmap("C:/Users/MINEDUCYT/Documents/Python/temporizador/reloj.ico")


#--------------------------MENU--------------------------------

def temp():
	txt1.destroy()
	txt2.destroy()


	global txta1, txta2, entrada, i, hourS, minuteS, secondS, setTimeButton, hourTextbox, minuteTextbox, secondTextbox

	#----------------temporizador---------------------
	

	txta1=tk.Label(vent, text = "TEMPORIZADOR", 
	font = "Arial 40 bold",
	fg = "white",
	bg = "#416DB2")
	txta1.place(x=275, y = 95)


	### Declare variables
	hourS = tk.StringVar()
	minuteS = tk.StringVar()
	secondS = tk.StringVar()

	### Set strings to default value
	hourS.set(" 00")
	minuteS.set(" 00")
	secondS.set(" 00")

	### Get user input
	hourTextbox = Entry(vent, width=3, font=("Calibri", 60, ""), textvariable=hourS)
	minuteTextbox = Entry(vent, width=3, font=("Calibri", 60, ""), textvariable=minuteS)
	secondTextbox = Entry(vent, width=3, font=("Calibri", 60, ""), textvariable=secondS)

	### Center textboxes
	hourTextbox.place(x=290, y=230)
	minuteTextbox.place(x=440, y=230)
	secondTextbox.place(x=590, y=230)

	def runTimer():
	    try:
	        clockTime = int(hourS.get())*3600 + int(minuteS.get())*60 + int(secondS.get())
	    except:
	        print("Incorrect values")
	
	    while(clockTime > -1):
	        
	        totalMinutes, totalSeconds = divmod(clockTime, 60)
	
	        totalHours = 0
	        if(totalMinutes > 60):
	            totalHours, totalMinutes = divmod(totalMinutes, 60)
	
	        hourS.set("{0:2d}".format(totalHours))
	        minuteS.set("{0:2d}".format(totalMinutes))
	        secondS.set("{0:2d}".format(totalSeconds))
	
	        ### Update the interface
	        vent.update()
	        time.sleep(1)
	
	        ### Let the user know if the timer has expired
	        if(clockTime == 0):
	            messagebox.showinfo("Ojito!", "El tiempo se acabo! :0")
	
	        clockTime -= 1
	
	
	setTimeButton = Button(vent, text='INICIAR', bd='0', font="Arial 20", command=runTimer)
	setTimeButton.place(x= 440, y=400)



#--------------------------INICIO2--------------------------------
def inicio():
	txta1.destroy()
	setTimeButton.destroy()
	hourTextbox.destroy()
	minuteTextbox.destroy()
	secondTextbox.destroy()


	global txt1, specialtext, txt2

	txt1=tk.Label(vent, text = "HORA - TEMP", 
	font = "Arial 40 bold",
	fg = "white",
	bg = "#416DB2")
	txt1.place(x=310, y = 165)

	specialtext=tk.Label(vent, text = "This aplication was created thinking on AMCR",
		font = "Arial 10",
		fg = "white",
		bg = "#416DB2")
	specialtext.place(x=350, y=650)

	txt2 = tk.Label(text=time.strftime('%H:%M:%S'),
		font = "calibri 95",
		fg = "#fff",
		bg = "#416DB2")
	txt2.place(x = 260, y = 250)
	print(txt2['text'])

	def update_clock():
		time_now = time.strftime('%H:%M:%S')
		
		try:
			if txt2['text'] != time_now:
				txt2['text'] = time_now
		except:
			"Invalid command name"

		vent.after(1000, update_clock)


	update_clock()



#---------------------------INICIO-------------------------------
txt1=tk.Label(vent, text = "HORA - TEMP", 
	font = "Arial 40 bold",
	fg = "white",
	bg = "#416DB2")
txt1.place(x=310, y = 165)

specialtext=tk.Label(vent, text = "This aplication was created thinking on AMCR",
	font = "Arial 10",
	fg = "white",
	bg = "#416DB2")
specialtext.place(x=350, y=650)

txt2 = tk.Label(text=time.strftime('%H:%M:%S'),
	font = "calibri 95",
	fg = "#fff",
	bg = "#416DB2")
txt2.place(x = 260, y = 250)
print(txt2['text'])

def update_clock():
	time_now = time.strftime('%H:%M:%S')

	try:
		if txt2['text'] != time_now:
			txt2['text'] = time_now
	except:
		"Invalid command name"

	vent.after(1000, update_clock)

update_clock()


#--------------Botones--------------
btn_temp = tk.Button(vent, text = "TEMPORIZADOR",
	font = "Arial 20 bold",
	relief = tkinter.SOLID,
	activeforeground="#fff",
	command = temp, width=31, height=1, anchor="center",
	border = 0,
	activebackground = "#305E9E",
	fg = "#fff",
	bg = "#416DB2"
	)
btn_temp.place(x=500, y=1)


btn_ini = tk.Button(vent, text = "INICIO",
	font = "Arial 20 bold",
	relief = tkinter.SOLID,
	activeforeground="#fff",
	command = inicio, width=31, height=1, anchor="center",
	border = 0,
	activebackground = "#305E9E",
	fg = "#fff",
	bg = "#416DB2"
	)
btn_ini.place(x=0, y=1)


vent.mainloop()