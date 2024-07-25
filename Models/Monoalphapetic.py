from tkinter import *
from tkinter import messagebox
import random
import re  # to validate input
import subprocess
import tkinter as tk

# Shuffle the alphabet to generate a random key
key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
random.shuffle(key)
alphabit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def MonoalphabeticEncryption():
    plaintext = TextBoxMono.get().lower()
    if not plaintext:
        messagebox.showwarning("Empty Text", "Please enter some text to encrypt.")
        return
    
    if not re.match("^[a-zA-Z]+$", plaintext):
        messagebox.showerror("Invalid Input", "Please enter only English alphabetic characters.")
        return
    
    cipherText = ''
    for i in plaintext:
        if i in alphabit:
            noOfIndex = alphabit.index(i)
            newLetter = key[noOfIndex]
            cipherText += newLetter
        else:
            cipherText += i

    labelconvEncrypt.config(text=cipherText)
    labelconvTDecrypt.config(text="")

def MonoalphabeticDycryption():
    cipherText = TextBoxMono.get().lower()
    if not cipherText:
        messagebox.showwarning("Empty Text", "Please enter some text to decrypt.")
        return
    
    if not re.match("^[a-zA-Z]+$", cipherText):
        messagebox.showerror("Invalid Input", "Please enter only English alphabetic characters.")
        return
    
    plaintext = ''
    for i in cipherText:
        if i in key:
            noOfIndex = key.index(i)
            newLetter = alphabit[noOfIndex]
            plaintext += newLetter
        else:
            plaintext += i

    labelconvTDecrypt.config(text=plaintext)
    labelconvEncrypt.config(text="")

def Back():
    windowmono.destroy()
    subprocess.run(["python", "Models\\StreamCipher.py"]) 

windowmono = Tk()
windowmono.title("Monoalphabetic")
windowmono.geometry('600x500')
windowmono.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(windowmono, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelMonoH = Label(windowmono, text="Hello in monoalphabetic cipher:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelMonoH.place(x=20, y=60)

labelMono = Label(windowmono, text='From:', bg='#000522', fg='white', font=('arabic typesetting', 20))
labelMono.place(x=50, y=220)

TextBoxMono = Entry(windowmono, font=('arabic typesetting', 16))
TextBoxMono.place(x=140, y=220, width=140)

labelMonoConv = Label(windowmono, text='Encrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
labelMonoConv.place(x=310, y=190)

labelconvEncrypt = Label(windowmono, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvEncrypt.place(height=38, width=110, x=420, y=190)

labelMonoConv = Label(windowmono, text='Decrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
labelMonoConv.place(x=310, y=250)

labelconvTDecrypt = Label(windowmono, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvTDecrypt.place(height=38, width=110, x=420, y=250)

encryptButton = Button(windowmono, text='Encryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=MonoalphabeticEncryption)
encryptButton.place(x=120, y=350, height=50, width=150)

decryptButton = Button(windowmono, text='Decryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=MonoalphabeticDycryption)
decryptButton.place(x=330, y=350, height=50, width=150)

decryptButton = Button(windowmono, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
decryptButton.place(x=0, y=450, height=50, width=150)

windowmono.mainloop()
