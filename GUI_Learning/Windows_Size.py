from tkinter import *   # Library import form package tkinter

window_size = Tk()  # Object create
window_size.title("Anmol's Window")             # Title of the window
window_size.iconbitmap('icons/python.ico')      # Icon of the window

# window_size.maxsize(width=600,height=700)   # Maximum size of window while maximizing
# window_size.minsize(width=600,height=700)   # Maximum size of window while minimizing
window_size.geometry('600x700')               # Minimum size of the window define


window_size.mainloop()      # Main loop of the window