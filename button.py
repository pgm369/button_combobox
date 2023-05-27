#Import class library 
import tkinter as tk

#Define a function to implement print function
def button_click():
    print("Button clicked!")

#Create root window object
root = tk.Tk()
root.title("Button Example")

#Create button object,put button in root window
#Set function for button to click 
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#Keep a root window open, call root object
root.mainloop()