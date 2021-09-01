from random import sample, randint
from tkinter import messagebox
password = ''
capital_letters_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
small_letters_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.lower().split(' ')
numbers_list = '0 1 2 3 4 5 6 7 8 9'.split(' ')
symbols_list = '! @ # $ % ^ & * ( ) _ - + = / ~ \ | { } [ ] ; : " " ' ' < > , . ?'.split(' ')

def generate(label, selected_length, flag_cap, flag_small, flag_num, flag_sym):
    temp_list = []
    if flag_cap == True:
        temp_list = temp_list + capital_letters_list
    if flag_small == True:
        temp_list = temp_list + small_letters_list
    if flag_num == True:
        temp_list = temp_list + numbers_list
    if flag_sym == True:
        temp_list = temp_list + symbols_list

    try:
        if flag_num == True and flag_cap == False and flag_small == False and flag_sym == False: # only number checkbox is checked
            if selected_length > 9:
                selected_length = 9
        randomized_list = sample(temp_list, len(temp_list)) # randomzing elements inside temp_list
        # print(randomized_list)
        global password
        password = ''.join(sample(randomized_list, selected_length))
        label.config(text = password)
    except Exception as e:
        messagebox.showwarning("Warning","Please check atleast one checkbox.")
    
def scalefunc(length):
    selected_length = length.get()
    return selected_length

def run_two_functions(label, length, flag_cap, flag_small, flag_num, flag_sym):
    selected_length = scalefunc(length)
    generate(label, selected_length, flag_cap, flag_small, flag_num, flag_sym)

def copytoclipboard(m):
    m.clipboard_clear()
    global password
    m.clipboard_append(password)