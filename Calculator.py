from tkinter import *

main = Tk()
main.title("Calculator")
# Entry Field
Field = Entry(main, width=30, borderwidth=5)
Field.grid(row=0, column=0, columnspan=3)
total = 0
firstnum = True
presign = ""


def Noclicked(number):
    Field.insert(END, number)


def Sign(sign):
    global total, firstnum, presign
    if firstnum:
        total = int(Field.get())
        Field.delete(0, END)
        firstnum = False
        presign = sign
    else:
        if presign == "+":
            total += int(Field.get())
            Field.delete(0, END)
        elif presign == "-":
            total -= int(Field.get())
            Field.delete(0, END)
        presign = sign


def Display():
    global total, presign
    if presign == "+":
        total += int(Field.get())
        presign = ""
    elif presign == "-":
        total -= int(Field.get())
        presign = ""
    elif presign == "":
        total = int(Field.get())
    Field.delete(0, END)
    Field.insert(0, str(total))


def CLEAR():
    global total, firstnum, presign
    total = 0
    firstnum = True
    presign = ""
    Field.delete(0, END)


# Define Number Buttons
B1 = Button(main, text="1", width=10, command=lambda: Noclicked(1))
B2 = Button(main, text="2", width=10, command=lambda: Noclicked(2))
B3 = Button(main, text="3", width=10, command=lambda: Noclicked(3))
B4 = Button(main, text="4", width=10, command=lambda: Noclicked(4))
B5 = Button(main, text="5", width=10, command=lambda: Noclicked(5))
B6 = Button(main, text="6", width=10, command=lambda: Noclicked(6))
B7 = Button(main, text="7", width=10, command=lambda: Noclicked(7))
B8 = Button(main, text="8", width=10, command=lambda: Noclicked(8))
B9 = Button(main, text="9", width=10, command=lambda: Noclicked(9))
B0 = Button(main, text="0", width=10, command=lambda: Noclicked(0))

Bplus = Button(main, text="+", width=10, command=lambda: Sign("+"))
Bminus = Button(main, text="-", width=10, command=lambda: Sign("-"))
Bequal = Button(main, text="=", width=10, command=Display)
Bclear = Button(main, text="Clear", width=23, command=CLEAR)

B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)

B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)

B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)

B0.grid(row=4, column=0)
Bplus.grid(row=4, column=1)
Bminus.grid(row=4, column=2)
Bequal.grid(row=5, column=0)
Bclear.grid(row=5, column=1, columnspan=2)
main.mainloop()

