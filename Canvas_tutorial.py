# Import tkinter library
from tkinter import *
# from tkinter import Tk, Canvas, PhotoImage, NW

# Creating object of the Tk()
window = Tk()


canvas = Canvas(width=1300, height=866, bg='blue')
canvas.pack()

photo = PhotoImage(file='C://Users//Ashutosh//OneDrive - University of Bedfordshire//Taxi Booking images//b.png')

canvas.create_image(0, 0, image=photo, anchor=NW)

window.mainloop()