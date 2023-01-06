from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

app = Tk()
app.title('Gestor de Archivos')

# app.filename = filedialog.askopenfilename(title='Elige una foto',filetypes=(('Archivos PNG','*.png'),('todos','*')))
# #askopenfilename(Argumento1=Titulo,Argumento2=tipos de archivos: como filtros disponibles)
# l =Label(app,text=app.filename)
# l.pack()
# # El primer label sirve para mostrar la direccion de la imagen
# img = Image.open(app.filename)
# imgTk= ImageTk.PhotoImage(img)
# # Generas la variable que contendra el archivo seleccionado en 
# # askopenfilename en este caso una imagen
# l2 =Label(app, image=imgTk,width=500, height=700)
# l2.pack()
# Generas un Label que contenga la imagen

def open():
    global imgTk
    app.filename = filedialog.askopenfilename(title='Elige una foto',filetypes=(('Archivos PNG','*.png'),('todos','*')))
    l =Label(app,text=app.filename)
    l.pack()
    img = Image.open(app.filename)
    imgTk= ImageTk.PhotoImage(img)

    l2 =Label(app, image=imgTk,width=500, height=700)
    l2.pack()
    
btn=Button(app,text='Cargar Imagen',command=open)
btn.pack()
app.mainloop()