from tkinter import *

app =Tk()
app.title('Radio Button')

# r = IntVar()
# r.set('2')
# Radiobutton(app,text='Opcion 1', variable=r,value=1).pack()
# Radiobutton(app,text='Opcion 2', variable=r,value=2).pack()
LIBROS =[
    ('Solo','Leveling'),
    ('Sucide','Hero'),
    ('Mist','Born'),
    ('Storm','light')
] 
#Se crea una lista con 2 valores: El primero se asignara al
#radio button y el segundo al label

book = StringVar()
book.set('Leveling')
#Se asigna un valor predeterminado para la variable label 
for text, libro in LIBROS:
    Radiobutton(app,text=text,variable=book,value=libro).pack()
# Se itera el primer texto x elemento de la lista de "LIBROS"
# Cada ves que se itera se genera un Radiobutton
# Que contiene el texto,la variable "book", y el segundo valor de 
# los elementos de las filas
l = Label(app,textvariable=book)
l.pack()
app.mainloop()