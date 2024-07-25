from tkinter import *
from tkinter import messagebox
import subprocess
import tkinter as tk
def choise():
    labelblock.config(text='your choise is '+blockChoise.get())

def Go():
    selectedValue = blockChoise.get()
    if selectedValue == 'DES':
        windowblock.destroy()
        import DES # allow to aceess to next 
        subprocess.run(["python", "Models\DES.py"])
    elif selectedValue == 'AES':
        windowblock.destroy()
        import AES
        subprocess.run(["python", "Models\AES.py"])
        
def Back():
    windowblock.destroy()
    subprocess.run(["python", "Models\CipherType.py"]) 
   
windowblock = Tk()
windowblock.title("Block Cipher")
windowblock.geometry('600x500')
windowblock.config(bg='#000522')


background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(windowblock, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelB =Label(windowblock, text="what type of block Cipher🫣:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelB.place(x=20, y=60)

blockChoise =StringVar()

Des =Radiobutton(windowblock, text='DES', variable=blockChoise, value='DES', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
Des.place(x=50, y=190)

aes =Radiobutton(windowblock, text='AES', variable=blockChoise, value='AES', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
aes.place(x=50, y=240)



labelblock =Label(windowblock, text='', relief='groove', bg='#083367',fg='white')
labelblock.place(height=40, width=200, x=310, y=220)

BlockButton =Button(windowblock, text='Ok', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18),command=Go)
BlockButton.place(x=350, y=350, height=50, width=150)

BlockButton =Button(windowblock, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18),command=Back)
BlockButton.place(x=150, y=350, height=50, width=150)

windowblock.mainloop()
