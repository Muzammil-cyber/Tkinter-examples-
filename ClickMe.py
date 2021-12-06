from tkinter import *

# Creating a Main Window
mainWindow = Tk()


# A Prodecure called when button Clicked
def Clicked():
    Label1 = Label(mainWindow, text="You Clicked me!!!")
    Label1.pack()

# Creating a Button
button1 = Button(mainWindow, text="!!Click ME!!", padx=50, pady=10,command=Clicked, fg='blue',bg="#000000")
# Placing the Button on the Main Window
button1.pack()
mainWindow.mainloop()
