from tabnanny import check
from tkinter import *
from tkinter import font
from turtle import bgcolor, title

from numpy import pad
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=35,pady=50)
canvas = Canvas(width=512,height=512)
coffee = PhotoImage(file="hard-work.png")
canvas.create_image(250,250, image=coffee)
canvas.create_text(170,270,text="00:00",fill=PINK, font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start = Button(width=5,height=1,text="START",highlightthickness=0,font=(FONT_NAME,12,"bold"),bg=PINK)
start.grid(row=0,column=0)
reset = Button(width=5,height=1,text="RESET",highlightthickness=0,font=(FONT_NAME,12,"bold"),bg=PINK)
reset.grid(row=0,column=3)

title_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"),fg=GREEN)
title_label.grid(row=0,column=1)

check_mark= Label(text=check_mark ,font=(FONT_NAME, 15, "bold") ,  fg=GREEN )
check_mark.grid(column=1,row=2)



window.mainloop()