from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

main= Tk()
main.title("Image Opener")

def OpenIMG():
    global img
    main.filename = filedialog.askopenfilename(initialdir="#Path of Any directory#",title="Select File",filetypes=(("PNG File","*.png"),("JPEG File","*.jpg")))
    img= ImageTk.PhotoImage(Image.open(main.filename))
    L1 = Label(main,image=img).grid(column=0,row=1,columnspan=3)




B1= Button(main,text="Open Image",command= OpenIMG)
B1.grid(column=1,row=0)
main.mainloop()
