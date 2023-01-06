from tkinter import *

app =Tk()
app.title('OptionMenu/Dropdown')
app.geometry('500x500')


def mostrar():
    l =Label(app,text=value.get())
    l.pack()

lista =[
    'Solo Leveling',
    'Mistborn',
    'Stormligth Archive'
]
value =StringVar()
value.set(lista[0])

drop = OptionMenu(app,value,*lista)
drop.pack()



btn = Button(app, text='Click',command=mostrar)
btn.pack()

app.mainloop()