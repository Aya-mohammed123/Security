from Crypto.Cipher import DES
from tkinter import *
from tkinter import messagebox
import subprocess

def pad(text):
    # Pad the text to a multiple of 8 bytes (64 bits)
    while len(text) % 8 != 0:
        text += b'\x00'
    return text
# 
def DES_Encryption():
    plaintext = TextBoxDES.get().encode()
    key = TextBoxKey.get().encode()

    # Validate the length of the key
    if len(key) != 8:
        messagebox.showerror("Invalid Key", "Key length must be 8 bytes.")
        return

    # Initialize the DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    labelConvEncrypt.config(text=ciphertext.hex())

def DES_Decryption():
    ciphertext = bytes.fromhex(labelConvEncrypt.cget("text"))
    key = TextBoxKey.get().encode()

    if len(key) != 8:
        messagebox.showerror("Invalid Key", "Key length must be 8 bytes.")
        return

    # Initialize the DES cipher in ECB mode   plaintext is encrypted independently with the same key
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt
    decrypted_text = cipher.decrypt(ciphertext)
    labelConvDecrypt.config(text=decrypted_text.rstrip(b'\x00').decode('utf-8'))

def Back():
    windowDES.destroy()
    subprocess.run(["python", "Models\BlockCipher.py"]) 

windowDES = Tk()
windowDES.title("DES Encryption and Decryption")
windowDES.geometry('600x500')
windowDES.config(bg='#000522')  # Background color changed

# Set background image
background_image = PhotoImage(file="Assets\cyber2.png")
background_label = Label(windowDES, image=background_image)
background_label.place(relx=0.5, rely=0.5, anchor=CENTER)

labelDES = Label(windowDES, text="DES: ", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelDES.place(x=30, y=60)

labelKey = Label(windowDES, text='Enter Key :', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelKey.place(x=50, y=150)

TextBoxKey = Entry(windowDES, font=('arabic typesetting', 16))
TextBoxKey.place(x=170, y=150, width=200, height=35)

labelTextDES = Label(windowDES, text='Enter Text:', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelTextDES.place(x=50, y=200)

TextBoxDES = Entry(windowDES, font=('arabic typesetting', 16))
TextBoxDES.place(x=170, y=200, width=200, height=35)

labelEncryptDES = Label(windowDES, text='Encrypt: ', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelEncryptDES.place(x=50, y=250)

labelConvEncrypt = Label(windowDES, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelConvEncrypt.place(height=38, width=200, x=170, y=250)

labelDecryptDES = Label(windowDES, text='Decrypt:', bg='#000522', fg='white', font=('arabic typesetting', 16))
labelDecryptDES.place(x=50, y=300)

labelConvDecrypt = Label(windowDES, text='', relief='groove', bg='White', font=('arabic typesetting', 16))
labelConvDecrypt.place(height=38, width=200, x=170, y=300)

encryptButtonDES = Button(windowDES, text='Encrypt', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=DES_Encryption)
encryptButtonDES.place(x=210, y=350, height=50, width=150)

decryptButtonDES = Button(windowDES, text='Decrypt', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=DES_Decryption)
decryptButtonDES.place(x=400, y=350, height=50, width=150)

backButtonDES = Button(windowDES, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
backButtonDES.place(x=0, y=450, height=50, width=100)

windowDES.mainloop()
