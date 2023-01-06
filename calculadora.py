from tkinter import *

app = Tk()
app.title('Calculadora')
app.configure(background='#333333')
app.geometry('386x180')

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

equation=StringVar()

def press(num):
    equation.set(equation.get()+str(num))

def equalpress():
    try:
        total =str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('Error')

def clear():
    equation.set('')
expression_entry=Entry(app,textvariable=equation)
expression_entry.grid(row=0,columnspan=4,sticky='nswe')
#columnspan = utilice las columnas que renderice y max 4 
#sticky = utilizar todo el alto del entry con el string'norht,sur,west.east'
btn7 = Button(app,text='7',fg='#fff',background='#666',command=lambda: press(7))
btn7.grid(row=1,column=0,sticky='nswe')
btn8=Button(app,text='8',fg='#fff',background='#666',command=lambda: press(8))
btn8.grid(row=1,column=1,sticky='nswe')
btn9=Button(app,text='9',fg='#fff',background='#666',command=lambda: press(9))
btn9.grid(row=1,column=2,sticky='nswe')
btn4=Button(app,text='4',fg='#fff',background='#666',command=lambda: press(4))
btn4.grid(row=2,column=0,sticky='nswe')
btn5=Button(app,text='5',fg='#fff',background='#666',command=lambda: press(5))
btn5.grid(row=2,column=1,sticky='nswe')
btn6=Button(app,text='6',fg='#fff',background='#666',command=lambda: press(6))
btn6.grid(row=2,column=2,sticky='nswe')
btn1=Button(app,text='1',fg='#fff',background='#666',command=lambda: press(1))
btn1.grid(row=3,column=0,sticky='nswe')
btn2=Button(app,text='2',fg='#fff',background='#666',command=lambda: press(2))
btn2.grid(row=3,column=1,sticky='nswe')
btn3=Button(app,text='3',fg='#fff',background='#666',command=lambda: press(3))
btn3.grid(row=3,column=2,sticky='nswe')
btn0=Button(app,text='0',fg='#fff',background='#666',command=lambda: press(0))
btn0.grid(row=4,column=0,sticky='nswe',columnspan=2)
Decimal=Button(app,text='.',fg='#fff',background='#666',command=lambda: press('.'))
Decimal.grid(row=4,column=2,sticky='nswe')

plus=Button(app,text='+',fg='#fff',background='#fe9727',command=lambda: press('+'))
plus.grid(row=1,column=3,sticky='nswe')
minus=Button(app,text='-',fg='#fff',background='#fe9727',command=lambda: press('-'))
minus.grid(row=2,column=3,sticky='nswe')
multiply=Button(app,text='*',fg='#fff',background='#fe9727',command=lambda: press('*'))
multiply.grid(row=3,column=3,sticky='nswe')
divide=Button(app,text='/',fg='#fff',background='#fe9727',command=lambda: press('/'))
divide.grid(row=4,column=3,sticky='nswe')

Resultado=Button(app,text='=',fg='#fff',background='#fe9727',command=equalpress)
Resultado.grid(row=5,column=3,sticky='nswe')
Limpiar=Button(app,text='Clear',fg='#fff',background='#999',command=clear)
Limpiar.grid(row=5,column=2,sticky='nswe')


app.mainloop()