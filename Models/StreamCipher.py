from tkinter import *
from tkinter import messagebox
import subprocess
import tkinter as tk
def choise():
    labelS.config(text='your choise is '+streamChoise.get())
    
def Go():
    selectedValue = streamChoise.get()
    if selectedValue == 'Monoalphabetic':
        windowstream.destroy()
        subprocess.run(["python", "Models\Monoalphapetic.py"])
    elif selectedValue == 'polyalphabetic':
        windowstream.destroy()
        subprocess.run(["python", "Models\Polyalphabetic.py"])
    elif selectedValue == 'Rail Fence':
        windowstream.destroy()
        subprocess.run(["python", "Models\ReilFence.py"]) 
    elif selectedValue == 'Ceasar':
        windowstream.destroy()
        subprocess.run(["python", "Models\Ceasar.py"])        
    elif selectedValue == 'vigenere':
        windowstream.destroy()
        subprocess.run(["python", "Models\\vegenere.py"])
    elif selectedValue == 'playfiar':
        windowstream.destroy()
        subprocess.run(["python", "Models\PlayFair.py"])        
    
    elif selectedValue == 'Row Transoposition':
        windowstream.destroy()
        subprocess.run(["python", "Models\\rowTransoposition.py"])
    
def Back():
    windowstream.destroy()
    subprocess.run(["python", "Models\CipherType.py"])   

    
windowstream = Tk()
windowstream.title("Stream Cipher")
windowstream.geometry('600x500')
windowstream.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(windowstream, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

labelStream =Label(windowstream, text="What type of stream Cipher😇:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelStream.place(x=20, y=60)

streamChoise =StringVar()

ceaser =Radiobutton(windowstream, text='Ceasar Cipher', variable=streamChoise, value='Ceasar', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
ceaser.place(x=50, y=150)

Monoalphabetic =Radiobutton(windowstream, text='Monoalphabetic', variable=streamChoise, value='Monoalphabetic', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
Monoalphabetic.place(x=50, y=200)

playfiar =Radiobutton(windowstream, text='playfiar', variable=streamChoise, value='playfiar', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
playfiar.place(x=50, y=250)

polyalphabetic =Radiobutton(windowstream, text='polyalphabetic', variable=streamChoise, value='polyalphabetic', bg='#083367', fg='white', font=('arabic typesetting', 20), command=choise)
polyalphabetic.place(x=310, y=150)

vigenere =Radiobutton(windowstream, text='vigenere', variable=streamChoise, value='vigenere', bg='#083367', fg='white', font=('arabic typesetting', 20), command=choise)
vigenere.place(x=310, y=200)

railFence =Radiobutton(windowstream, text='Rail Fence', variable=streamChoise, value='Rail Fence', bg='#083367', fg='white', font=('arabic typesetting', 20), command=choise)
railFence.place(x=310, y=250)

rowTransoposition =Radiobutton(windowstream, text='Row Transoposition', variable=streamChoise, value='Row Transoposition', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
rowTransoposition.place(x=140, y=310)

labelS =Label(windowstream, text='', relief='groove', bg='#000522',fg='white')
labelS.place(height=40, width=200, x=180, y=450)

applyButton =Button(windowstream, text='Ok', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18),command=Go)
applyButton.place(x=400, y=450, height=50, width=150)

applyButton =Button(windowstream, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18),command=Back)
applyButton.place(x=10, y=450, height=50, width=150)


windowstream.mainloop()
