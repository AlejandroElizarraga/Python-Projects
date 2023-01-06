from tkinter import *

app = Tk()
app.title('frame app')
app.geometry('300x200')

# frame = LabelFrame(app, text='Login',padx=10,pady=10,borderwidth=6)
# frame = LabelFrame(app,padx=10,pady=10,borderwidth=6)
frame = Frame(app,padx=10,pady=10,borderwidth=6)
# Solo indicar el widget frame es para hacer un marco 
# imaginario solo para ordenar 
frame.pack(padx=50,pady=50)# es igual a un fieldset
# El argumento de "pad" x-y  es para agregar un padding
# fuera del marco si se indica en el metodo pack
# y dentro del marco si se indica en la creacion del frame

l = Label(frame,text='Estoy dentro de un frame')
l.pack()
btn = Button(frame, text='Salir',command=app.quit)
btn.pack()
app.mainloop()