from tkinter import *
from tkinter import ttk
from toolTip import *


###############################
########## Functions ##########
###############################

# Name:                 calculate(*args)
# Description:          to convert from feet to meters.
def calculateMeters(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


# Name:                 calculateFeet(*args)
# Description:          to convert from Meters to Feet.
def calculateFeet(*args):
    try:
        value = float(meters.get())
        meters.set(int(value * 3.2804))
    except ValueError:
        pass

# Name:                 button_pressed()
# Description:          to check if the button is pressed.
def button_pressed(*args):
    print("Button is pressed")



###############################
########## MainFrame ##########
###############################
root = Tk()
root.title("Feet to Meters")
root.geometry('300x100')


img = PhotoImage(file='transfer.png').subsample(30)

while button_pressed:
    # 1) Step one create the frame that will hold everything.
    mainframe = Frame(root,borderwidth=4,highlightcolor='red')           #padding from the frame to the entire window.
    mainframe.pack()                                                     #mainframe is the child of root

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)       #creating an entry widget with a value of "feet" line 17
    feet_entry.grid(row=0,column=0)                                    #important step in order to show the widget on the screen.
    

    
    meters = StringVar()                                                
    ttk.Label(mainframe, textvariable=meters).grid(row=0,column=2)     
                                                                    
                                                   
    ttk.Button(mainframe, text="Calculate", command=calculateMeters).grid(row=1,column=1)

    ttk.Label(mainframe, text="feet is equivalent to").grid(row=0,column=1) 
    ttk.Label(mainframe, text="meters").grid(row=0,column=3)
    
    # create a button
    button = Button(root, text='Button',image=img,command=button_pressed)

    # define the text for the tooltip
    tooltip_text = 'Convert from Meters to Feet'

    create_tooltip(button, tooltip_text)

    button.pack()


    for child in mainframe.winfo_children():                            #creating a padding inside the parent window.
        child.grid_configure(padx=1, pady=1)                            #mainly for every widget inside the children

    feet_entry.focus()
    root.bind("<Return>",calculateMeters)
    root.mainloop()
    
else :
    # 1) Step one create the frame that will hold everything.
    mainframe = Frame(root,borderwidth=4,highlightcolor='red')           #padding from the frame to the entire window.
    mainframe.pack()                                                     #mainframe is the child of root
    
    meters = StringVar()                                                
    meters = ttk.Entry(mainframe,width=7, textvariable=meters)
    meters.grid(row=0,column=2)                                             

    
    feet = StringVar()
    feet_entry = ttk.Label(mainframe, width=7, textvariable=feet)       #creating an entry widget with a value of "feet" line 17
    feet_entry.grid(row=0,column=0)                                    #important step in order to show the widget on the screen.

    ttk.Button(mainframe, text="Calculate", command=calculateFeet).grid(row=1,column=1)
    
    ttk.Label(mainframe, text="meters is equivalent to").grid(row=0,column=1) 
    ttk.Label(mainframe, text="feet").grid(row=0,column=3)    
    
    # create a button
    button = Button(root, text='Button',image=img,command=button_pressed)    
    
    # define the text for the tooltip
    tooltip_text = 'Convert from Meters to Feet'

    create_tooltip(button, tooltip_text)
    button.pack()


    for child in mainframe.winfo_children():                            #creating a padding inside the parent window.
        child.grid_configure(padx=1, pady=1)                            #mainly for every widget inside the children

    meters.focus()
    root.bind("<Return>",calculateFeet)
    root.mainloop()
    
# 2) Create the widgets for everything.
#   2.1) Create an Entry widget.
#   2.2) Create a Label Widget.
#   2.3) Create a label widget that calculate the equation.
#   2.4) Create a Button that perform the calculation.
#   2.5) Create a Button that will Swap the equation.


    
    
    
    


