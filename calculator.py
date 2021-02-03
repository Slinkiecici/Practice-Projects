#!/usr/bin/python3

from tkinter import *
import tkinter as tk# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tk.Tk()
numberslist = [[1,2,3],[4,5,6],[7,8,9],[0,'*', '/']]

for numbers in numberslist:
    index = numberslist.index(numbers)
    if index == 0:
        rows = 1
    elif index == 1:
        rows = 2
    elif index == 2:
        rows = 3
    elif index == 3:
        row = 4
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


    
top.mainloop()