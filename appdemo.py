
from tkinter import *
import string
import random
import pyperclip

from tkinter import messagebox


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg='grey')
root.resizable(False, False)


choice=IntVar()
Font=('times new roman',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.pack(anchor="center", pady="10px")
#passwordLabel.grid(row = 0, column = 0,pady=10)


weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.pack(anchor="center", pady="5px")
#grid(row = 1, column = 0,pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.pack(anchor="center", pady="5px")
#grid(row = 2, column = 0,pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.pack(anchor="center", pady="5px")

lengthLabel=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.pack(anchor="center", pady="10px")


def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"


def on_leave(e):
    generate_btn['bg'] = "pink"
    generate_btn['fg'] = "black"

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.pack(anchor="center", pady="10px")#grid(pady=5)

generate_btn = Button(root, text="Generate Password", bg="#FF3399", fg="#FFFFFF", font=("ubuntu", 15), cursor="hand2",
                     command=generator)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.pack(anchor="center", pady="10px")



passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.pack(anchor="center", pady="10px")

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.pack(anchor="center", pady="5px")

#grid(pady=5)

manage_btn=Button(root,text="Manage Passwords",bg="#FF3399", fg="#FFFFFF", font=Font)
manage_btn.bind("<Enter>", on_enter)
manage_btn.bind("<Leave>", on_leave)
manage_btn.pack(anchor="center", pady="5px")
root.mainloop()

