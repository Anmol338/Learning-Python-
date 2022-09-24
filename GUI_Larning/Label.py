from tkinter import *   # Library import form package tkinter

window_size = Tk()  # Object create
window_size.title("Anmol's Window")             # Title of the window
window_size.iconbitmap('icons/python.ico')      # Icon of the window

window_size.maxsize(width=600,height=700)   # Maximum size of window while maximizing
window_size.minsize(width=600,height=700)   # Maximum size of window while minimizing

##### ----- Label ----- #####
lbl = Label(window_size,text="Hello World of Python !!",bg='black',fg='white',width=50,height=10)

##### ----- pack ----- #####
# lbl.pack()                    # Enable lbl at vertcally and horizontally center of the window

##### ----- grid ----- #####
# lbl.grid()                    # Place the lbl at row = 0 and column =0
# lbl.grid(row=3,column=3)      # Place the lbl at row = 3 and column = 3

##### ----- place ----- #####
lbl.place(x=100,y=10)           # Place lbl at x = 100 (Left to right) and y = 10 (top to buttom)


window_size.mainloop()          # Main loop of the window