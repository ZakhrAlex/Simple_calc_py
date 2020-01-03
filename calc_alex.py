from tkinter import *


def add(event):
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    result = number1 + number2
    entry3.insert("0", str(result))


def minus(event):
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    result = number1 - number2
    entry3.insert("0", str(result))

def multy(event):
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    result = number1 * number2
    entry3.insert("0", str(result))

def devid(event):
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    result = number1 / number2
    entry3.insert("0", str(result))

def clear(event):
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    return

win = Tk()
frame1 = Frame(win)
frame1.pack()

frame2 = Frame(win)
frame2.pack()

frame3 = Frame(win)
frame3.pack()

# Frame1
label1 = Label(frame1, text='Число 1:')
label1.pack(side="left")

entry1 = Entry(frame1)
entry1.pack(side="left")

# Frame2
label2 = Label(frame2, text='Число 2:')
label2.pack(side="left")
entry2 = Entry(frame2)
entry2.pack(side="left")

# Frame3
btnPlus = Button(frame3, text=' + ')
btnPlus.pack(side="left")
btnPlus.bind("<Button-1>", add)

btnPlus = Button(frame3, text=' - ')
btnPlus.pack(side="left")
btnPlus.bind("<Button-1>", minus)

btnPlus = Button(frame3, text=' * ')
btnPlus.pack(side="left")
btnPlus.bind("<Button-1>", multy)

btnPlus = Button(frame3, text=' / ')
btnPlus.pack(side="left")
btnPlus.bind("<Button-1>", devid)

btnClear = Button(frame3, text=' AC ')
btnClear.pack(side="left")
btnClear.bind("<Button-1>", clear)

label3 = Label(win, text='Результат:')
label3.pack()
entry3 = Entry(win)
entry3.pack()

win.mainloop()
