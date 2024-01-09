from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("ROCK PAPER SCISSOR")
root.iconbitmap("Task4(rock_paper_scissor)/images/rps.ico")
root.geometry("800x500")
root.resizable(False,False)
root.config(bg="#2ecc71")

def restart_game():
    global user_score,comp_score
    user_score = 0
    comp_score = 0
    user_score_label.config(text=user_score)
    comp_score_label.config(text=comp_score)
    win_label.config(text="PLAY!")
    user_choice_label.config(text="Your Choice..")
    comp_choice_label.config(text="Bot Choice..")
    user_img_label.config(image=user_rock_img)
    comp_img_label.config(image=comp_rock_img)

def restart_clicked(event):
    restart_game()

def declare_winner(user,comp):
    global user_score, comp_score
    if user == comp:
        win_label.config(text="Match Tied!")
    elif user == "rock":
        if comp == "paper":
            comp_score += 1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Bot Won")
        else:
            user_score +=1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won")
    elif user == "paper":
        if comp == "rock":
            user_score +=1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won")
        else:
            comp_score += 1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Bot Won")
    elif user == "scissor":
        if comp == "paper":
            user_score += 1
            user_score_label.config(text=user_score)
            win_label.config(text="You Won")
        else:
            comp_score +=1
            comp_score_label.config(text=comp_score)
            win_label.config(text="Bot Won")
    else:
        pass

def players_turn(user_turn):
    possible_choice =["rock","paper","scissor"]
    comp_turn = random.choice(possible_choice)
    if comp_turn == "rock":
      comp_img_label.config(image=comp_rock_img)
      comp_choice_label.config(text="Bot chose ROCK!")
    elif comp_turn == "paper":
       comp_img_label.config(image=paper_img)
       comp_choice_label.config(text="Bot chose PAPER!")
    else:
       comp_img_label.config(image=comp_scissor_img)
       comp_choice_label.config(text="Bot chose SCISSOR!")
    if user_turn == "rock":
      user_img_label.config(image=user_rock_img)
      user_choice_label.config(text="You chose ROCK!")
    elif user_turn == "paper":
       user_img_label.config(image=paper_img)
       user_choice_label.config(text="You chose PAPER!")
    else:
       user_img_label.config(image=user_scissor_img)
       user_choice_label.config(text="You chose SCISSOR!")
    declare_winner(user_turn,comp_turn)

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

#user choice statement
user_choice_frame = Frame(root,relief=RIDGE,bg="#2ecc71")
user_choice_frame.grid(row = 3,column=0)
user_choice_label = Label(user_choice_frame,text="Your Choice..",font = ("Ariel",15,"normal"),bg ="#2ecc71",fg="#ffffff")
user_choice_label.grid(row =1,column=1)

#computer choice statement
comp_choice_frame = Frame(root,relief=RIDGE,bg="#2ecc71")
comp_choice_frame.grid(row = 3,column=2)
comp_choice_label = Label(comp_choice_frame,text="Bot Choice..",font = ("Ariel",15,"normal"),bg ="#2ecc71",fg="#ffffff")
comp_choice_label.grid(row =1,column=1)

#buttons
rock_btn = Button(root,text="Rock",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("rock"))
rock_btn.grid(row=5,column=0,padx=5,pady=10)

paper_btn = Button(root,text="Paper",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("paper"))
paper_btn.grid(row=5,column=1)

scissor_btn = Button(root,text="Scissor",width = 15,height=2,font=("Arial",15,"bold"),bg ="#ffffff",fg="black",command=lambda:players_turn("scissor"))
scissor_btn.grid(row=5,column=2)

#restarts game
restart_btn = Label(root,text="Restart",width = 15,height=2,cursor="hand2",font=("Arial",20,"underline"),bg ="#2ecc71",fg="#ffffff")
restart_btn.grid(row=6,column=1)
restart_btn.bind("<Button-1>",restart_clicked)


root.mainloop()
