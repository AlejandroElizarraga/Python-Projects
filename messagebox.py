from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Message-box')
# def click ():
#     messagebox.showwarning('Popup','Hola Mundo')
# def click ():
#     messagebox.showinfo('Popup','Hola Mundo')
# def click ():
#     messagebox.showerror('Popup','Hola Mundo')

# def click ():
#     respuesta=messagebox.askquestion('Popup','Hola Mundo')
#     print(respuesta)
#     if respuesta == 'yes': 
#         messagebox.showinfo('Respuesta','La respuesta fue '+ respuesta)
#     else: 
#         messagebox.showerror('Respuesta','La respuesta fue '+respuesta)

# def click ():
#     respuesta=messagebox.askokcancel('Ask','desea realizar la acción')
#     print(respuesta)
#     if respuesta :
#         messagebox.showinfo('info','La respuesta fue Ok')
#     else:
#         messagebox.showerror('info','La respuesta fue negativa')

def click ():
    respuesta=messagebox.askyesno('Ask','desea realizar la acción')
    print(respuesta)
    if respuesta :
        messagebox.showinfo('info','La respuesta fue Ok')
    else:
        messagebox.showerror('info','La respuesta fue negativa')
        
btn =Button(app,text='Presioname',command=click)
btn.pack()

app.mainloop()