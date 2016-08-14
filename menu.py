from Tkinter import *


def doNothing():
    print("fine, okay.")

root = Tk()

menu = Menu(root)
root.config(menu=menu)
root.geometry("400x600")

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="And then...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ********* Toolbar *********
toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Dingus", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar, text="Pringal", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ********* Status Bar *********
status = Label(root, text="preparing to do nothing like a cold female heart...'", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()