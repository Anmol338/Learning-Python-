from tkinter import *
from tkinter import messagebox

##------------ Frame Design
display = Tk()
display.title('LogIn')             # Title of the frame
display.geometry('1000x500+300+150')       # (width x height + x-axis + y-axis)
display.configure(bg="#fff")       # background color
display.resizable(False,False)     # Display Resizeable

img = PhotoImage(file='login.png')  # Image
Label(display,image=img,bg='white').place(x=50,y=50) # Image position align


##### ----- Function to check valid useror not ----- #####
def signin():
    user_name = user.get()
    user_pass = password.get()


    if user_name == 'admin' and user_pass == 'password':
        screen = Toplevel(display)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Hello World of Python!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif user_name != 'admin' and user_pass != 'password':
        messagebox.showerror("Invalid","Invalid username or password")

## --------- Adding another frame inside primary frame ----- ##
frame = Frame(display,width=350,height=350,bg="white")
frame.place(x=550,y=60)  # Align the position of the frame

## ----- Heading ----- ##
head = Label(frame,text='Sign In',fg='#94f440',bg='white',font=('Mocrosoft YaHei UI Light',23,'bold'))
head.place(x=100,y=5)

## ----- Function for username ----- ##
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

### ----- Username ----- ###
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Mocrosoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=300,height=2,bg='black').place(x=25,y=107)

## ----- Function for password ----- ##
def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    pas = password.get()
    if pas == '':
        password.insert(0,'Password')

## ----- Password ----- ###
password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Mocrosoft YaHei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)

Frame(frame,width=300,height=2,bg='black').place(x=25,y=177)


## ----- Button ----- ##
Button(frame,width=39,pady=7,text='SignIn',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

## ----- Sign Up ----- ##
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',10))
label.place(x=75,y=270)

## ----- Button ----- ##
sign_up = Button(frame,width=6,text='SignUp',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=220,y=272)

##------------- Frame loop start
display.mainloop()