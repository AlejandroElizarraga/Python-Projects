from tkinter import *
from PIL import ImageTk, Image

app=Tk()
app.title('Ventana')
# SOLUCION 1
# def open():
#     img =ImageTk.PhotoImage(Image.open('images/Bosque.jpg'))
#     top =Toplevel()
#     top.title('Nueva Ventana')
#     l = Label(top,text='Soy un texto en una segunda ventana')
#     l2 =Label(top,image=img,width=500, height=700)
#     l.pack()
#     l2.pack()
#     top.mainloop()
# btn=Button(app,text='Click',command=open).pack()
# app.mainloop()

# DESCRIPCIÓN
# Ventana necesita loop de eventos se pueden colocar widgets pero 
# no imagenes por que sera recolectada por el garbage collector y 
# se perdera la referencia de imagen


# SOLUCION 2
# def open():
#     global img
#     img =ImageTk.PhotoImage(Image.open('images/Bosque.jpg'))
#     top =Toplevel()
#     top.title('Nueva Ventana')
#     l = Label(top,text='Soy un texto en una segunda ventana')
#     l2 =Label(top,image=img,width=500, height=700)
#     l.pack()
#     l2.pack()
# btn=Button(app,text='Click',command=open).pack()
# app.mainloop()

# DESCRIPCIÓN
# Declaras la variable de imagen como global de esta manera el 
# garbage collector no eliminara la variable de imagen

# SOLUCION 3
# def open(img):
#     top =Toplevel()
#     top.title('Nueva Ventana')
#     l = Label(top,text='Soy un texto en una segunda ventana')
#     l2 =Label(top,image=img,width=500, height=700)
#     l.pack()
#     l2.pack()
#     top.mainloop()

# DESCRIPCIÓN
# Defines la imagen en un peldaño por encima de la ventana que se
# esta generando
img =ImageTk.PhotoImage(Image.open('images/Bosque.jpg'))
btn=Button(app,text='Click',command=lambda:open(img)).pack()

app.mainloop()