#!/usr/bin/python3

from tkinter import *
import tkinter as tk# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tk.Tk()
buttons_frame = Frame(top)
buttons_frame.grid(row=0, column=0, sticky=W+E)
#The below code is an attempt at creating buttons in loop to shorten code, however currently it is not shorter than just declarng variables indivudally.
equation = StringVar() 
expression_field = Entry(buttons_frame, textvariable=equation) 
expression_field.grid(row = 6, columnspan=5)


button_one = tk.Button(buttons_frame, text= "1")
button_one.grid(row = 1, column = 1, sticky=N+S+E+W)
button_two = tk.Button(buttons_frame, text= "2")
button_two.grid(row = 1, column = 2, sticky=N+S+E+W)
button_three = tk.Button(buttons_frame, text= "3")
button_three.grid(row = 1, column = 3, sticky=N+S+E+W)
button_four = tk.Button(buttons_frame, text= "4")
button_four.grid(row = 2, column = 1, sticky=N+S+E+W)
button_five = tk.Button(buttons_frame, text= "5")
button_five.grid(row = 2, column = 2, sticky=N+S+E+W)
button_six = tk.Button(buttons_frame, text= "6")
button_six.grid(row = 2, column = 3, sticky=N+S+E+W)
button_seven = tk.Button(buttons_frame, text= "7")
button_seven.grid(row = 3, column = 1, sticky=N+S+E+W)
button_eight = tk.Button(buttons_frame, text= "8")
button_eight.grid(row = 3, column = 2, sticky=N+S+E+W)
button_nine = tk.Button(buttons_frame, text= "9")
button_nine.grid(row = 3, column = 3, sticky=N+S+E+W)
button_zero = tk.Button(buttons_frame, text= "0")
button_zero.grid(row = 4, column = 2, sticky=N+S+E+W)

button_plus = tk.Button(buttons_frame, text = "+")
button_plus.grid(row = 1, column = 4, sticky=N+S+E+W)
button_minus = tk.Button(buttons_frame, text = "-")
button_minus.grid(row = 2, column = 4, sticky=N+S+E+W)
button_multiply = tk.Button(buttons_frame, text = "*")
button_multiply.grid(row = 3, column = 4, sticky=N+S+E+W)
button_divide = tk.Button(buttons_frame, text = "/")
button_divide.grid(row = 4, column = 4, sticky=N+S+E+W)
button_equal = tk.Button(buttons_frame, text = "ENTER")
button_equal.grid(row = 5, columnspan= 5, sticky=N+S+E+W)
"""numberslist = [[1,2,3],[4,5,6],[7,8,9],[0,'*', '/'], ["+", "-", "ENTER"]]
for numbers in numberslist:
    index = numberslist.index(numbers)
    if index == 0:
        rows = 1
    elif index == 1:
        rows = 2
    elif index == 2:
        rows = 3
    elif index == 3:
        rows = 4
    else: rows = 5
    for number in numbers:
        if number in numbers:
            col_index = numbers.index(number)
            print (col_index)
            if col_index == 0:
                columns = 1
            elif col_index == 1:
                columns = 2
            if col_index == 2:
                columns = 3
            button = tk.Button(
            text=str(number),
            fg="blue",
            bg="yellow",
            )
            button.grid(row = rows,column = columns)
        else: continue
"""

top.resizable(True, True)
top.mainloop()