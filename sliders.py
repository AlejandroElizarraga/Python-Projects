from tkinter import *

app =Tk()
app.title('Sliders')

vertical = Scale(app,from_=0, to=200,command=lambda x:Enviar())
vertical.pack()
# El comando de lambda en la definicion del slider vertical 
# Que ocupa la funcion de Enviar con la variable x es 
# Para que se actualice los valores siempre que estos cambien
# (Continuamente)
Horizontal = Scale(app,from_=0, to=200,orient=HORIZONTAL)
Horizontal.pack()

def Enviar():#Esta funcion es para obtener los valores que tienen 
    #los sliders e imprimirlos en la consola
    hor= Horizontal.get()
    ver= vertical.get()
    print(str(hor)+' '+str(ver))

btn= Button(app, text='Enviar',command=Enviar)
btn.pack()
app.mainloop()