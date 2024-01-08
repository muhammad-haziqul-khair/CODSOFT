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

#Username
user_name_frame = Frame(root,relief=RIDGE,bg="#2ecc71")
user_name_frame.grid(row = 0,column=0,padx=10,pady=10)
user_name_label = Label(user_name_frame,text="User",font = ("Ariel",20,"bold"),bg ="#2ecc71",fg="#ffffff")
user_name_label.grid(row =1,column=1)

# Computer Name
comp_name_frame = Frame(root,relief=RIDGE,bg="#2ecc71")
comp_name_frame.grid(row = 0,column=2,padx=10,pady=10)
comp_name_label = Label(comp_name_frame,text="Computer",font = ("Ariel",20,"bold"),bg ="#2ecc71",fg="#ffffff")
comp_name_label.grid(row =1,column=1)

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

# Frame for Player Score
score_frame = Frame(root,relief=RIDGE,bg = "#2ecc71",width =250,height = 20)
score_frame.grid(row=1,column = 1,padx=10,pady=10)

#User Score
user_score = 0
user_score_label = Label(score_frame,text=user_score,font = ("Ariel",50,"bold"),fg="#ffffff",bg ="#2ecc71")
user_score_label.grid(row=1,column=1,pady=5)

space_label = Label(score_frame,text="\t\t\t\t\t    ",bg="#2ecc71",fg="#ffffff")
space_label.grid(row=1, column=2)

#Computer Score
comp_score = 0
comp_score_label = Label(score_frame,text=comp_score,font = ("Ariel",50,"bold"),bg ="#2ecc71",fg="#ffffff")
comp_score_label.grid(row=1,column=3,pady=5)

#winning statement
win_frame = Frame(root,relief=RIDGE,bg = "#2ecc71")
win_frame.grid(row=2,column = 1,padx=10,pady=10)
win_label = Label(win_frame,text="PLAY!",font = ("Ariel",20,"bold"),fg="#ffffff",bg ="#2ecc71")
win_label.grid(row=1,column=1,pady=5)

root.mainloop()
