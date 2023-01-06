from tkinter import *
from tkinter import ttk

app = Tk()
app.title('Calculadora')
app.configure(background='#333333')
app.geometry('386x180')

s = ttk.Style()
s.configure(
    "N.TButton",foreground='#2585E6',background='#333333'
)

equation=StringVar
expression_entry=Entry(app,textvariable=equation)
expression_entry.grid(row=0,columnspan=4,sticky='nswe')
#columnspan = utilice las columnas que renderice y max 4 
#sticky = utilizar todo el alto del entry con el string'norht,sur,west.east'
btn7=ttk.Button(app,text='7',style="N.TButton")
btn7.grid(row=1,column=0,sticky='nswe')

btn8 =  ttk.Button(app,text='8',style='N.TButton')
btn8.grid(row=1,column=1,sticky='nswe')

btn9 = ttk.Button(app,text='9',style='N.TButton')
btn9.grid(row=1,column=2,sticky='nswe')

btn4 = ttk.Button(app,text='4',style='N.TButton')
btn4.grid(row=2,column=0,sticky='nswe')

btn5 = ttk.Button(app,text='5',style='N.TButton')
btn5.grid(row=2,column=1,sticky='nswe')

btn6 = ttk.Button(app,text='6',style='N.TButton')
btn6.grid(row=2,column=2,sticky='nswe')

btn1 = ttk.Button(app,text='1',style='N.TButton')
btn1.grid(row=3,column=0,sticky='nswe')

btn2 = ttk.Button(app,text='2',style='N.TButton')
btn2.grid(row=3,column=1,sticky='nswe')

btn3 = ttk.Button(app,text='3',style='N.TButton')
btn3.grid(row=3,column=2,sticky='nswe')

btn0 = ttk.Button(app,text='0',style='N.TButton')
btn0.grid(row=4,column=0,sticky='nswe',columnspan=2)

btnR = ttk.Button(app,text='=',style='N.TButton')
btnR.grid(row=4,column=3,sticky='nswe')

# btncls = ttk.Button(app,text='Clear')
# btncls.grid(row=4,column=2,sticky='nswe')

app.mainloop()