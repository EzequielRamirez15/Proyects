from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
	enlace=videos.get()
	video = YouTube(enlace)
	descarga = video.streams.get_highest_resolution()
	descarga.download()

def popup():
	MessageBox.showinfo("Sobre mi", "Soy Ezequiel Ramirez mejor conocido como Eze15ram xd. Soy un aficionado por la programacion :D")

vent = Tk()
vent.config(bd=15)
vent.title("Down from YouTube")
try:
	vent.iconbitmap('logo.ico')
except Exception:
	"Not Defined"

imagen = PhotoImage(file="C:\\Users\\MINEDUCYT\\Documents\\Python\\descargaryutu\\img\\yutu.png")
foto = Label(vent, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(vent)
vent.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas info", menu= helpmenu)
helpmenu.add_command(label="Info del autor", command= popup)
menubar.add_command(label="Salir", command=vent.destroy)

instrucciones = Label(vent, text= "Programa creado en Python para Descargar videos de YouTube :0\n")
instrucciones.grid(row=0, column=1)

videos= Entry(vent)
videos.grid(row=1, column=1)

boton = Button(vent, text="Descargar :D", command=accion)
boton.grid(row=2, column=1)



vent.mainloop()
