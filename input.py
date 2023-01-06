from tkinter import *
from tkinter import ttk
# ttk themed tk sirve para darle tema o apariencia a 
# las opciones clasicas de tkinter de igual manera
# seguire usando la libreria para el curso ya que algunas
# funciones se encuentran deshabilitadas o migradas a esta
# libreria

app =Tk()
app.title('entry/input app')
app.geometry('300x200')
## TK OPCION ##

e= Entry(app,width=40)
e.pack()
e.insert(0,'Ingresa texto')
## TTK OPCION ##
# e = ttk.Entry()
# defines el nombre y el tipo de widget
# e.place(x=10, y=10)
# e.insert(0, "Hola mundo!")
#1er argumento es el lugar donde se colocara el texto
#2er argumento el texto que colocaras como placeholder
# def click():
#     textoEtq = e.get()
#     etiqueta.configure(text=textoEtq)

def click1():
    textoEtq = e.get()#Metodo get obtiene el valor de entry/input
    textvar.set(textoEtq)
    # etiqueta = Label(app,text=textoEtq) 
    # etiqueta.pack()
    e.delete(0,END)#Metodo delete borra del indice 0 a el ultimo

btn = Button(app, text='Actualiza',command=click1)
btn.pack()

textvar = StringVar()

etiqueta = Label(app,textvariable=textvar)
etiqueta.pack()

app.mainloop()

############### NOTAS ###############
#Los metodos de los widgets que quieras declarar 
# siempre tienen que estar despues de mostrarlos con pack
# en una linea distinta a la declaracion de los widgets