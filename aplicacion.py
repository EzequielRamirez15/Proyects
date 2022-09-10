from tkinter import *
import tkinter
from tokenize import Name

ventana = tkinter.Tk()
ventana.title("Aplicación de medidas")
ventana.geometry("900x650")
ventana.resizable(0, 0)
ventana.config(bg="#3F4854")


#-----------------------MENU---------------------
def pag1():
	text1.destroy()
	boton_bienvenida.destroy()
	text2.destroy()

	global bt1, bt2, bt3, bt4, text_a1


	text_a1 = tkinter.Label(ventana, text = "¿Qué deseas hacer?", 
		font = "Arial 30 bold",
		fg = "white", 
		bg = "#3F4854")
	text_a1.place(x = 260, y = 75)

	bt1 = tkinter.Button(ventana, text = "Sucesión aritmética", 
		font = "Calibri 20", 
		relief= tkinter.SOLID, 
		border=1, 
		command=suceari, 
		activebackground='white', 
		bg="#3F4854",
		fg = "white")
	bt1.place(x=170, y= 200)

	bt2 = tkinter.Button(ventana, text = "Sucesión geométrica", 
		font = "Calibri 20", 
		relief= tkinter.SOLID, 
		border=1, 
		command=suceari, 
		activebackground='white', 
		bg="#3F4854",
		fg = "white")
	bt2.place(x=550, y= 200)

	bt3 = tkinter.Button(ventana, text = "Área de una figura", 
		font = "Calibri 20", 
		relief= tkinter.SOLID, 
		border=1, 
		command=suceari, 
		activebackground='white', 
		bg="#3F4854",
		fg = "white")
	bt3.place(x=170, y= 300)

	bt4 = tkinter.Button(ventana, text = "Volumen de un cuerpo", 
		font = "Calibri 20", 
		relief= tkinter.SOLID, 
		border=1, 
		command=suceari, 
		activebackground='white', 
		bg="#3F4854",
		fg = "white")
	bt4.place(x=550, y= 300)

