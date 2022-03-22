from cgitb import text
from math import floor
from tabnanny import check
from tkinter import *
from tkinter import font
from turtle import bgcolor, title
import time
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
CYCLE=0

# ---------------------------- TIMER RESET ------------------------------- # 
def reseted(): 
    canvas.itemconfig(counter_label,text="5" )
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def started(): 
    global CYCLE 
    CYCLE +=1
    #Timer devam etmeli . 
    if CYCLE !=1 and CYCLE % 2 == 0 : 
        counter(1*60) 
    elif CYCLE == 1 or CYCLE % 2 == 1 : 
        counter(2*60)      
    #counter(25 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count) : 
    mn= floor(count/60)
    sc= count % 60 
    if sc == 0 : 
        sc = "00" 
    elif sc < 10 : 
        sc = f"0{sc}"
        if sc == 0 :
            mn = mn-1
    canvas.itemconfig(counter_label,text=f"{mn}:{sc}", )
    if count > 0 :
      window.after(1000 , counter , count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=35,pady=50)

canvas = Canvas(width=512,height=512)
coffee = PhotoImage(file="hard-work.png")
canvas.create_image(250,250, image=coffee)
counter_label = canvas.create_text(170,270,text="25:00",fill=PINK, font=(FONT_NAME,35,"bold"))
#counter(5)
canvas.grid(column=1,row=1)
start = Button(width=5,height=1,text="START",highlightthickness=0,font=(FONT_NAME,12,"bold"),bg=PINK,command=started)
start.grid(row=0,column=0)
reset = Button(width=5,height=1,text="RESET",highlightthickness=0,font=(FONT_NAME,12,"bold"),bg=PINK,command=reseted)
reset.grid(row=0,column=3)

title_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"),fg=GREEN)
title_label.grid(row=0,column=1)

check_mark= Label(text=check_mark ,font=(FONT_NAME, 15, "bold") ,  fg=GREEN )
check_mark.grid(column=1,row=2)



window.mainloop()