from tkinter import *

# Creating a Main Window
mainWindow = Tk()
# Creating a Label(Hello World)
Label1 = Label(mainWindow, text="Hello World")
Label2 = Label(mainWindow, text="HI!!!")
# Using the Grid System
Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
mainWindow.mainloop()
