import random
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Tarot Programm")
# Set geometry (widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Pick a card")
lbl.grid()

tarot = ["The Fool","The Magician","The High Priestess","The Empress","The Emperor","The Hierophant"]
def pick_card(cards):
    chosen_card = random.choice(cards)
    return chosen_card

# function to display text when
# button is clicked
def clicked():
    chosen_card = random.choice(tarot)
    lbl.configure(text = chosen_card)
    
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)



    
    


# all widgets will be here
# Execute Tkinter
root.mainloop()

