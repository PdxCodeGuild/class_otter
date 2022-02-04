def addition(a, b):
    return a + b

# print(addition(-2, 3))

def hypotenuse(a, b):
    return (a**2 + b**2) ** .5

#print(hypotenuse(5, 7))

def fibonacci(n):
    F = [0, 1]
    count = 2
    while count <= n:
        F.append(F[count - 1] + F[count - 2])
        count += 1
    return F

def fib_golden(nums, a):
    return (nums[a] / nums[a-1])

# print(fibonacci(10))
# print(fibonacci(9))
# print(fib_golden(fibonacci(10), 9))

#print(fibonacci(100))
#34 / 21  9 8=                   1.6190476190476190476190476190476
#144 / 89  12 11=                1.6179775280898876404494382022472
#1597 / 987  18 17=              1.6180344478216818642350557244174
#2584 / 1597  19 18=             1.618033813400125
#196418 / 121393  28 27=         1.618033988780243
#24157817 / 14930352  38 37=                            1.6180339887498968544077192553799
#2971215073 / 1836311903  48 47=                        1.6180339887498948483372108273046
#31940434634990099905 / 19740274219868223167  95 94=    1.6180339887498948482045868343656
#354224848179261915075 / 218922995834555169026  100 99= 1.6180339887498948482045868343656 
"""
from tkinter import *

class App:
	def __init__(self, root, use_geometry, show_buttons):
		fm = Frame(root, width=300, height=200, bg="blue")
		fm.pack(side=TOP, expand=NO, fill=NONE)
		
		if use_geometry:
			root.geometry("600x400")  ### (1) Note geometry Window Manager method

		if show_buttons:			
			Button(fm, text="Button 1", width=10).pack(side=LEFT)
			Button(fm, text="Button 2", width=10).pack(side=LEFT)
			Button(fm, text="Button 3", width=10).pack(side=LEFT)
		

case = 0
for use_geometry in (0, 1):
	for show_buttons in (0,1):
		case = case + 1		
		root = Tk()
		root.wm_title("Case " + str(case))  ### (2) Note wm_title Window Manager method
		display = App(root, use_geometry, show_buttons)
		root.mainloop()
"""

from tkinter import *
 
# globally declare the expression variable
expression = ""
 
 
# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light green")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("270x150")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()