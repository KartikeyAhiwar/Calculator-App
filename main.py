# Import necessary classes from the tkinter module
from tkinter import Tk, Button, Entry, StringVar

class Calculator:
    def __init__(self, master):
        # Set the title of the calculator window
        master.title("CALCULATOR")
        # Set the dimensions of the calculator window
        master.geometry("550x760+0+0")
        # Allow resizing of the calculator window
        master.resizable(True, True)
        # Set the background color of the calculator window
        master.config(bg='black')

        # Initialize a StringVar to hold the equation displayed on the calculator
        self.equation = StringVar()
        self.equation.set("")  # Set the initial value to an empty string
            
        # Create an Entry widget for displaying the equation
        Entry(master, width=21, bg="#cddfff",border= 2, relief="groove", 
              font=('Arial Bold', 35), textvariable=self.equation).place(x=0, y=5, height=77)
        
        # Create number buttons (1 to 9) with specified properties
        Button(master, text='1', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(1)).place(x=1, y=85)
        Button(master, text='2', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(2)).place(x=111, y=85)
        Button(master, text='3', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(3)).place(x=221.3, y=85)

        Button(master, text='4', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(4)).place(x=1, y=263)
        Button(master, text='5', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(5)).place(x=111, y=263)
        Button(master, text='6', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(6)).place(x=221, y=263)

        Button(master, text='7', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(7)).place(x=1, y=440)
        Button(master, text='8', width=14, height=11, bg="#B0C4DE", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(8)).place(x=111, y=440)
        Button(master, text='9', width=14, height=11, bg="#B0C4DE", fg="black", 
               font=('Arial', 9, 'bold'), relief='flat', command=lambda: self.show(9)).place(x=221, y=440)

        # Create the button for 0 with different size and color
        Button(master, text='0', width=10, height=7, bg="#4682B4", fg="black", 
               relief='flat', font=('Arial', 11, 'bold'), command=lambda: self.show(0)).place(x=115, y=617)

        # Create a clear button (C) to reset the input
        Button(master, text='C', width=11, height=7, bg="#FF6347", fg="white", 
               font=('Arial', 11, 'bold'), relief='flat', command=self.clear).place(x=1, y=617)
        # Create a backspace button (⌫) to delete the last input character
        Button(master, text='⌫', width=11, height=7, bg="#708090", fg="white", 
               relief='flat', font=('Arial', 11, 'bold'), command=self.delete).place(x=220, y=617)

        # Operation buttons (+, -, ×, ÷, %) with specified properties
        Button(master, text='+', width=14, height=11, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show('+')).place(x=331, y=85)
        Button(master, text='-', width=11, height=9, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 11, 'bold'), command=lambda: self.show('-')).place(x=331, y=263)
        Button(master, text='×', width=11, height=9, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 11, 'bold'), command=lambda: self.show('*')).place(x=331, y=440)
        Button(master, text='÷', width=11, height=7, bg="#cddfff", fg="black", 
               relief='flat', font=('Arial', 11, 'bold'), command=lambda: self.show('/')).place(x=331, y=617)
        Button(master, text='%', width=14, height=11, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show('%')).place(x=442, y=440)

        # Create buttons for decimal point (.) and square (x²)
        Button(master, text='.', width=14, height=11, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show('.')).place(x=442, y=263)
        Button(master, text='x²', width=14, height=11, bg="#7FFFD4", fg="black", 
               relief='flat', font=('Arial', 9, 'bold'), command=self.square).place(x=441.3, y=85)

        # Create the equals button (=) to evaluate the expression
        Button(master, text='=', width=12, height=8, bg="#00A4EF", fg="white", 
               relief='flat', font=('Arial', 10, 'bold'), command=self.solve).place(x=442, y=617)

    def show(self, value):
        # Get the current value displayed in the equation
        current_value = self.equation.get()
        # Convert the button value to a string
        self.entry_value = str(value)
        # Append the new value to the current equation and update the display
        self.equation.set(current_value + str(value))
    
    def clear(self):
        # Clear the entry value and reset the displayed equation
        self.entry_value = ''
        self.equation.set("")
    
    def solve(self):
        # Attempt to evaluate the mathematical expression
        try:
            result = eval(self.equation.get())  # Evaluate the expression
            self.equation.set(result)  # Display the result
        except:
            # If there is an error, display "Error"
            self.equation.set("Error")

    def delete(self):
        # Get the current text in the equation
        current_text = self.equation.get()
        # Remove the last character from the equation
        self.equation.set(current_text[:-1])
       
    def square(self):
        # Attempt to square the current input
        try:
            current_value = float(self.equation.get())  # Get the current input as a float
            squared_value = current_value ** 2           # Square the value
            self.equation.set(str(squared_value))        # Set the result back to the screen
        except ValueError:
            # Handle invalid input by displaying "Error"
            self.equation.set("Error")

# Create the main window
root = Tk()
# Instantiate the Calculator class
Calculator = Calculator(root)
# Start the Tkinter event loop
root.mainloop()
