from tkinter import Tk, Button, Label

root = Tk()

def myClick():
    myLabel = Label(root, text='Look! I clicked a Button!!')
    myLabel.pack()

myButton = Button(root, text='Click Me!', command=myClick, bg='black', fg='#00ff00')
myButton.pack()

root.mainloop()