from tkinter import *
from tkinter import messagebox
import re
import subprocess
import tkinter as tk

selected_numbers = []

def choice():
    selected_numbers.clear()
    for i in range(26):
        if checkboxes[i].get() == 1:
            selected_numbers.append(i)

    if len(selected_numbers) < 2 and doneClicked:
        messagebox.showerror("Error", "Please select at least two keys.")
    else:
        labelKey.config(text='Your choice: ' + ', '.join(str(num) for num in selected_numbers))
        labelKey.grid()

def toggle_checkbox(index):
    if checkboxes[index].get() == 1:
        if index in selected_numbers:
            repeat_or_remove(index)
        else:
            selected_numbers.append(index)
    else:
        selected_numbers.remove(index)

    choice()

def repeat_or_remove(index):
    response = messagebox.askquestion("Repeat or Remove", "Do you want to repeat or remove the selection?")
    if response == 'yes':
        # Repeat selection
        selected_numbers.append(index)
    else:
        # Remove selection
        checkboxes[index].set(0)
        selected_numbers.remove(index)

def done_clicked():
    global doneClicked
    doneClicked = True
    choice()
    if len(selected_numbers) < 2:
        if not doneClicked:
            messagebox.showerror("Error", "Please select at least two keys.")
    else:
        apply_polyalphabetic_window()

def clear_window():
    windowstream.destroy()
    create_window()

def create_window():
    global windowstream
    windowstream = Tk()
    windowstream.title("Choose keys for polyalphabetic")
    windowstream.geometry('900x500')
    windowstream.config(bg='#000522')

    global doneClicked
    doneClicked = False

    global labelStream, labelKey, doneButton, checkboxes
    labelStream = Label(windowstream, text="Choose all keys you need to apply:", bg='#000522', fg='white', font=('arabic typesetting', 26))
    labelStream.grid(row=0, column=0, columnspan=4, pady=10)

    checkboxes = []
    for i in range(26):
        checkbox_var = IntVar()
        checkbox = Checkbutton(windowstream, text=str(i), variable=checkbox_var, bg='#000522', fg='white', font=('arabic typesetting', 20), command=lambda i=i: toggle_checkbox(i))
        checkbox.grid(row=(i // 7) + 1, column=i % 7, padx=20, pady=5, sticky=W)
        checkboxes.append(checkbox_var)

    global labelKey
    labelKey = Label(windowstream, text='', relief='groove', bg='#000522',fg='white')
    labelKey.place(height=40, width=450, x=10, y=430)

    doneButton = Button(windowstream, text='Done', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=done_clicked)
    doneButton.place(x=720, y=430, height=50, width=150)

    clearButton = Button(windowstream, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=back_to_main_window)
    clearButton.place(x=550, y=430, height=50, width=150)

def back_to_main_window():
    windowstream.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"])

def apply_polyalphabetic_window():
    windowPoly = Tk()
    windowPoly.title("Polyalphabetic")
    windowPoly.geometry('600x500')
    windowPoly.config(bg='#000522')


    labelMonoH = Label(windowPoly, text="Hello in polyalphabetic cipher:", bg='#000522', fg='white', font=('arabic typesetting', 26))
    labelMonoH.place(x=20, y=60)

    labelMono = Label(windowPoly, text='From:', bg='#000522', fg='white', font=('arabic typesetting', 20))
    labelMono.place(x=50, y=220)

    TextBoxMono = Entry(windowPoly, font=('arabic typesetting', 16))
    TextBoxMono.place(x=140, y=220, width=140)

    labelMonoConv = Label(windowPoly, text='Encrypt:', bg='#000522', fg='white', font=('arabic typesetting', 20))
    labelMonoConv.place(x=310, y=190)

    labelconvEncrypt = Label(windowPoly, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
    labelconvEncrypt.place(height=38, width=110, x=420, y=190)

    labelMonoConv = Label(windowPoly, text='Decrypt:', bg='#000522', fg='white', font=('arabic typesetting', 20))
    labelMonoConv.place(x=310, y=250)

    labelconvTDecrypt = Label(windowPoly, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
    labelconvTDecrypt.place(height=38, width=110, x=420, y=250)

    def polyalphabeticEncryption():
        plaintext = TextBoxMono.get().lower()
        if not plaintext:
            messagebox.showwarning("Empty Text", "Please enter some text to encrypt.")
            return

        if not re.match("^[a-zA-Z]+$", plaintext):
            messagebox.showerror("Invalid Input", "Please enter only English alphabetic characters.")
            return

        cipherText = ''
        key_len = len(selected_numbers)
        for i, ch in enumerate(plaintext):
            if ch.isalpha():
                noOfIndex = ord(ch) - ord('a')
                newLetter = chr((noOfIndex + selected_numbers[i % key_len]) % 26 + ord('a'))
                cipherText += newLetter
            else:
                cipherText += ch

        labelconvEncrypt.config(text=cipherText)
        labelconvTDecrypt.config(text="")

    def polyalphabeticDycryption():
        cipherText = TextBoxMono.get().lower()
        if not cipherText:
            messagebox.showwarning("Empty Text", "Please enter some text to decrypt.")
            return

        if not re.match("^[a-zA-Z]+$", cipherText):
            messagebox.showerror("Invalid Input", "Please enter only English alphabetic characters.")
            return

        plaintext = ''
        key_len = len(selected_numbers)
        for i, ch in enumerate(cipherText):
            if ch.isalpha():
                noOfIndex = ord(ch) - ord('a')
                newLetter = chr((noOfIndex - selected_numbers[i % key_len]) % 26 + ord('a'))
                plaintext += newLetter
            else:
                plaintext += ch

        labelconvTDecrypt.config(text=plaintext)
        labelconvEncrypt.config(text="")

    encryptButton = Button(windowPoly, text='Encryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=polyalphabeticEncryption)
    encryptButton.place(x=100, y=350, height=50, width=150)

    decryptButton = Button(windowPoly, text='Decryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=polyalphabeticDycryption)
    decryptButton.place(x=310, y=350, height=50, width=150)

    backButton = Button(windowPoly, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18),command=windowPoly.destroy)
    backButton.place(x=0, y=450, height=50, width=150)

create_window()
windowstream.mainloop()
