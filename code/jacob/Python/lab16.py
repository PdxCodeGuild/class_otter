import tkinter
from tkinter import *

class MyApp:

    def __init__(self, parent):
        
        button_width = 6

        button_padx = "15m"
        button_pady = "1m"

        buttons_frame_padx = "3m"
        buttons_frame_pady = "1m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack(ipadx = buttons_frame_ipadx, ipady = buttons_frame_ipady, padx = buttons_frame_padx, pady = buttons_frame_pady)


        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello World!" 
        self.button1["background"] = "blue"
        self.button1.bind("<Button-1>", self.button1Click)
        self.button1.focus_force()
        self.button1.configure(width = button_width, padx = button_padx, pady = button_pady)
        self.button1.pack()

        self.button2 = Button(self.myContainer1, command = self.button2Click)
        self.button2.configure(text = "Time to play some games!", background = "teal")
        self.button2.configure(width = button_width, padx = button_padx, pady = button_pady)
        self.button2.pack()
        self.button2.bind("<Return>", self.button2Click_a)

        self.button3 = Button(self.myContainer1)
        self.button3["text"] = "Let's see some more!"
        self.button3["background"] = "orange"
        self.button3.pack(side = LEFT)

        self.button4 = Button(self.myContainer1, command = self.button3Click)
        self.button4.configure(text = 'Addition', background = 'green')
        self.button4.pack()


    def button1Click(self, event):
        print("button1Click event handler")
        if self.button1["background"] == "blue":
            self.button1["background"] = "yellow"
        else:
            self.button1['background'] = "blue"

    def button2Click(self):
        print("button2Click event handler")
        self.myParent.destroy()

    def button3Click(self):
        a = int(input('What numbers to add? '))
        b = int(input('What numbers to add? '))
        print(calculate(a, b))

    def button2Click_a(self, event):
        self.button2Click()



def calculate(a, b):
    return a + b
"""
def report_event(event):
	    
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
	    
    print("Time:", str(event.time))
    print("EventType=" + str(event.type), \
            event_name[str(event.type)],\
            "EventWidgetId=" + str(event.widget), \
		    "EventKeySymbol=" + str(event.keysym) )
"""


root = Tk()
myapp = MyApp(root)                

root.mainloop()