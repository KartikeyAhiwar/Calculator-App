from tkinter import Tk, Button, Entry, StringVar

class Calculator:
    def __init__(self, master):
        
        master.title("CALCULATOR")
        master.geometry("550x760+0+0")
        master.resizable(True, True)
        master.config(bg='light blue')
        
        self.equation = StringVar()
        self.equation.set("")
            
 # Entry for the equation display
        Entry(master, width=40, bg="#cddfff",relief="groove", font=('Arial Bold', 35), textvariable=self.equation).place(x=0, y=5, height=75)
        
# Buttons - these should be created inside the __init__ method
        Button(master, text='1', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(1)).place(x=1, y=85)
        Button(master, text='2', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(2)).place(x=111, y=85)
        Button(master, text='3', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(3)).place(x=221, y=85)

        Button(master, text='4', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(4)).place(x=1, y=263)
        Button(master, text='5', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(5)).place(x=111, y=263)
        Button(master, text='6', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(6)).place(x=221, y=263)

        Button(master, text='7', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(7)).place(x=1, y=440)
        Button(master, text='8', width=14, height=11, bg="#B0C4DE", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show(8)).place(x=111, y=440)
        Button(master, text='9', width=14, height=11, bg="#B0C4DE", fg="black", font=('Arial', 9, 'bold'), relief='flat', command=lambda: self.show(9)).place(x=221, y=440)

        Button(master, text='0', width=10, height=7, bg="#4682B4", fg="black", relief='flat', font=('Arial', 11, 'bold'), command=lambda: self.show(0)).place(x=114, y=617)

        Button(master, text='C', width=11, height=7, bg="#FF6347", fg="white", font=('Arial', 11, 'bold'), relief='flat', command=self.clear).place(x=0, y=617)
        Button(master, text='⌫', width=11, height=7, bg="#708090", fg="white", relief='flat', font=('Arial', 11, 'bold'), command=self.delete).place(x=219, y=617)

# Operation buttons with bold text
        Button(master, text='+', width=14, height=11, bg="#7FFFD4", fg="black", relief='flat', font=('Arial', 9, 'bold'), command=lambda: self.show('+')).place(x=332, y=85)
        Button(master, text='-', width=11, height=9, bg="#7FFFD4", fg="black", relief='flat',font=('Arial', 11, 'bold'),command=lambda: self.show('-')).place(x=331, y=263)
        Button(master, text='×', width=11, height=9, bg="#7FFFD4", fg="black", relief='flat',font=('Arial', 11, 'bold'), command=lambda: self.show('*')).place(x=331, y=440)
        Button(master, text='÷', width=11, height=7, bg="#cddfff", fg="black", relief='flat',font=('Arial', 11, 'bold'), command=lambda: self.show('/')).place(x=331, y=617)
        Button(master, text='%', width=14, height=11, bg="#7FFFD4", fg="black", relief='flat',font=('Arial', 9, 'bold'), command=lambda: self.show('%')).place(x=442, y=440)
# Decimal and square buttons
        Button(master, text='.', width=14, height=11, bg="#7FFFD4", fg="black", relief='flat',font=('Arial', 9, 'bold'), command=lambda: self.show('.')).place(x=442, y=263)
        Button(master, text='x²', width=14, height=11, bg="#7FFFD4", fg="black", relief='flat',font=('Arial', 9, 'bold'), command=self.square).place(x=442, y=85)

# Create the backspace button
        Button(master, text='=', width=12, height=8, bg="#00A4EF", fg="white", relief='flat',font=('Arial', 10, 'bold'),command=self.solve).place(x=442, y=617)

    def show(self, value):
        # Get the current value displayed in the equation
        current_value = self.equation.get()

        # Allow only valid characters: digits, '+', '-', '*', '/', '%', and '.'
        if str(value) in '0123456789+-*/%.':
            # Append the new value to the current equation and update the display
            self.equation.set(current_value + str(value))
            
    def clear(self):
        self.entry_value = ''
        self.equation.set("")
    
    def solve(self):
        try:
            result = eval(self.equation.get())
            self.equation.set(result)
        except:
            self.equation.set("Error")
    # Define the delete method in your class
    def delete(self):
       current_text = self.equation.get()
    # Remove the last character
       self.equation.set(current_text[:-1])
       
    def square(self):
      try:
        current_value = float(self.equation.get())  # Get the current input
        squared_value = current_value ** 2           # Square the value
        self.equation.set(str(squared_value))        # Set the result back to the screen
      except ValueError:
        self.equation.set("Error")  # Handle invalid input

        
root = Tk()
Calculator = Calculator(root)
root.mainloop()

