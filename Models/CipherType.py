from tkinter import *
from tkinter import messagebox
import subprocess

def choise():
    labelType.config(text='Your choice is ' + strType.get())

def Go():
    selectedValue = strType.get()
    if selectedValue == 'stream':
        windowType.destroy()
        subprocess.run(["python", "Models\\StreamCipher.py"])
    elif selectedValue == 'block':
        windowType.destroy()
        subprocess.run(["python", "Models\BlockCipher.py"])
    else:
        messagebox.showerror("Error", "Invalid choice")

def Back():
    windowType.destroy()
    subprocess.run(["python","Models\\LoginPage.py"])

windowType = Tk()
windowType.title("Cipher page")
windowType.geometry('600x500')
windowType.config(bg='#000522')

# Set background image
background_image = PhotoImage(file="Assets\cyber2.png")
background_label = Label(windowType, image=background_image)
background_label.place(relx=0.5, rely=0.5, anchor=CENTER)

labelT = Label(windowType, text="Cipher Type🤔:", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelT.place(x=20, y=60)

strType = StringVar()

# stream = Radiobutton(windowType, text='Stream Cipher', variable=strType, value='stream', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
# stream.place(x=50, y=190)

block = Radiobutton(windowType, text='Block Cipher', variable=strType, value='block', bg='#000522', fg='white', font=('arabic typesetting', 20), command=choise)
block.place(x=50, y=240)

labelType = Label(windowType, text='', relief='groove', bg='#083367', fg='white')
labelType.place(height=40, width=200, x=310, y=220)

TypeButton = Button(windowType, text='Ok', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Go)
TypeButton.place(x=390, y=350, height=50, width=150)

BackButton = Button(windowType, text='Back', bg='#000522', bd=5, fg='white', font=('arabic typesetting', 18), command=Back)
BackButton.place(x=190, y=350, height=50, width=150)

windowType.mainloop()
