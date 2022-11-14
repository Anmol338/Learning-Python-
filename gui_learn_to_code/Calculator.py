from tkinter import Tk, Entry, Button, END

root = Tk()
root.title("Simple Calculator")

myEntry = Entry(root, width=45, borderwidth=4)
myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = self.a + self.b

    def button_click(self, number):
        current = myEntry.get()
        myEntry.delete(0, END)
        myEntry.insert(0, str(current) + str(number))

    def button_click_clear(self):
        myEntry.delete(0, END)

    def button_click_add(self):
        self.a = int(myEntry.get())
        myEntry.delete(0, END)

    def button_click_equal(self):
        self.b = int(myEntry.get())
        self.sum = self.a + self.b
        myEntry.delete(0, END)
        myEntry.insert(0, self.sum)


calculate = Calc
# Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: calculate.button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: calculate.button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: calculate.button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: calculate.button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: calculate.button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: calculate.button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: calculate.button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: calculate.button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: calculate.button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: calculate.button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command= calculate.button_click_add)
button_equal = Button(root, text="=", padx=91, pady=20, command= calculate.button_click_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command= calculate.button_click_clear)

# Button position on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5,column=1, columnspan=2)

root.mainloop()