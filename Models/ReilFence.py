from tkinter import *
from tkinter import messagebox
import subprocess
import tkinter as tk

def encrypt_rail_fence(text):
    text = text.replace(" ", "").lower()
    rail1, rail2 = "", ""

    for i, char in enumerate(text):
        if i % 2 == 0:
            rail1 += char
        else:
            rail2 += char

    return rail1 + rail2

def decrypt_rail_fence(cipher):
    half_length = len(cipher) // 2
    rail1, rail2 = cipher[:half_length], cipher[half_length:]
    plaintext = ""

    for i in range(half_length):
        plaintext += rail1[i] + rail2[i]

    if len(cipher) % 2 != 0:
        plaintext += rail2[-1]

    return plaintext

def RailFenceEncryption():
    plaintext = TextBoxRail.get()
    if not plaintext:
        messagebox.showwarning("Empty Text", "Please enter some text to encrypt.")
        return
    
    ciphertext = encrypt_rail_fence(plaintext)
    labelconvEncryptRail.config(text=ciphertext)
    labelconvDecryptRail.config(text="")

def RailFenceDecryption():
    cipher_text = TextBoxRail.get()
    if not cipher_text:
        messagebox.showwarning("Empty Text", "Please enter some text to decrypt.")
        return
    
    decrypted_text = decrypt_rail_fence(cipher_text)
    labelconvDecryptRail.config(text=decrypted_text)
    labelconvEncryptRail.config(text="")

def Back():
    windowrail.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"])

windowrail = Tk()
windowrail.title("Rail Fence Cipher")
windowrail.geometry('600x500')
windowrail.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(windowrail, image=background_image, highlightthickness=0)
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelMonoH = Label(windowrail, text="Hello in rail fence cipher:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelMonoH.place(x=20, y=80)

labelRail = Label(windowrail, text='Text:', bg='#000522', fg='white', font=('arabic typesetting', 20))
labelRail.place(x=50, y=200)

TextBoxRail = Entry(windowrail, font=('arabic typesetting', 16))
TextBoxRail.place(x=140, y=200, width=140)

encryptButtonRail = Button(windowrail, text='Encryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=RailFenceEncryption)
encryptButtonRail.place(x=120, y=350, height=50, width=150)

decryptButtonRail = Button(windowrail, text='Decryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=RailFenceDecryption)
decryptButtonRail.place(x=330, y=350, height=50, width=150)

labelConvRailEncrypt = Label(windowrail, text='Encrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
labelConvRailEncrypt.place(x=310, y=190)

labelconvEncryptRail = Label(windowrail, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvEncryptRail.place(height=38, width=110, x=420, y=190)

labelConvRailDecrypt = Label(windowrail, text='Decrypt:', bg='#083367', fg='white', font=('arabic typesetting', 20))
labelConvRailDecrypt.place(x=310, y=250)

labelconvDecryptRail = Label(windowrail, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelconvDecryptRail.place(height=38, width=110, x=420, y=250)

backButtonRail = Button(windowrail, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
backButtonRail.place(x=0, y=450, height=50, width=150)

windowrail.mainloop()
