from Tkinter import *

#create blank window
root = Tk()

# theLabel = Label(root, text="boobies")
# theLabel.pack()
# root.title("penis")
root.geometry("800x1000")

# frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#label
one = Label(root, text="mombo dogface", bg="red", fg="green")
one.pack(fill=X)

two = Label(root, text="mombo dogface", bg="brown", fg="yellow")
two.pack()

#buttons
button1 = Button(topFrame, text="tits", fg="red")
button1.pack(side=LEFT)

button2 = Button(bottomFrame, text="tits", fg="green")
button2.pack(side=LEFT)

#make application persist
root.mainloop()


