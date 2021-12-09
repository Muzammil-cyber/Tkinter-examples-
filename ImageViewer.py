from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Image Viewer")
main.iconbitmap("ImageViewer/Asset 1.png")

imag0 = ImageTk.PhotoImage(
    Image.open("ImageViewer/IMG_1.jpg"))
imag1 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-4.jpg"))
imag2 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-6.jpg"))
imag3 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-7.jpg"))
imag4 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-19.jpg"))
imag5 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-21.jpg"))
imag6 = ImageTk.PhotoImage(
    Image.open("ImageViewer/Snapchat-2.jpg"))

imagelist = [imag0, imag1, imag2, imag3, imag4, imag5, imag6]
listlen = len(imagelist) - 1
posInList = 0

MainImage = Label(main, image=imagelist[posInList])
MainImage.grid(row=1, column=1)


def Back():
    global posInList

    posInList -= 1
    print(posInList)
    MainImage.config(image=imagelist[posInList])
    if posInList == 0:
        BBack.config(state="disabled")


def Forward():
    global posInList

    posInList += 1
    print(posInList)
    MainImage.config(image=imagelist[posInList])
    if posInList == listlen:
        BFront.config(state="disabled")


BBack = Button(main, text="<<<", command=Back)
BExit = Button(main, text="Exit", command=main.destroy)
BFront = Button(main, text=">>>", command=Forward)

BBack.grid(row=1, column=0)
BExit.grid(row=0, column=1)
BFront.grid(row=1, column=2)

mainloop()
