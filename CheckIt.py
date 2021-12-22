from tkinter import *

main = Tk()
main.geometry("400x400")


def select():
    L1 = Label(main, text=var.get())
    L1.pack()


var = StringVar()
var.set("No")
CB = Checkbutton(main, text="I Dare you to Check it", variable=var, onvalue="Yes", offvalue="No")
CB.pack()
B1 = Button(main, text="Selected", command=select)
B1.pack()

main.mainloop()
