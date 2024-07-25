import math
import re  # to validate input
import subprocess
from tkinter import *
import tkinter as tk

def encrypt(plain_text, key):
    
    cipher_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - 97
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + key_shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + key_shift) % 26 + 97)
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    key_length = len(key)
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - 97
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - key_shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - key_shift) % 26 + 97)
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text

def encrypt_button_click():
    plain_text = plain_Text_entry.get()
    encryption_key = Key_entry.get()
    encrypted_text = encrypt(plain_text, encryption_key)
    cipher_Text_entry.delete(0, END)
    cipher_Text_entry.insert(0, encrypted_text)

def decrypt_button_click():
    cipher_text = cipher_Text_entry.get()
    decryption_key = Key_entry.get()
    decrypted_text = decrypt(cipher_text, decryption_key)
    plain_Text_entry.delete(0, END)
    plain_Text_entry.insert(0, decrypted_text)

def Back():
    VigenerCipher.destroy()
    subprocess.run(["python", "Models\StreamCipher.py"]) 
    
VigenerCipher = Tk()
VigenerCipher.title("Vigenere Cipher")
VigenerCipher.geometry('600x500')
VigenerCipher.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(VigenerCipher, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelVigenre = Label(VigenerCipher, text="Hello in Vigenere Cipher:", bg='#000522', fg='white',font=('arabic typesetting', 26))
labelVigenre.place(x=20, y=60)

Key = Label(VigenerCipher, text='Key:', bg='#000522', fg='white', font=('arabic typesetting', 20))
Key.place(x=50, y=150)

Key_entry = Entry(VigenerCipher, font=('arabic typesetting', 16))
Key_entry.place(x=140, y=150, width=140)

plain_Text_lbl = Label(VigenerCipher, text='Plain Text: ', bg='#000522', fg='white', font=('arabic typesetting', 20))
plain_Text_lbl.place(x=50, y=210)

plain_Text_entry = Entry(VigenerCipher, font=('arabic typesetting', 16))
plain_Text_entry.place(x=210, y=210, width=140)

cipher_Text_lbl = Label(VigenerCipher, text='Cipher Text: ', bg='#000522', fg='white', font=('arabic typesetting', 20))
cipher_Text_lbl.place(x=50, y=270)

cipher_Text_entry = Entry(VigenerCipher, font=('arabic typesetting', 16))
cipher_Text_entry.place(x=210, y=270, width=140)

encryptButton = Button(VigenerCipher, text='Encryption', bg='#000522', bd=5, fg='white',font=('arabic typesetting', 18), command=encrypt_button_click)
encryptButton.place(x=120, y=350, height=50, width=150)

decryptButton = Button(VigenerCipher, text='Decryption', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=decrypt_button_click)
decryptButton.place(x=330, y=350, height=50, width=150)

backButton = Button(VigenerCipher, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
backButton.place(x=0, y=450, height=50, width=150)

VigenerCipher.mainloop()