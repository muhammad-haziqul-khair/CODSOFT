from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

#generates a random password
def generate_password():
    global length
    length = length_var.get()
    if length == 0:
        messagebox.showerror("Error", "Enter a password length")
    characters = str(string.ascii_letters+string.digits+string.punctuation)
    char_lst = []
    for char in characters:
        char_lst.append(char)
    random.shuffle(char_lst)
    global password,pswd_label
    password = ""
    for password_character in range(length):
        password += random.choice(char_lst)
    pswd_label.config(text=password)

#validates input to be integer only
def validate_input(num):  
    if num.isdigit():
        return True
    elif num == "":
        return True
    else:
        return False
    
def copy_password():
    try:
        pyperclip.copy(password)
        messagebox.showinfo(root,"Text Copied to Clipboard ):")
    except:
        messagebox.showerror("Error","Enter the Password length!")

root = Tk()
root.config(bg ="#2B98DC")
root.title("Password Generator")
root.iconbitmap("Task3(password_generator)/images/myicon.ico")
root.geometry("600x300")
root.resizable(False,False)
reg = root.register(validate_input)

lb = Label(root,text = "Enter the length of Password: ",font=("Arial", 15, "bold"),bg ="#2B98DC",fg="white")
lb.grid(row=2,column=1,padx=10, pady=10)

# entry widget for getting password length
length_var = IntVar()
length_entry = Entry(root,width=10,font=("Arial", 20, "bold"),justify="center",bg ="white",textvariable=length_var,validate="key",validatecommand=(reg,"%P"))
length_entry.grid(row=2,column=2,padx=10, pady=10)

#button for generating password 
btn_pswd = Button(root,text="Generate Password",width = 20,font=7,command=generate_password)
btn_pswd.grid(row=3,column=1,padx=10, pady=10)

#button to copy password
btn_copy = Button(root,text="Copy Password",width = 20,font=7,bg="white",command=copy_password)
btn_copy.grid(row=3,column=2,padx=10, pady=10)

pswd_label = pswd_label = Label(root,text ="",font =("Arial",20,"bold"),width= 20,bg ="#2B98DC",fg="white")
pswd_label.grid(row=4,column=1)

root.mainloop()