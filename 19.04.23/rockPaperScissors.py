from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import random
import time

score = [0, 0, 0]
health = 3

def display(player, computer):
    movesLabel.config(text=player + " vs " + computer)
    healthLabel.config(text="Health: " + str(health))

def rockPaperScissors(player):
    global health

    movesLabel.config(text=player + " vs ")

    moves = ["rock", "paper", "scissors"]
    computer = random.choice(moves)

    if player == computer:
        score[1] += 1
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        score[0] += 1
    else:
        score[2] += 1
        health -= 1

    movesLabel.after(1000, lambda: display(player, computer))
    print(player, computer)

window = Tk()
window.geometry("400x400")
window.title("Rock, paper, scissors")
window.config(background="#F5DAE0")

#buttons
rock = Button(window,
                font=("Visby",13, "bold"),
                text="rock",
                background="#d56f87",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("rock"))

paper = Button(window,
                font=("Visby",13, "bold"),
                text="paper",
                background="#FBACBE",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("paper"))

scissors = Button(window,
                font=("Visby",13, "bold"),
                text="scissors",
                background="#DD4D6E",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("scissors"))


rock.place(x=40, y= 50)
paper.place(x=160, y= 50)
scissors.place(x=280, y= 50)

movesLabel = Label(window,
            font=("Visby",15, "bold"),
            text="",
            background="white",
            relief=FLAT)

movesLabel.place(x=120, y=150)

healthLabel = Label(window,
            font=("Visby",15, "bold"),
            text="",
            background="white",
            relief=FLAT)

healthLabel.pack(side=BOTTOM)

window.mainloop()