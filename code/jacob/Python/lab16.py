import tkinter
from tkinter import *


class MyApp:

    def __init__(self, parent):
        
        self.myParent = parent
        #self.myParent.geometry("640x640")
        
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        
        ### constants for scale of layout----------
        button_width = 6

        button_padx = "15m"
        button_pady = "1m"

        buttons_frame_padx = "3m"
        buttons_frame_pady = "1m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        ###----------------------------------------
        
        self.buttons_frame = Frame(self.myContainer1)
        self.buttons_frame.pack(side = TOP, ipadx = buttons_frame_ipadx, ipady = buttons_frame_ipady, padx = buttons_frame_padx, pady = buttons_frame_pady)
        
        self.top_frame = Frame(self.myContainer1)
        self.top_frame.pack(side = TOP, fill = BOTH, expand = YES)

        self.bottom_frame = Frame(self.myContainer1, borderwidth = 5, relief = RIDGE, height = 200, background = "white", width=550)
        self.bottom_frame.pack(side = TOP, fill = BOTH, expand = YES)

        self.left_frame = Frame(self.top_frame, background = "blue", borderwidth=5, relief=RIDGE, height=200, width=250)
        self.left_frame.pack(fill=BOTH, expand=YES)

        self.right_frame = Frame(self.top_frame, background="yellow", borderwidth=5, relief=RIDGE, height=100, width=550)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.right_frame2 = Frame(self.bottom_frame, background="yellow", borderwidth=5, relief=RIDGE, height=100, width=250)
        self.right_frame2.pack(side=LEFT, fill=BOTH, expand=YES)

        self.right_frame3 = Frame(self.bottom_frame, background="green", borderwidth=5, relief=RIDGE, height=100, width=250)
        self.right_frame3.pack(side=RIGHT, fill=BOTH, expand=YES)


        self.button1 = Button(self.right_frame2, command = self.button1Click) 
        self.button1["text"] = "Hello World!" 
        self.button1["background"] = "blue"
        self.button1.bind("<Return>", self.button1Click_a)
        self.button1.focus_force()
        self.button1.configure(width = button_width, padx = button_padx, pady = button_pady)
        self.button1.pack(pady=125)

        self.button2 = Button(self.myContainer1, command = self.button2Click)
        self.button2.configure(text = "Close", background = "red")
        self.button2.configure(width = button_width, padx = button_padx, pady = button_pady)
        self.button2.pack(side=RIGHT, pady=100)
        self.button2.bind("<Return>", self.button2Click_a)

        self.button3 = Button(self.myContainer1)
        self.button3["text"] = "Let's see some more!"
        self.button3["background"] = "orange"
        self.button3.pack(side = LEFT)

        self.button4 = Button(self.right_frame3, command = self.button3Click)
        self.button4.configure(text = 'Addition', background = 'white')
        self.button4.place(x = 120, y = 100)

        self.button5 = Button(self.right_frame3, command = self.button4Click)
        self.button5.configure(text = 'Subtraction', background = 'white')
        self.button5.place(x = 45, y = 130)

        self.button6 = Button(self.right_frame3, command = self.button5Click)
        self.button6.configure(text = 'Multiplication', background = 'white')
        self.button6.place(x = 100, y = 160)

        self.button7 = Button(self.right_frame3, command = self.button6Click)
        self.button7.configure(text = 'Division', background = 'white')
        self.button7.place(x = 175, y = 130)

        self.text_add1 = StringVar()
      
        self.add1_field = Entry(self.right_frame3, textvariable = self.text_add1)
        self.add1_field.place(x=80, y=10)
        
        self.text_add2 = StringVar()
      
        self.add2_field = Entry(self.right_frame3, textvariable = self.text_add2)
        self.add2_field.place(x=80, y=35)
        
        self.text_output = StringVar()
      
        self.expression_field = Entry(self.right_frame3, textvariable = self.text_output)
        self.expression_field.place(x=80, y=60)

    def button1Click(self):
        
        if self.button1["background"] == "blue":
            self.button1["background"] = "yellow"
            self.right_frame2["background"] = "blue"  
            
        else:
            self.button1['background'] = "blue"
            self.right_frame2['background'] = "yellow"  
    
    def button2Click(self):
        
        self.myParent.destroy()

    def button3Click(self):
        a = int(self.add1_field.get())
        b = int(self.add2_field.get())
        self.text_output.set(add_nums(a, b))

    def button4Click(self):
        a = int(self.add1_field.get())    
        b = int(self.add2_field.get())
        self.text_output.set(sub_nums(a, b))

    def button5Click(self):
        a = int(self.add1_field.get())    
        b = int(self.add2_field.get())
        self.text_output.set(mult_nums(a, b))

    def button6Click(self):
        a = int(self.add1_field.get())    
        b = int(self.add2_field.get())
        self.text_output.set(div_nums(a, b))

    def button1Click_a(self, event):
        self.button1Click()
    
    def button2Click_a(self, event):
        self.button2Click()



def add_nums(a, b):
    return (a + b)

def sub_nums(a, b):
    return (a - b)

def mult_nums(a, b):
    return (a * b)

def div_nums(a, b):
    return (a / b)

root = Tk()
root.wm_title("Testing")
myapp = MyApp(root)                

root.mainloop()