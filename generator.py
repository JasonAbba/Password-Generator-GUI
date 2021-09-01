from tkinter import *
from tkinter import messagebox
from functions import *

flag_cap = False 
flag_small = False
flag_num = False 
flag_sym = False

m = Tk()
m.geometry('600x300')
m.title('Password Generator')
m.configure(bg = '#FFDD28')
def isChecked():
    global flag_cap, flag_small, flag_num, flag_sym # changes in value are globally affected

    # all if(s) are resetting values of flags, where as else(s) are setting it to default value i.e false
    if capital_letters.get() == 1:
        flag_cap = True
    else: 
        flag_cap = False
    if small_letters.get() == 1:
        flag_small = True
    else: 
        flag_small = False
    if numbers.get() == 1:
        flag_num = True
    else: 
        flag_num = False
    if symbols.get() == 1:
        flag_sym = True
    else: 
        flag_sym = False

Label(m, text = 'Password Generator', font = 'comicsansms 14 bold', pady = 15, bg = '#FFDD28').grid(row = 0, column = 3)
label = Label(m, text = '', font = 'comicsansms 12', pady = 10, bg = '#FFDD28', fg = '#644EE9')
label.grid(row = 1, column = 3)
copybtn = Button(m, text = 'Copy to clipboard', font = 'comicsansms 10 italic', command = lambda: copytoclipboard(m), bg = '#FFDD28', fg = '#644EE9').grid(row = 1, column = 4)
Label(m, text = 'Length', font = 'comicsansms 9 bold', bg = '#FFDD28', fg = '#644EE9').grid(row = 6, column = 1)

capital_letters = IntVar()
small_letters = IntVar()
numbers = IntVar()
symbols = IntVar()
length = IntVar()

cap = Checkbutton(m, text = 'Capital Letters', font = 'comicsansms 9 bold', variable = capital_letters, onvalue=1, offvalue=0, command = isChecked, bg = '#FFDD28', fg = '#644EE9').grid(row = 2, column = 1)
small = Checkbutton(m, text = 'Small Letters', font = 'comicsansms 9 bold', variable = small_letters, onvalue=1, offvalue=0, command = isChecked, bg = '#FFDD28', fg = '#644EE9').grid(row = 3, column = 1)
num = Checkbutton(m, text = 'Numbers', font = 'comicsansms 9 bold', variable = numbers, onvalue=1, offvalue=0, command = isChecked, bg = '#FFDD28', fg = '#644EE9').grid(row = 4, column = 1)
sym = Checkbutton(m, text = 'Symbols', font = 'comicsansms 9 bold', variable = symbols, onvalue=1, offvalue=0, command = isChecked, bg = '#FFDD28', fg = '#644EE9').grid(row = 5, column = 1)
scale = Scale(m, variable = length, from_ = 4, to = 16, orient = HORIZONTAL, font = 'comicsansms 9 bold', bg = '#FFDD28', fg = '#644EE9').grid(row = 6, column = 2)

Button(m, text = 'Generate', font = 'comicsanms 12 bold', command = lambda: run_two_functions(label, length, flag_cap, flag_small, flag_num, flag_sym), bg = '#FFDD28', fg = '#644EE9').grid(row = 7, column = 3)
m.mainloop()