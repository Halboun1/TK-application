from tkinter import *
from tkinter import ttk
from toolTip import *

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")
root.geometry('500x400')



# create a button
button = Button(root, text='Button')

# define the text for the tooltip
tooltip_text = 'Hello'

create_tooltip(button, tooltip_text)

button.pack()


img = PhotoImage(file='transfer.png').subsample(30)

mainframe = Frame(root,borderwidth=4,highlightcolor='red')           #padding from the frame to the entire window.
mainframe.pack()                                                                        #mainframe is the child of root



feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)       #creating an entry widget with a value of "feet" line 17
feet_entry.grid(row=0,column=0)                                    #important step in order to show the widget on the screen.

meters = StringVar()                                                
ttk.Label(mainframe, textvariable=meters).grid(row=0,column=2)     #creating a lable widget.
                                                                    #important step to show the widget on the screen.
                                                                    
                                                                    
ttk.Button(mainframe, text="Calculate",image=img, command=calculate).grid(row=1,column=1)

ttk.Label(mainframe, text="feet is equivalent to").grid(row=0,column=1)
ttk.Label(mainframe, text="meters").grid(row=0,column=3)

for child in mainframe.winfo_children():                            #creating a padding inside the parent window.
    child.grid_configure(padx=1, pady=1)                            #mainly for every widget inside the children

feet_entry.focus()
root.bind("<Return>",calculate)


root.mainloop()