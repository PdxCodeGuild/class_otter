'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*          Python Mini-Capstone             *
*           "The Calc-In-Ator"              *
*              01/February/2022             *
*                                           *
*********************************************
'''
import tkinter as tk

#*************Define Font Types******************************

large_font_type = ("arial", 40, "bold") # <<<|
small_font_type = ("arial", 16) # <<<<<<<<<<<|
digits_font_type = ("arial", 24, "bold") # <<|<<--- defines typeset, size and any special font settings, i.e., "bold"
default_font_type = ("arial", 20) # <<<<<<<<<|

#*************Define Colors******************************

labels_color = "#2F4F4F" # <<<|  
ivory1	= "#FFFFF0" # <<<<<<<<|
ivory3	= "#CDCDC1" # <<<<<<<<| 
lightcyan1	= "#E0FFFF"# <<<<<|<<--  # Sets variable to the color by passing it's Unicode Hex value.
paleturquoise3 = "#96CDCD"# <<|
paleturquoise1 = "#BBFFFF"# <<|
silver	= "#C0C0C0"# <<<<<<<<<|

#*************Create Class; setup variables; Construct GUI Elements; Add Operation Functionality ********************
class Calculator:
    
    def __init__(self): # Class __init__ Method
        self.window = tk.Tk() # Main window using the tk class of tkinter.
        self.window.geometry("375x667") # Set main Window size 4" x 7".
        self.window.resizable(0, 0) # Disables resizing of the window.
        self.window.title("The Calc-In-Ator")  # Sets title of Window.
        
        self.total = "" # assign variable for 'Total' Label string.
        self.current_op = "" # assign variable for 'Current Operation' Label.
        self.display_frame = self.create_display_frame() #Variable for Create Display Frame.
        
        self.total_label, self.label = self.create_display_labels() # ties variables to the Method.
        
        # dictionary represents digit value number: and the Grid value (row, column).
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} # Dict maps python arithmatic operations to the operation symbols; "\u00f7" is the Hex representation of Divide -->>
        # and "\u00D7" Hex for Multiply.
        
        self.buttons_frame = self.create_buttons_frame()  #Variable for Create Buttons Frame
        self.buttons_frame.rowconfigure(0, weight=1) # Non zero weight allows for expansion equivalent to 1 part of the total expandable area
        
        for x in range(1, 5): #Loop through rows and columns within the Button Frame giving them an even weight of 1 for equal allowed expansion
            self.buttons_frame.rowconfigure(x, weight=1) # Row position, allow for 1 part of expandable area.
            self.buttons_frame.columnconfigure(x, weight=1) # Column position, allow for 1 part of expandable area.
            
        self.create_digit_buttons()    #<<--|
        self.create_operator_buttons() #<<--|<<-- Call Methods
        self.create_special_buttons()  #<<--|
        self.bind_keys() # <<<<<<<<<<<<<<<--|
        
    def create_special_buttons(self): # Method to create special buttons. 
        self.create_clear_button() # Call Create 'Clear' button method.
        self.create_equals_button() # Call Create 'Equals' button method.
        self.create_square_button() # Call Create 'Square' button method.
        self.create_sqrt_button() # Call Create 'Sqrt' button method.
        
#*****************Define Display****************************
        
    def create_display_frame(self): # Create the calculator's output display frame
        frame = tk.Frame(self.window, height= 221, bg= silver) # Uses Tk Frame Class (Widget) to config Frame inside Main Window. also setting height, and background color (bg).
        frame.pack(expand= True, fill= "both") # Pack frame to  Main window allowing it to expand and fill empty space around it.
        return frame
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text= self.total, anchor= tk.E, bg= paleturquoise3, fg= labels_color, highlightbackground= silver, highlightthickness=2, relief= "sunken", padx= 24, font= small_font_type) # Uses Tk Label Class (Widget) -
        #'anchor=Tk.E' to position text at the East (Right) side of Frame, 'bg' is background color and 'fg' is foreground(label) color. 'padx' creates a space around label, -
        # 'font' = arial typeset at 16-point.
        total_label.pack(expand=True, fill="both") # Pack frame to  Main window allowing it to expand and fill empty space around it.
        
        label = tk.Label(self.display_frame, text= self.current_op, anchor=tk.E, bg= paleturquoise1, fg= labels_color, highlightbackground= silver, highlightthickness=2, relief= "sunken", padx= 24, font= large_font_type) # Uses Tk Label Class (Widget) =
        #'anchor=Tk.E' to position text at the East (Right) side of Frame, 'bg' is background color and 'fg' is foreground(label) color. 'padx' creates a space around label, -
        # 'font' = arial typeset at 40-point bold.
        label.pack(expand= True, fill= "both") # Uses the 'pack' layout manager to organize the label and it's parameters (passed from the 'label' variable) within it's allowed horizontal and verticle area. 
        #The geometry is determined by the parameters of the 'label' variable and set the parameters to expand to the geometry limits of the frame, determined in the Button Creation Methods, -->>
        # and to fill (utilize) the area both horizontally (X) and vertically (Y).
        
        return total_label, label
    
#***************** Define Buttons*************************
    
    def create_buttons_frame(self): # Method to create button frames.
        frame = tk.Frame(self.window) # Sets frame variable = to tk Frame method(self.window).
        frame.pack(expand=True, fill= "both") # Uses 'pack' layout manager to set the parameters to expand to the geometry limits of the frame, determined in the Button Creation Methods, -->>
        # and to fill (utilize) the area both horizontally (X) and vertically (Y).
        return frame 
    
    def create_digit_buttons(self): # Method to set the buttons digit, defined in the self.digits Dictionary.
        for digit, grid_value in self.digits.items(): # Loop through digit numbers and their grid position from the Dictionary.
            button = tk.Button(self.buttons_frame, text=str(digit), bg=ivory1, fg=labels_color, font=digits_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=lambda x=digit: self.add_to_op(x)) # Uses Tk Button Class (Widget) -->>
            # with args in order to config the button characteristics, then assigns the functionality for the button through "command=lambda x=digit:" i.e, WHEN [_ButtonCommand(command) -->>
            # 'return the callback' (lambda) = 'specific digit' (x):] IS PRESSED, ASSIGN 'specific function(x)'. 
            # Since the dict "digit" holds 'Integers' must convert to a string obj to pass as arg; "text=str(digit)" boarderwidth=0 sets no border.
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW) # Ties button to grid row first position [0] and column second position [1], -->>
            # sticky=tk.NSEW (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell".
            
    def create_operator_buttons(self): # Method to Create Operation Buttons
        i = 0 # row positional counter
        for operator, symbol in self.operations.items(): # loop through Dict to get operator:symbol values
            button = tk.Button(self.buttons_frame, text=symbol, bg=ivory3, fg=labels_color,font=default_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=lambda x=operator: self.append_operator(x)) # -->>
            #  Uses Tk Button Class (Widget) with args in order to config the button characteristics, then assigns the functionality for the button through "command=lambda x=operator:" i.e, 
            # WHEN [_ButtonCommand(command) = 'return the callback' (lambda) = '(x)' (the value of 'operator:)] IS PRESSED, ASSIGN 'specific function(x)'. 
            button.grid(row=i, column=4, sticky=tk.NSEW) # Configure Operators to reside at row position 'defined by i' and along the column 4 vertical, -->>
            # sticky=tk.NSEW (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell". 
            i += 1 # increment row positional counter by 1.
            
    def create_equals_button(self): # Method to create 'Equals' Button
        button = tk.Button(self.buttons_frame, text="=", bg=lightcyan1, fg=labels_color, font=default_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=self.evaluate) # Uses Tk Button Class (Widget) to assign configuration to button -->>
        # Finally, assigns functionality to button through 'command=self.evaluate' i.e., WHEN [_ButtonCommand(command) IS PRESSED, assign 'self.evaluate' function. 
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW) # Configure "Equals" button position, use columnspan to stretch it accross 2 columns (west to east) -->>
        # sticky=tk.NSEW (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell."
        
    def create_clear_button(self): # Method to create 'Clear' Button
        button = tk.Button(self.buttons_frame, text="C", bg=ivory3, fg=labels_color,font=default_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=self.clear) # Uses Tk Button Class (Widget) to assign configuration to button -->>
        #Finally assigns functionality to button through 'command=self.clear' i.e., WHEN [_ButtonCommand(command) IS PRESSED, assign 'self.clear' function. 
        button.grid(row=0, column=1, sticky=tk.NSEW) # Configure "Clear" button position, 'sticky=tk.NSEW' (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell". 
        
    def create_square_button(self): # Method to create 'Square' Button
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=ivory3, fg=labels_color, font=default_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=self.square) # Uses Tk Button Class (Widget) to assign configuration -->>
        #('x\u00b2' is the Unicode Hex value for the 'Square' operation) to button. Finally assigns functionality to button through 'command=self.clear' i.e., WHEN [_ButtonCommand(command) IS PRESSED, assign 'self.clear' function. 
        button.grid(row=0, column=2, sticky=tk.NSEW) # Configure "Clear" button position, 'sticky=tk.NSEW' (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell". 
    
    def create_sqrt_button(self): # Method to create 'Square Root' Button
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=ivory3, fg=labels_color, font=default_font_type, borderwidth=3, relief= "raised", padx=5, pady=10, command=self.sqrt) # Uses Tk Button Class (Widget) to assign configuration -->>
        #('x\u00b2' is the Unicode Hex value for the 'Square Root' operation) to button. Finally assigns functionality to button through 'command=self.clear' i.e., WHEN [_ButtonCommand(command) IS PRESSED, assign 'self.clear' function. 
        button.grid(row=0, column=3, sticky=tk.NSEW) # Configure "Clear" button position, 'sticky=tk.NSEW' (North, South, East and West) so buttons functionality "sticks to every side and fills up the entire cell". 

#*********************************Define Operations****************************************            
    def bind_keys(self): # Method for allowing Keyboard Functionality
        self.window.bind("<Return>", lambda event: self.evaluate())  # For key in self.add_to_op, bind (pass) the key (digit), return as string.
        for key in self.digits: # Loop through 'in scope' keys
            self.window.bind(str(key), lambda event, digit=key: self.add_to_op(digit)) # For key in self.add_to_op, bind (pass) the key (digit), return as string.
            
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator)) # For key in self.operations, bind (pass) the value (operator)
            
                   
    def append_operator(self, operator): # Method to append variables.
        self.current_op += operator # Set the value of 'self.current_op' = 'self.current_op' + 'operator'.
        self.total += self.current_op # Then set the value of 'self.total' = 'self.total' + 'self.current op). 
        self.current_op ="" # Now clean up by clearing the value of 'self.current_op' by setting it to an empty string
        self.update_total_label() # call the method to Update the value of 'total_label'.
        self.update_label() # call the method to Update the value of 'label'.
    
    def add_to_op(self, value):
        self.current_op +=str(value)
        self.update_label()
    
    def clear(self): # Clear Method 
        self.current_op ="" # Clear self.current_op.
        self.total ="" # Clear self.total.
        self.update_label() # Call Method to update label.
        self.update_total_label() # Call Method to update total_label.

    def square(self): # Square Method
        self.current_op = str(eval(f"{self.current_op}**2")) # Sets self.current_op = the evaluation of 'self.current_op to the Second Power (**2) returning it as a string.
        self.update_label() # Call Method to update label.

    def sqrt(self): #Square root Method
        self.current_op = str(eval(f"{self.current_op}**0.5")) # Sets self.current_op = the evaluation of taking the Square Root (**0.5) of 'self.current_op' returning it as a string.
        self.update_label()
        
    def evaluate(self): # Method to conduct evaluation (the eval function evaluates and returns the value of a python expression).
        self.total += self.current_op # Make self.total = self.total + self.current_op.
        self.update_total_label() # Call Method to update total_label.

        try: #Try loop to handle exceptions like 'Divide by Zero Error' without erroring out of the program.
            self.current_op = str(eval(self.total)) # Self.current_op is equal to the evaluated string value of self.total.
            self.total = "" # Set self.total to an empty string
        except Exception as _: # If exception occurs
            self.current_op = "Error" # Set the value of self.current_op to 'Error'.
        finally: # Then
            self.update_label() # Update Label
        
        self.total = "" # Clears value of 'self.total' by setting it to an empty string.
        self.update_label() # Call Method to update label.
        
           
    def update_total_label(self): # Method to update the text display of the defined object.
        expression = self.total # create a new variable to use with replacements below.
        for operator, symbol in self.operations.items(): # Loop through replacement.
            expression = expression.replace(operator, f' {symbol} ') # Replaces  'operator' with its symbol. Adds the display of the current operator symbol to the operation display.
        self.total_label.config(text=expression) # Update the text display of the defined object by setting the text value to the current value of 'expression'.
 
    def update_label(self): # Method to update the text display of the defined object.
        self.label.config(text=self.current_op[:11]) # Update the text display of the defined object by setting the text value to the current value of 'self.current_op' -->>
        # and limiting (truncating) the output length by '[:11]'.
                
        
    def run(self):
        self.window.mainloop() # Start Calculator App.
        
        
if  __name__ == "__main__": # dunder to the races.
    calc = Calculator() # Assign 'calc' = to "Calculator" Class.
    calc.run() # Run it.   