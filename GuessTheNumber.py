import random
import os,sys
from os import close
from tkinter import*
from tkinter.ttk import *
tries = 0
screen = Tk()
screen.title("Guess the number")
screen.resizable(height=False, width=False)
screen.configure(background="#261E36")
screen.title("GuessTheNumber")
screen.geometry("400x200")
choice = IntVar()

def rescource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def close_app():
    screen.destroy()

def randomize():
    global a
    imglbl.configure(image=dice)
    difficulty = choice.get()
    if difficulty == 1:
        a = random.randint(0,50)
    elif difficulty == 2:
        a = random.randint(0,100)
    elif difficulty == 3:
        a = random.randint(0,200)
    #print(a)

def check(event):
    global tries
    guess = think.get()
    if int(guess) == a:
        imglbl.configure(image=correct)
    elif int(guess) > a:
        imglbl.configure(image=down)
    elif int(guess) < a:
        imglbl.configure(image=up)
    tries += 1
    triesL.config(text="tries: "+str(tries))
    think.delete(0,END)

up = PhotoImage(file=rescource_path("up_python.png"))
down = PhotoImage(file=rescource_path("Down_python.png"))
dice = PhotoImage(file=rescource_path("Dice_python.png"))
correct = PhotoImage(file=rescource_path("check_python.png"))

Lbl= Label(screen,text="Guess The Number",background="#261E36",foreground="white",)
rb1 = Radiobutton(screen, text="Easy(0-50)", value=1, variable=choice)
rb2 = Radiobutton(screen,text="Normal(0-100)",value=2,variable=choice)
rb3 = Radiobutton(screen,text="Hard(0-200)",value=3,variable=choice,)
Lbl2= Label(screen,text="In this Game you will try to find a secret  number"
                        "\nthat is randomly chosen every round"
                        "\nTry to guess it with the least possible tries!",justify=CENTER, background="#261E36",foreground="white")
btn1 = Button(screen,text="Randomize", command=randomize)
btn2 = Button(screen,text="Exit",command=close_app)
think = Entry(screen)
imglbl = Label(screen,image = dice,background="#261E36",foreground="white")
triesL = Label(screen,text="tries:0",background="#261E36",foreground="white")


Lbl= Label(screen,text="Guess The Number",background="#261E36",foreground="white",)
rb1 = Radiobutton(screen, text="Easy(0-50)", value=1, variable=choice)
rb2 = Radiobutton(screen,text="Normal(0-100)",value=2,variable=choice)
rb3 = Radiobutton(screen,text="Hard(0-200)",value=3,variable=choice,)
Lbl2= Label(screen,text="In this Game you will try to find a secret  number"
                        "\nthat is randomly chosen every round"
                        "\nTry to guess it with the least possible tries!",justify=CENTER, background="#261E36",foreground="white")

Lbl.grid(row=0,column=2)
rb1.grid(row=1,column=1)
rb2.grid(row=1,column=2)
rb3.grid(row=1,column=3)
Lbl2.grid(row=2,column=1,columnspan=3)
btn1.grid(row=3,column=3)
btn2.grid(row=4,column=3)
think.grid(row=4,column=2)
imglbl.grid(row=3,column=0,rowspan=2)
triesL.grid(row=3,column=2)

screen.bind('<Return>', check)

screen.mainloop()