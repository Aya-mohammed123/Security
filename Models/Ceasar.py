from tkinter import *
from tkinter import messagebox
import subprocess
import tkinter as tk


def CeaserCipherEncryption():
    key = Key_entry.get()
    text = Text_entry.get()

    # Check if the key is numeric
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a numeric value")
        return

    key = int(key)  # Convert the key to an integer
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char

    # Display the encrypted text
    labelconvEncrypt.config(text=encrypted_text)
    labelconvTDecrypt.config(text="")


def CeaserCipherDycryption():
    key = Key_entry.get()
    ciphertext = Text_entry.get()

    # Check if the key is numeric
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a numeric value")
        return

    key = int(key)  # Convert the key to an integer
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    # Display the decrypted text
    labelconvTDecrypt.config(text=decrypted_text)
    labelconvEncrypt.config(text="")


def Back():
    CeaserScreen.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"])


CeaserScreen = Tk()
CeaserScreen.title("CeaserCipher")
CeaserScreen.geometry('600x500')
CeaserScreen.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(CeaserScreen, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelceaser = Label(CeaserScreen, text="Hello in Ceaser cipher:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelceaser.place(x=20, y=60)

Key = Label(CeaserScreen, text='Key:', bg='#000522', fg='white', font=('arabic typesetting', 20))
Key.place(x=50, y=200)

Key_entry = Entry(CeaserScreen, font=('arabic typesetting', 16))
Key_entry.place(x=140, y=200, width=140)

Text_lbl = Label(CeaserScreen, text='Text: ', bg='#000522', fg='white', font=('arabic typesetting', 20))
Text_lbl.place(x=50, y=260)

Text_entry = Entry(CeaserScreen, font=('arabic typesetting', 16))
Text_entry.place(x=140, y=260, width=140)

Encrypt_lbl = Label(CeaserScreen, text='Encrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
Encrypt_lbl.place(x=310, y=190)

labelconvEncrypt = Label(CeaserScreen, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvEncrypt.place(height=38, width=110, x=420, y=190)

Decrypt_lbl = Label(CeaserScreen, text='Decrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
Decrypt_lbl.place(x=310, y=250)

labelconvTDecrypt = Label(CeaserScreen, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvTDecrypt.place(height=38, width=110, x=420, y=250)

encryptButton = Button(CeaserScreen, text='Encryption', bg='#000522', bd=5, fg='white',
                       font=('arabic typesetting', 18), command=CeaserCipherEncryption)
encryptButton.place(x=120, y=350, height=50, width=150)

decryptButton = Button(CeaserScreen, text='Decryption', bg='#000522', bd=5, fg='white',
                       font=('arabic typesetting', 18), command=CeaserCipherDycryption)
decryptButton.place(x=330, y=350, height=50, width=150)

decryptButton = Button(CeaserScreen, text='Back', bg='#000522', bd=5, fg='white',
                       font=('arabic typesetting', 18), command=Back)
decryptButton.place(x=0, y=450, height=50, width=150)

CeaserScreen.mainloop()
