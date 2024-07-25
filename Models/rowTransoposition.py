from tkinter import *
from tkinter import messagebox
import math
import subprocess
import tkinter as tk

def RowTranspositionCipherEncryption():
    msg = Text_entry.get()
    key = Key_entry.get()

    cipher = ""
    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))  # sort key
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = row * col - msg_len
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for i in range(col):
        curr_idx = key.index(key_lst[i])
        cipher += ''.join([row[curr_idx] for row in matrix])

    labelconvEncrypt.config(text=cipher.upper())
    labelconvTDecrypt.config(text="")

def RowTranspositionCipherDycryption():
    key = Key_entry.get()
    ciphertext = Text_entry.get()
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = len(ciphertext)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []

    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = ciphertext[msg_indx]
            msg_indx += 1
        k_indx += 1

    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        msg = msg[:-null_count]

    labelconvTDecrypt.config(text=msg.upper())
    labelconvEncrypt.config(text="")


def Back():
    RowTranspositionCipher.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"])

RowTranspositionCipher = Tk()
RowTranspositionCipher.title("Row Transposition Cipher")
RowTranspositionCipher.geometry('600x500')
RowTranspositionCipher.config(bg='#000522')


background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(RowTranspositionCipher, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelceaser = Label(RowTranspositionCipher, text="Hello in Row Transposition Cipher:", bg='#000522', fg='white',
                    font=('arabic typesetting', 26))
labelceaser.place(x=20, y=60)

Key = Label(RowTranspositionCipher, text='Key:', bg='#000522', fg='white', font=('arabic typesetting', 20))
Key.place(x=30, y=190)

Key_entry = Entry(RowTranspositionCipher, font=('arabic typesetting', 16))
Key_entry.place(x=100, y=200, width=140)

Text_lbl = Label(RowTranspositionCipher, text='Text: ', bg='#000522', fg='white', font=('arabic typesetting', 20))
Text_lbl.place(x=30, y=250)

Text_entry = Entry(RowTranspositionCipher, font=('arabic typesetting', 16))
Text_entry.place(x=100, y=260, width=140)

Encrypt_lbl = Label(RowTranspositionCipher, text='Encrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
Encrypt_lbl.place(x=250, y=190)

labelconvEncrypt = Label(RowTranspositionCipher, text='', relief='groove', bg='White',
                         font=('arabic typesetting', 16))
labelconvEncrypt.place(height=38, width=220, x=360, y=190)

Decrypt_lbl = Label(RowTranspositionCipher, text='Decrypt:', bg='#083367', fg='white',
                    font=('arabic typesetting', 20))
Decrypt_lbl.place(x=250, y=250)

labelconvTDecrypt = Label(RowTranspositionCipher, text='', relief='groove', bg='White',
                          font=('arabic typesetting', 16))
labelconvTDecrypt.place(height=38, width=220, x=360, y=250)

encryptButton = Button(RowTranspositionCipher, text='Encryption', bg='#000522', bd=5, fg='white',
                       font=('arabic typesetting', 18), command=RowTranspositionCipherEncryption)
encryptButton.place(x=120, y=350, height=50, width=150)

decryptButton = Button(RowTranspositionCipher, text='Decryption', bg='#000522', bd=5, fg='white',
                       font=('arabic typesetting', 18), command=RowTranspositionCipherDycryption)
decryptButton.place(x=330, y=350, height=50, width=150)

backButton = Button(RowTranspositionCipher, text='Back', bg='#000522', bd=5, fg='white',
                    font=('arabic typesetting', 18), command=Back)
backButton.place(x=0, y=450, height=50, width=150)

RowTranspositionCipher.mainloop()