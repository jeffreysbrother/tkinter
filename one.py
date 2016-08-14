from Tkinter import *

#create blank window
root = Tk()

def printName():
    print("go fuck yourself")

def rightClick(event):
    print("right clicking PIECE OF TRASH!!!")

def middleClick(event):
    print("wheelclick jackass bitch")

root.title("application")
root.geometry("400x600")

#button
button_1 = Button(root, text="click me", command=printName)

button_1.bind("<Button-2>", rightClick)
button_1.bind("<Button-3>", middleClick)

#labels
label_1 = Label(root, text="name")
label_2 = Label(root, text="password")

#entries
entry_1 = Entry(root)
entry_2 = Entry(root)

#positioning of button, labels and entries
button_1.grid(row=0, column=0)

label_1.grid(row=1, column=0, sticky=E)
label_2.grid(row=2, column=0, sticky=E)

entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)

c = Checkbutton(root, text="male?")
c.grid(columnspan=2)

#make application persist
root.mainloop()


