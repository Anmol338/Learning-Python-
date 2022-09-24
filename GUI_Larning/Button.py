from tkinter import *   # Library import form package tkinter

window_size = Tk()  # Object create
window_size.title("Anmol's Window")             # Title of the window
window_size.iconbitmap('icons/python.ico')      # Icon of the window

window_size.maxsize(width=600, height=700)   # Maximum size of window while maximizing
window_size.minsize(width=600, height=700)   # Maximum size of window while minimizing

##### ----- Function Declare ----- #####
def process() :
    store_user = txt_user.get()
    store_pass = txt_pass.get()
    lbl_output_user.config(text=f'Your username is : {store_user}')
    lbl_output_pass.config(text=f'Your password is : {store_pass}')


##### ----- Label ----- #####
lbl_user = Label(window_size, text="Username :- ")
lbl_user.place(x=20, y=10)

lbl_pass = Label(window_size, text="Password :- ")
lbl_pass.place(x=20, y=50)

lbl_output_user = Label(window_size)
lbl_output_user.place(x=20, y=150)

lbl_output_pass = Label(window_size)
lbl_output_pass.place(x=20, y=200)

##### ----- entry ----- #####
txt_user = StringVar()
txt_pass = StringVar()

ent_user = Entry(window_size, width=30, textvariable=txt_user)
ent_user.place(x=150, y=10)

ent_pass = Entry(window_size, width=30, textvariable=txt_pass)
ent_pass.place(x=150, y=50)

##### ----- Button ----- #####
btn = Button(window_size, text="LogIn", command=process)
btn.place(x=150, y=80)


window_size.mainloop()          # Main loop of the window