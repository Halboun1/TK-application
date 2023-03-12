from tkinter import *
from tkinter import ttk
from toolTip import *

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def button_pressed():
    print("Button is pressed")

root = Tk()
root.title("Feet to Meters")
root.geometry('500x400')

# 1) Step one create the frame that will hold everything.
# 2) Create the widgets for everything.
#   2.1) Create an Entry widget.
#   2.2) Create a Label Widget.
#   2.3) Create a label widget that calculate the equation.
#   2.4) Create a Button that perform the calculation.
#   2.5) Create a Button that will Swap the equation.














img = PhotoImage(file='transfer.png').subsample(30)

# create a button
button = Button(root, text='Button',image=img,command=button_pressed)

# define the text for the tooltip
tooltip_text = 'Convert from Meters to Feet'

create_tooltip(button, tooltip_text)

button.pack()




mainframe = Frame(root,borderwidth=4,highlightcolor='red')           #padding from the frame to the entire window.
mainframe.pack()                                                                        #mainframe is the child of root



feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)       #creating an entry widget with a value of "feet" line 17
feet_entry.grid(row=0,column=0)                                    #important step in order to show the widget on the screen.

meters = StringVar()                                                
ttk.Label(mainframe, textvariable=meters).grid(row=0,column=2)     #creating a lable widget.
                                                                    #important step to show the widget on the screen.
                                                                    
                                                                    
ttk.Button(mainframe, text="Calculate", command=calculate).grid(row=1,column=1)

ttk.Label(mainframe, text="feet is equivalent to").grid(row=0,column=1)
ttk.Label(mainframe, text="meters").grid(row=0,column=3)

for child in mainframe.winfo_children():                            #creating a padding inside the parent window.
    child.grid_configure(padx=1, pady=1)                            #mainly for every widget inside the children

feet_entry.focus()
root.bind("<Return>",calculate)


root.mainloop()