from tkinter import *


app =Tk()
app.title('Button app')
app.geometry('300x200')


l =Label(app,text='Impresion')
def click():
    l.pack()

btn =Button(app,text='Activar',command=click,fg='#dd00ee',bg='Blue')
#1er argumento donde se pretende colocar
#2do argumento el texto
#3er argumento la funcion pero sin ejecutarla
#4to argumento fg (foreground) color letras #Acepta Hexagecimal '#'#
#5to argumento bg (background) color de fondo del boton #Acepta Hexagecimal '#'#
btn.pack()









app.mainloop()