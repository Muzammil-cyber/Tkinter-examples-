from tkinter import *

main = Tk()
main.title("Select Your Pizza Topping")

Toppings = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom")
]

pizza = StringVar()
pizza.set("Cheese")
# For integer
# number = IntVar()

for text , mode in Toppings:
    Radiobutton(main,text= text, variable=pizza, value= mode).pack(anchor=W)

def Clicked(topping):
    label.config(text= topping)

button = Button(main, text = "Done", command= lambda: Clicked(pizza.get()))
button.pack()
frame = LabelFrame(main, text="Selected Topping", padx=5,pady=5)
frame.pack(pady=5,padx=5)
label = Label(frame,text = pizza.get())
label.pack()

main.mainloop()
