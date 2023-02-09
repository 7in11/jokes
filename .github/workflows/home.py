#домик с меняющимися цветами
from tkinter import *
list1 = ["yellow","red", "blue","violet","orange"]  #список цветов
def change():                                                           #создание функции по смене цвета
    if list1.index(canvas.itemcget(square, 'fill')) < len(list1)-1:
        canvas.itemconfig(square, fill=list1[list1.index(canvas.itemcget(square, 'fill'))+1])
    else:
        canvas.itemconfig(square, fill="yellow")
def changetr():
    if list1.index(canvas.itemcget(tr, 'fill')) < len(list1)-1:
        canvas.itemconfig(tr, fill=list1[list1.index(canvas.itemcget(tr, 'fill'))+1])
    else:
        canvas.itemconfig(tr, fill="yellow")
def changeo():
    if list1.index(canvas.itemcget(oval, 'fill')) < len(list1)-1:
        canvas.itemconfig(oval, fill=list1[list1.index(canvas.itemcget(oval, 'fill'))+1])
    else:
        canvas.itemconfig(oval, fill="yellow")          
root=Tk()                                                                #создание окна
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
square = canvas.create_rectangle(50, 100, 150, 200, fill='yellow')     #создание фигур
tr = canvas.create_polygon(50,100, 100, 50, 150, 100, fill='yellow')
oval = canvas.create_oval(150,20, 170, 40, fill='yellow')
b1 = Button(text='основание', command=change).pack()                   #создание кнопок
b2 = Button(text='крыша', command=changetr).pack()
b3 = Button(text='солнце', command=changeo).pack()
root.mainloop()
