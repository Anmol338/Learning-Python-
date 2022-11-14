from tkinter import Tk, Label

root = Tk()

root.title("Grid")

myLabel = Label(root, text="Hello World")
myLabel1 = Label(root, text="My name is Anmol Shrestha")
myLabel2 = Label(root, text="I am 20 years old.")

# # Pack
# myLabel.pack()
# myLabel1.pack()

# # Grid
# myLabel.grid(row=0, column=0)
# myLabel1.grid(row=1, column=1)
# myLabel2.grid(row=2, column=0)

root.mainloop()