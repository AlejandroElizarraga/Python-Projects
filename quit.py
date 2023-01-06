from tkinter import *

app = Tk()
app.title('Hola Mundo!')
app.geometry('386x180')

exit=Button(app,text='Salir',command=app.quit)
exit.pack()
app.mainloop()