#------------------PRIMER BOTON SUCESION ARITMENTICA--------------
def suceari():
	bt1.destroy()
	bt2.destroy()
	bt3.destroy()
	bt4.destroy()
	text_a1.destroy()

	global bt_back, text_a2, primera_medida, segunda_medida, entrada1, entrada2, tercera_medida, entrada3, bt_check, procescheck, result, mensaje


	bt_back = tkinter.Button(ventana, text = "(←) REGRESAR", 
		font = "Cooper 14 bold",
		relief= tkinter.SOLID, 
		border = 1,
		command=lambda:[pag1(), back_pag1()],
		bg ="#505B6A",
		fg = "white"
		)
	bt_back.place(x=700, y = 40)

	text_a2=tkinter.Label(ventana, text="Este apartado es solamente para encontrar la medida total de \n una sucesión aritmética",
		font = "calibri 20",
		fg = "white",
		bg = "#3F4854")
	text_a2.place(x=105, y=150)

	primera_medida=tkinter.Label(ventana, text="Digite el número inicial: ",
		font = "calibri 15 bold",
		fg = "white",
		bg = "#3F4854")
	primera_medida.place(x = 150, y = 280)

	entrada1 = tkinter.Entry(ventana, width = 12, font = "calibri 14")
	entrada1.place(x = 415, y = 282)
	entrada1.get()

	segunda_medida=tkinter.Label(ventana, text="Digite la distancia o altura: ",
		font = "calibri 15 bold",
		fg = "white",
		bg = "#3F4854")
	segunda_medida.place(x = 150, y = 320)

	entrada2 = tkinter.Entry(ventana, width = 12, font = "calibri 14")
	entrada2.place(x = 415, y = 322)
	entrada2.get()

	tercera_medida=tkinter.Label(ventana, text="Digite el número de bloques: ",
		font = "calibri 15 bold",
		fg = "white",
		bg = "#3F4854")
	tercera_medida.place(x = 150, y = 360)

	entrada3 = tkinter.Entry(ventana, width = 12, font = "calibri 14")
	entrada3.place(x = 415, y = 362)
	entrada3.get()

	def proces():
		procescheck.destroy()

		global result, mensaje


		if entrada1.get() == "" or entrada2.get() == "" or entrada3.get() =="":
			mensaje = tkinter.Label(ventana, text = "Tiene que completar los tres apartados \n para encontrar el resultado total. :)",
				font = "calibri 15",
				fg = "black",
				bg = "white",
				border = "1",
				highlightthickness=4
				)
			mensaje.place(x = 150, y = 500)


		elif entrada1.get() != "" and entrada2.get() != "" and entrada3.get() != "":

			a1 = entrada1.get()
			a2 = entrada2.get()
			a3 = entrada3.get()
			a1 = int(a1)
			a2 = int(a2)
			a3 = int(a3)

			a7 = a1 + a2 * (a3 - 1)
			a4 = "El resultado es el siguiente: \n Si el numero inicial es de: " + str(a1) + ", Su diferencia o altura \n es de: " + str(a2) + ", y el numero de veces por multiplicar es de: " + str(a3) + "\nSe tiene que su altura total es de: " + str(a7)
			result = tkinter.Label(ventana, text = "El resultado es el siguiente: \n Si el numero inicial es de: " + str(a1) + ", Su diferencia o altura \n es de: " + str(a2) + ", y el numero de veces por multiplicar es de: " + str(a3) + "\nSe tiene que su altura total es de: " + str(a7), 
				font = "calibri 16", 
				fg = "#fff", 
				bg = "#3F4854")
			result.place(x = 130, y = 500)


	def proces2():
		bt_back.destroy()
		text_a2.destroy()
		primera_medida.destroy()
		segunda_medida.destroy()
		tercera_medida.destroy()
		entrada2.destroy()
		entrada1.destroy()
		entrada3.destroy()
		bt_check.destroy()


	bt_check = tkinter.Button(ventana, text = "(✓) CALCULAR", 
		font = "Cooper 14 bold",
		relief= tkinter.SOLID, 
		border = 1,
		command=proces,
		bg ="#505B6A",
		fg = "white"
		)
	bt_check.place(x=660, y = 500)

	varR = tkinter.StringVar()

	procescheck = tkinter.Checkbutton(ventana, text = "  Mostrar procedimiento  ", 
		font = "calibri 13", 
		fg = "#fff", 
		bg = "#3F4854",
		onvalue="R", 
		offvalue="nR",
		variable = varR)
	procescheck.deselect()
	procescheck.place(x = 250, y = 410)


#-----------------------------Regresar--------------------------
def back_pag1():
	bt_back.destroy()
	text_a2.destroy()
	primera_medida.destroy()
	segunda_medida.destroy()
	tercera_medida.destroy()
	entrada2.destroy()
	entrada1.destroy()
	entrada3.destroy()
	bt_check.destroy()
	procescheck.destroy()
	result.destroy()
	mensaje.destroy()

def welcome(event):
	pass


#--------------Ventana de bienvenida-------------
text1 = tkinter.Label(ventana, text = "Hola, Bienvenidos", 
	font = "Arial 40 bold",
	fg = "white",
	bg = "#3F4854")
text1.place(x=220, y = 95)

text2 = tkinter.Label(ventana, text = "Está es una aplicación que sigue en proceso de codificación, por \n lo cual todas sus funciones no se encuentran disponibles. \n Esta Aplicación fue creada con el lenguaje de programación de PYTHON \n con el próposito de calcular medidas.",
	font = "calibri 17",
	fg = "#fff",
	bg = "#3F4854")
text2.place(x = 105, y = 200)

#Boton para empezar
boton_bienvenida = tkinter.Button(ventana, text="¡Empezar! :D", 
	font = "Arial 20 bold",
	relief= tkinter.SOLID, 
	border=1, 
	command=pag1, 
	activebackground='white', 
	fg = "#fff",
	bg = "#3F4854",
	cursor = "hand2")
boton_bienvenida.place(x= 345, y = 400)



ventana.mainloop()