from tkinter import *

app = Tk()
app.title('Pies a metros')

def calcular(*args):
    try:
        value =float(pies.get())
        m = int(0.3048*value*10000+0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set('Error')
frame = Frame(app,pady=3,padx=12)
frame.grid(column=0,row=0)

pies = StringVar()#Valor cambiante de pies
pies_input=Entry(frame,width=7,textvariable=pies)#toma el valor del input 
pies_input.grid(column=1,row=0)

metros = StringVar()#Valor cambiante

Label(frame,textvariable=metros).grid(column=1,row=1)#Etiqueta donde se colocara el resultado en metros

Button(frame,text='Calcular',command=calcular).grid(column=2,row=2)

Label(frame,text='Pies: ').grid(column=0,row=0)
Label(frame,text='Es igual a: ').grid(column=0,row=1)
Label(frame,text='Metros').grid(column=3,row=1)
pies_input.focus()#Para que la aplicacion se inicie en un widget
app.bind("<Return>",calcular)#Para hacer que funcione segun se preciona el boton de enter
app.mainloop()