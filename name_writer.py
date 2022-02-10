from tkinter import *
from functools import partial

#########################################################################
#                                                                       #
#              			Name Writer - Hanyi Liu				            #
#              			last revised: 2/10/22                           #
#                                                                       #
#   Returns your name displayed in a "LASTNAME, FIRSTNAME" format.	    #
#########################################################################



ENTRY_SIZE = (100, 25)


#CREATE INPUT LABELS

firstLabel = Label(text="First Name:")
firstLabel.grid(row=0, column=0)

firstLabel = Label(text="Last Name:")
firstLabel.grid(row=0, column=1)




#CREATES INPUT
firstName = Entry(relief=GROOVE)
lastName = Entry(relief=GROOVE)

firstName.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5, ipadx=ENTRY_SIZE[0], ipady=ENTRY_SIZE[1])
lastName.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5, ipadx=ENTRY_SIZE[0], ipady=ENTRY_SIZE[1])

firstName.insert(END, '')
lastName.insert(END, '')

firstName.config(width=2)
lastName.config(width=2)


#CREATE LABEL
name = StringVar()
displayName = Label(textvariable=name)
displayName.grid(row=2, column=0, padx=5, pady=5, ipadx=ENTRY_SIZE[0], ipady=ENTRY_SIZE[1], columnspan=2)

def write():
    print("Writing name...")

    first = firstName.get()
    last = lastName.get()

    if(first == "" or last == ""):
        name.set("Enter your name first.")
    else:
        name.set(last + ", " + first)



#CREATE BUTTON
writeName = Button(command=partial(write))
writeName.config(text="Write Name")
writeName.grid(row=3, column=0, padx=5, pady=5, ipadx=10, ipady=10, columnspan=2)


mainloop()
