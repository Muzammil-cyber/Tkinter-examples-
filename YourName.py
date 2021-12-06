from tkinter import *

# Creating a Main Window
mainWindow = Tk()
# Creating a Feild to Enter Data
Field1 = Entry(mainWindow,width=20,fg = "#FFFFFF",bg = "black",borderwidth=10)
Field1.pack()
Field1.insert(0,"Your Name")
# Showing the Data Enter in the Field When the Button is Pressed
def Clicked():
  # Getting the data enter in the Field
    hello = "Hello " + Field1.get()
    Label1 = Label(mainWindow, text=hello)
    Label1.pack()


button1 = Button(mainWindow, text="!!Click ME!!", padx=50, pady=10,command=Clicked, fg='blue',bg="#000000")
button1.pack()
mainWindow.mainloop()
