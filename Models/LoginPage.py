import tkinter as tk
from tkinter import messagebox
import subprocess

window = tk.Tk()
window.title("Cyber Security")
window.geometry('600x500')
window.config(bg='#000522')

background_image = tk.PhotoImage(file="Assets\cyber2.png")
background_image = background_image.subsample(1, 1)
background_label = tk.Label(window, image=background_image, highlightthickness=0)  # Set highlightthickness to 0
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

global TextBoxUser
global TextBoxPass

def Login():
    userName = TextBoxUser.get()
    password = TextBoxPass.get()

    if userName == '' or password == '':
        messagebox.showerror("Login", 'Blanks are not allowed')
    elif userName == 'Eng.Esraa' and password == '12345':
        window.destroy()  # Close this window
        subprocess.run(["python", "Models\CipherType.py"])
    elif userName != 'Eng.Esraa':
        messagebox.showinfo("Login", 'Wrong User Name')
    else:
        messagebox.showinfo("Login", 'Wrong Password')

labelLogin = tk.Label(window, text="Security Team💙", bg='#000522', fg='white', font=('arabic typesetting', 26))
labelLogin.place(x=180, y=60)

labelUser = tk.Label(window, text='User Name:', bg='#000522', fg='white', font=('arabic typesetting', 20))
labelUser.place(x=50, y=190)

labelPass = tk.Label(window, text='Password:', bg='#000522', fg='white', font=('arabic typesetting', 20))
labelPass.place(x=50, y=240)

TextBoxUser = tk.Entry(window, font=('arabic typesetting', 20))
TextBoxUser.place(x=220, y=190)

TextBoxPass = tk.Entry(window, font=('arabic typesetting', 20), show='*')
TextBoxPass.place(x=220, y=240)

loginButton = tk.Button(window, text='Login', bg='#083367', bd=5, fg='white', font=('arabic typesetting', 18), command=Login)
loginButton.place(x=250, y=350, height=50, width=150)

window.mainloop()
