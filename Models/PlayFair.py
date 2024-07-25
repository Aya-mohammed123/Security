import math
import re  # to validate input
import subprocess
from tkinter import *
import tkinter as tk

def Generate_Table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def Playfair_Cipher_E():
    key = str(var1.get())
    table = Generate_Table(key)
    input1 = list(var2.get())
    for char in range(len(input1)):
        if (input1[char] == 'j') or (input1[char] == 'J'):
            input1[char] = 'i'
    input1 = ''.join(input1).upper()
    input1 = list(input1)
    
    output1 = ''
    x = 0
    while x < len(input1)-1:
        if input1[x] == input1[x+1]:
            input1.insert(x+1, 'X')
        x = x+2

    if len(input1) % 2 == 1:
        input1.append('X')

    l2 = []
    x = 0
    while x < len(input1):
        index1 = table.index(input1[x])
        index2 = table.index(input1[x+1])

        if abs(index1 - index2) == abs(index1 % 5 - index2 % 5):
            if index1 % 5 == 4:
                l2.append(table[index1 - 4])
            else:
                l2.append(table[index1 + 1])
            if index2 % 5 == 4:
                l2.append(table[index2 - 4])
            else:
                l2.append(table[index2 + 1])

        elif index1 % 5 == index2 % 5:
            if index1 + 5 > 24:
                l2.append(table[index1 % 5])
            else:
                l2.append(table[index1 + 5])
            if index2 + 5 > 24:
                l2.append(table[index2 % 5])
            else:
                l2.append(table[index2 + 5])
        else:
            if index2 % 5 > index1 % 5:
                shift = index2 % 5 - index1 % 5
                l2.append(table[index1 + shift])
                l2.append(table[index2 - shift])
            else:
                shift = index1 % 5 - index2 % 5
                l2.append(table[index1 - shift])
                l2.append(table[index2 + shift])
        x = x+2
    output1 = ''.join(l2)
    var3.set(output1)


def Playfair_Cipher_D():
    key = str(var1.get())
    table = Generate_Table(key)
    input1 = list(var3.get())
    output = []
    x = 0
    
    while x < len(input1):
        index1 = table.index(input1[x])
        index2 = table.index(input1[x+1])

        if abs(index1 - index2) == abs(index1 % 5 - index2 % 5):
            if index1 % 5 == 0:
                output.append(table[index1 + 4])
            else:
                output.append(table[index1 - 1])
            if index2 % 5 == 0:
                output.append(table[index2 + 4])
            else:
                output.append(table[index2 - 1])

        elif index1 % 5 == index2 % 5:
            if index1 - 5 < 0:
                output.append(table[index1 + 20])
            else:
                output.append(table[index1 - 5])
            if index2 - 5 < 0:
                output.append(table[index2 + 20])
            else:
                output.append(table[index2 - 5])

        else:
            if index2 % 5 > index1 % 5:
                shift = index2 % 5 - index1 % 5
                output.append(table[index1 + shift])
                output.append(table[index2 - shift])
            else:
                shift = index1 % 5 - index2 % 5
                output.append(table[index1 - shift])
                output.append(table[index2 + shift])
        x = x+2
    output = ''.join(output)
    var2.set(output)

def Back():
    window.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"]) 
    
    
window = Tk()
window.geometry('320x450+250+250')  
window.title('Playfair Cipher')    
window.geometry('600x500')
window.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(window, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


labelplay = Label(window, text="Hello in PlayFair Cipher:", bg='#000522', fg='white',font=('arabic typesetting', 26))
labelplay.place(x=20, y=60)


var1 = StringVar()  
Label(text=" Key:", fg='white',bg='#000522',font=('arabic typesetting', 16)).place(x=50, y=150)
Entry(window, textvariable=var1).place(x=120, y=150,width=140, height=30)


var2 = StringVar()  
Label(text="Plain Text:", fg='white',bg='#000522',font=('arabic typesetting', 16)).place(x=50, y=210)
Entry(window,  width=50, textvariable=var2).place(x=160, y=210,width=140, height=30)


Button(text="Encyrption", bg='#000522',fg='white', command=Playfair_Cipher_E).place(x=120, y=350,height=50,width=150)

var3 = StringVar()

Label(text="Cipher Text:", fg='White',bg='#000522',font=('arabic typesetting', 16)).place(x=50, y=270)
Button(text="Decyrption", bg='#000522',fg='white', command=Playfair_Cipher_D).place(x=330, y=350,height=50,width=150)
Entry(window,  width=50, textvariable=var3).place(x=170, y=270,width=140, height=30)

backButton = Button(window, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
backButton.place(x=0, y=450, height=50, width=150)

window.mainloop()