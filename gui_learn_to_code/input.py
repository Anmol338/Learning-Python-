from tkinter import Tk, Entry, Button, Label

root = Tk()

myEntry = Entry(root, width=50, bg='#ffffff', fg='#ff00ff', borderwidth=5)
myEntry.pack()
myEntry.insert(0,"Enter your name: ")

def onClick():
    myLabel = Label(root, text=myEntry.get())
    myLabel.pack()

myButton = Button(root, text="Click Me!!!", command=onClick)
myButton.pack()


root.mainloop()