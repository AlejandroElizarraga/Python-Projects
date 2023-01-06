from tkinter import *
from PIL import ImageTk, Image

app = Tk()
app.title('Imagen')

# imagen = Image.open('Bosque.jpg')
# imagen.show()#sirve para llamar al gestor de imagenes nativo de el S.O

img = ImageTk.PhotoImage(Image.open('images/Bosque.jpg'))
#Image.open obtenemos una variable que va a contener la imagen
#PhotoImage tomar la imagen que tenemos en una variable y lo trasformara
#a un tipo de datos que podemos utilizar con Tkinter
l = Label(image=img)
l.pack()
app.mainloop()