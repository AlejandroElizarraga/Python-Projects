from tkinter import *

root = Tk()

root.title('Hello World')#Nombre de la pestaña de la aplicación
root.geometry('400x400')#Es para indicar el Ancho y el alto de la ventana respectivamente

### FORMA  LARGA ####

# label = Label(root, text='Necesito trabajo')#1er argumento es donde se pretende colocar, 2do argumento es el texto a escribir# Esto es solo la definicion falta colocarlo
# label.pack()#Sirve para que el elemento sea visible 

### FORMA CORTA ###

#Etiqueta = Label(root,text='Forma corta').pack()#instruccion pack solo es para mostrarlo (lo centra)#
Etiqueta1 = Label(root,text='Hola Mundo!')
Etiqueta2 = Label(root,text='Forma corta 2')

Etiqueta1.grid(row=0, column=0)
Etiqueta2.grid(row=0, column=1)

# Se tiene que agrandar con mas elementos si es que se requiere acomodar los elementos principales #
root.mainloop() #Estara constantemente escuchando el programa por posibles cambios 

