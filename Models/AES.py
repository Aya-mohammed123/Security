from Crypto.Cipher import AES
from tkinter import *
from tkinter import messagebox
import subprocess
from Crypto.Cipher import DES
import tkinter as tk

def pad(text):
    # Pad the text to a multiple of the block size (16 bytes for AES)
    block_size = 16
    padding = block_size - len(text) % block_size
    return text + bytes([padding] * padding)

def unpad(text):
    # Remove padding characters (including null bytes) from the decrypted text
    padding_length = text[-1]
    return text[:-padding_length]

def AES_Encryption():
    plaintext = TextBoxAES.get().encode()
    key = TextBoxAESKey.get().encode()

    # Check if both key and plaintext are provided
    if not plaintext or not key:
        messagebox.showerror("Missing Input", "Please enter both text and key.")
        return

    # Validate the length of the key
    if len(key) not in [16, 24, 32]:
        messagebox.showerror("Invalid Key", "Key length must be 16, 24, or 32 bytes.")
        return

    # Initialize the AES cipher in ECB mode  plaintext is encrypted independently with the same key
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    labelConvEncryptAES.config(text=ciphertext.hex())

def AES_Decryption():
    ciphertext = bytes.fromhex(labelConvEncryptAES.cget("text"))
    key = TextBoxAESKey.get().encode()

    # Check if both key and ciphertext are provided
    if not ciphertext or not key:
        messagebox.showerror("Missing Input", "Please enter both ciphertext and key.")
        return

    # Validate the length of the key
    if len(key) not in [16, 24, 32]:
        messagebox.showerror("Invalid Key", "Key length must be 16, 24, or 32 bytes.")
        return

    # Initialize the AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text)
    labelConvDecryptAES.config(text=plaintext.decode('utf-8'))

def Back():
    windowAES.destroy()
    subprocess.run(["python", "Models\BlockCipher.py"]) 

windowAES = Tk()
windowAES.title("AES Encryption and Decryption")
windowAES.geometry('600x500')
windowAES.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(windowAES, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelAES = Label(windowAES, text="AES: ", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelAES.place(x=50, y=60)

labelKeyAES = Label(windowAES, text='Enter Key: ', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelKeyAES.place(x=50, y=150)

TextBoxAESKey = Entry(windowAES, font=('arabic typesetting', 16))
TextBoxAESKey.place(x=180, y=150, width=250,height=35)

labelTextAES = Label(windowAES, text='Enter Text:', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelTextAES.place(x=50, y=200)

TextBoxAES = Entry(windowAES, font=('arabic typesetting', 16))
TextBoxAES.place(x=180, y=200, width=250,height=35)

labelEncryptAES = Label(windowAES, text='Encypt: ', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelEncryptAES.place(x=50, y=250)

labelConvEncryptAES = Label(windowAES, text='', relief='solid', bg='White', font=('arabic typesetting', 16))
labelConvEncryptAES.place(height=38, width=250, x=180, y=250)

labelDecryptAES = Label(windowAES, text='Decrypt:', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelDecryptAES.place(x=50, y=300)

labelConvDecryptAES = Label(windowAES, text='', relief='solid', bg='White', font=('arabic typesetting', 16))
labelConvDecryptAES.place(height=38, width=250, x=180, y=300)

encryptButtonAES = Button(windowAES, text='Encrypt', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=AES_Encryption)
encryptButtonAES.place(x=220, y=350, height=50, width=150)

decryptButtonAES = Button(windowAES, text='Decrypt', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=AES_Decryption)
decryptButtonAES.place(x=420, y=350, height=50, width=150)

backButtonAES = Button(windowAES, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
backButtonAES.place(x=0, y=450, height=50, width=100)

windowAES.mainloop()
