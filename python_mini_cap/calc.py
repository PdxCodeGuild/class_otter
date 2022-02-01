import tkinter as tk

large_font_type = ("arial", 40, "bold")
small_font_type = ("arial", 16)
digits_font_type = ("Arial", 24, "bold")
default_font_type = ("Arial", 20)

off_white = "#F8FAFF"
white = "#FFFFFF"
light_blue = "#CCEDFF"
antique_white = "#FFEFDB" # sets variable to use the color antique white which has a Hex value of #FFEFDB
labels_color = "#2F4F4F"   # sets variable to use the color Dark Slate Gray which has a Hex value of #2F4F4F

class Calculator:
    
    def __init__(self):
        self.window = tk.Tk() # Main window using the tk class of tkinter
        self.window.geometry("375x667") # Set main Window size
        self.window.resizable(0, 0) # Disables resizing of the window
        self.window.title("Calculator")
        
        self.total = 0 #variable for 'Total' Label
        self.current_op = 0 #variable for 'Current Operation' Label
        self.display_frame = self.create_display_frame() #Variable for Create Display Frame
        
        self.total_label, self.label = self.create_display_labels() # ties to Method
        
        # dictionary represents digit value number: and the Grid value (row, column)
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} # Dict maps python arithmatic operations to the operation symbols; 
        # \u00f7 is the Hex representation of Divide and \u00D7 Hex for Multiply
        self.buttons_frame = self.create_buttons_frame() #Variable for Create Buttons Frame
  
            
    # def create_special_buttons(self):

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total, anchor=tk.E, bg =antique_white, fg = labels_color, padx= 24, font=small_font_type) # Uses Tk Label Class (Widget) 
        #'anchor=Tk.E' to position text at the East (Right) side of Frame, 'bg' is background color and 'fg' is foreground(label) color. 'padx' creates a space around label,
        # 'font' = arial typeset at 16-point
        total_label.pack(expand=True, fill="both") # Pack frame to  Main window allowing it to expand and fill empty space around it
        
        label = tk.Label(self.display_frame, text = self.current_op, anchor=tk.E, bg =antique_white, fg = labels_color, padx= 24, font=large_font_type) # Uses Tk Label Class (Widget) 
        #'anchor=Tk.E' to position text at the East (Right) side of Frame, 'bg' is background color and 'fg' is foreground(label) color. 'padx' creates a space around label,
        # 'font' = arial typeset at 40-point bold
        label.pack(expand=True, fill="both") # Pack frame to  Main window allowing it to expand and fill empty space around it
        
        return total_label, label
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=antique_white) #uses Tk Frame Class (Widget) to config Frame inside Main Window. also setting height, and background color (bg)
        frame.pack(expand=True, fill ="both") # Pack frame to  Main window allowing it to expand and fill empty space around it
        return frame
    
    # def add_to_current_op(self, value): # def current operation 
    #     self.current_op += str(value)
    #     self.update_label()
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=white, fg=labels_color, font=digits_font_type, borderwidth=0) # Uses Tk Button Class (Widget) to config button frame. Convert the integer digit to a string
            #boarderwidth=0 sets no border
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW) # ties button to grid row first position [0] and column second position [1]. Sticky north, south, east and west so buttons "stick to every side and fills up the entire cell"
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window) #uses tk Frame method to config it inside Main Window.
        frame.pack(expand=True, fill ="both") # Pack frame to  Main window allowing it to expand and fill empty space around it
        return frame 
        
    # def create_operator_buttons():    
        
            
        
    def run(self):
        self.window.mainloop() # Start Calculator App
        
        
if  __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
    
         
        
        