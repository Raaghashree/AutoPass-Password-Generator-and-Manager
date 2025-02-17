import tkinter as tk
from tkinter import messagebox

#FUNCTIONS
def save_password():
    website = w_entry.get()
    username = u_entry.get()
    password = p_entry.get()

    if website and username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"Website: {website}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n\n")
            messagebox.showinfo("Success", "Password added!")

    else:
        messagebox.showerror("Error","Please enter all fields")    

    w_entry.delete(0, tk.END)
    u_entry.delete(0, tk.END)
    p_entry.delete(0, tk.END)    

def retrieve_passwords():
    passwords=""

    try:
        with open("passwords.txt", 'r') as f:
            passwords=f.read()
    except FileNotFoundError:
        passwords= "Password database not found"
    
    messagebox.showinfo("Stored passwords", passwords)

'''def delete_password():
    temp_passwords = ""
    username=u_entry.get

    try:
        with open("passwords.text",'r') as f:
            for k in f:
                i = k.split(' ')
                if i[1]!= username:
                temp_passwords+=(f"Website: {i[0]}\nUsername: {i[1]}\nPassword: {i[2]}")
    
        with open("passwords.txt",'w') as f:
            for line in temp_passwords:
'''               


#TKINTER PAGE
root = tk.Tk()
root.title("Password Manager")
root.geometry("260x250")

w_label = tk.Label(root, text="Website:")
w_label.pack()
w_entry = tk.Entry(root)
w_entry.pack()

u_label = tk.Label(root, text="Username:")
u_label.pack()
u_entry = tk.Entry(root)
u_entry.pack()

p_label = tk.Label(root, text="Password:")
p_label.pack()
p_entry = tk.Entry(root)
p_entry.pack()

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

retrieve_button = tk.Button(root, text="Retrieve Passwords", command=retrieve_passwords)
retrieve_button.pack()

"""delete_button = tk.Button(root, text="Delete", command=delete_password)
delete_button.pack()"""

root.mainloop()
