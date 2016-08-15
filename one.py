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

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

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


