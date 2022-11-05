#button = u click it, then it does stuff

from tkinter import *

count=0
def click():
    global count
    count+=1
    label.config(text=count)

window = Tk()
button = Button(window,text='Click me')
button.config(command=click) #Performs call back of function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.config(activebackground='#FF0000')
button.config(activeforeground='#fffb1f')

image= PhotoImage(file='emo1.png')

button.config(image=image)
button.config(compound='left')
#button.config(state=DISABLED)#active or disabled button
label = Label(window,text=count)
label.config(font=('Monoscape',50))

"""label.config(bg='#ff6200')
label.config(fg='#fffb1f')"""
label.pack()
button.pack()
window.mainloop()
window.geometry("500x500")

"""
#second function
def add():
    print(input("How are u?"))


button2 = Button(window, text='right here! :)')
button2.config(command=add)
"""


def click():
    global count
    count+=1
    label.config(text=count)

window = Tk()
button2 = Button(window,text='Click me')
button2.config(compound='right')
button2.config(command=click) #Performs call back of function
button2.config(font=('Ink Free', 50, 'bold'))
button2.config(bg='#ff6200')
button2.config(fg='#fffb1f')
button2.config(activebackground='#FF0000')
button2.config(activeforeground='#fffb1f')

image= PhotoImage(file='emo1.png')

button2.config(image=image)
button2.config(compound='left')
#button.config(state=DISABLED)#active or disabled button
label = Label(window,text=count)
label.config(font=('Monoscape',50))

"""label.config(bg='#ff6200')
label.config(fg='#fffb1f')"""
label.pack()
button2.pack()
window.mainloop()
window.geometry("500x500")
