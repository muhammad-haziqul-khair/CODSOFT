from tkinter import *

def validate_input(num):
    if num.isdigit():
        return True
    elif num == "":
        return True
    else:
        return False

root = Tk()
root.config(bg ="#2B98DC")
root.title("Password Generator")
root.iconbitmap("myicon.ico")
root.geometry("600x300")
root.resizable(False,False)
reg = root.register(validate_input)

lb = Label(root,text = "Enter the length of Password: ",font=("Arial", 15, "bold"),bg ="#2B98DC",fg="white")
lb.grid(row=2,column=1,padx=10, pady=10)

length_var = IntVar()
length_entry = Entry(root,width=10,font=("Arial", 20, "bold"),justify="center",bg ="white",textvariable=length_var,validate="key",validatecommand=(reg,"%P"))
length_entry.grid(row=2,column=2,padx=10, pady=10)


root.mainloop()