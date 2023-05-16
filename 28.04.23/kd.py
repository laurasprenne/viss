from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from datetime import date

window = Tk()
window.geometry("600x400")
window.title("Your age")
window.config(background="white")

# def calculate():
#     years = 2023 - (int(year.get()))
    # months =
    # days = (int(day.get()))
    # label.config(text="You are " + str(years) + " years old")

def calculateYears():
    today = date.today()
    years = today.year - int(birthyear.get()) - ((today.month, today.day) < (int(birthmonth.get()), int(birthday.get())))
    label.config(text="You are " + str(years) + " years old")

def calculateDays():
    today = date.today()
    days = today
    days = today.year - int(birthyear.get()) - ((today.month, today.day) < (int(birthmonth.get()), int(birthday.get())))
    label.config(text="You are " + str(days) + " days old")


label = Label(window,
            font=("Visby",15, "bold"),
            text="",
            background="white",
            relief=FLAT)

label.place(x=120, y=200)
    
birthday = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

birthday.place(x=10, y=60)

birthmonth = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

birthmonth.place(x=10, y=100)

birthyear = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

birthyear.place(x=10, y=140)


submitb = Button(window,
                font=("Visby",13, "bold"),
                text="submit",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=calculateYears)

inYears = Button(window,
                font=("Visby",13, "bold"),
                text="years",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=calculateYears)

inDays = Button(window,
                font=("Visby",13, "bold"),
                text="days",
                background="#94a0a8",
                activebackground="#94a0a8",
                # command=calculateDays
)

inSeconds = Button(window,
                font=("Visby",13, "bold"),
                text="seconds",
                background="#94a0a8",
                activebackground="#94a0a8",
                # command=calculateSeconds
)

submitb.place(x=330, y= 140)

inYears.place(x=10, y= 180)
inDays.place(x=90, y= 180)
inSeconds.place(x=170, y= 180)


window.mainloop()