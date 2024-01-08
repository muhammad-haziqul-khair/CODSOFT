from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("ROCK PAPER SCISSOR")
root.iconbitmap("Task4(rock_paper_scissor)/images/rps.ico")
root.geometry("800x500")
root.resizable(False,False)
root.config(bg="#2ecc71")

#Load Imgage
user_rock_img = ImageTk.PhotoImage(Image.open("Task4(rock_paper_scissor)/images/rock.png"))
comp_rock_img = ImageTk.PhotoImage(Image.open("Task4(rock_paper_scissor)/images/comp_rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Task4(rock_paper_scissor)/images/paper.png"))
user_scissor_img = ImageTk.PhotoImage(Image.open("Task4(rock_paper_scissor)/images/scissor.png"))
comp_scissor_img = ImageTk.PhotoImage(Image.open("Task4(rock_paper_scissor)/images/comp_scissor.png"))

# User Choice Image 
user_img_canvas = Canvas(root,relief=RIDGE,bg = "#2ecc71",width =300)
user_img_canvas.grid(row=1,column = 0,rowspan=2,padx=10,pady=10)
user_img_label = Label(user_img_canvas,image=user_rock_img,bg = "#2ecc71",fg="#ffffff")
user_img_label.pack(side=LEFT)

# Computer Choice Image
comp_img_canvas = Canvas(root, relief=RIDGE,bg = "#2ecc71")
comp_img_canvas.grid(row=1,column = 2,rowspan=2,padx=10,pady=10)
comp_img_label = Label(comp_img_canvas,image=comp_rock_img,bg = "#2ecc71",fg="#ffffff")
comp_img_label.pack(side=RIGHT)

root.mainloop()