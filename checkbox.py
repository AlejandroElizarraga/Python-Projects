from tkinter import *

app =Tk()
app.title('Checkboxs')
app.geometry('500x500')

var =StringVar()
var.set('No')
def Mostrar():
    l =Label(app,text=var.get())
    l.pack()

cb =Checkbutton(app,text='Soy un checkbutton', variable=var,onvalue='Si',offvalue='No')
cb.pack()

btn = Button(app, text='Click',command=Mostrar)
btn.pack()
app.mainloop()