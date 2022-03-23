from tkinter import *
from math import floor
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
CYCLE=0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def play() :
    playsound("notification.mp3")
def reseted(): 
    window.after_cancel(TIMER)
    canvas.itemconfig(counter_label,text=f"25:00",fill="PINK")
    global CYCLE 
    CYCLE = 0 
    check_mark.config(text="")
# TIMER MECHANISM  # 
def started(): 
    global CYCLE 
    CYCLE +=1
    print(CYCLE)
    #Timer devam etmeli .
    if CYCLE == 5 : 
        counter(4*60)  
        canvas.itemconfigure(counter_label, fill=RED)
        title_label.configure(text="LONG REST",fg=RED)
    elif CYCLE !=1 and CYCLE % 2 == 0 : 
        counter(1*60) 
        canvas.itemconfigure(counter_label, fill=GREEN)
        title_label.configure(text="REST",fg=GREEN)
        mark_str = int(CYCLE/2)*CHECK_MARK
        check_mark.config(text=mark_str)
    elif CYCLE == 1 or CYCLE % 2 == 1 : 
        counter(1*60) 
        canvas.itemconfigure(counter_label, fill=PINK) 
        title_label.configure(text="CONCENTRATE",fg=PINK)    
    #counter(25 * 60)
# COUNTDOWN MECHANISM # 
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
      global TIMER
      TIMER = window.after(1000 , counter , count - 1)
    elif count == 0:
      play()
      print("hımm")
      started()
      
          

          

# UI SETUP  #
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

check_mark= Label(font=(FONT_NAME, 15, "bold") ,  fg=GREEN )
check_mark.grid(column=1,row=2)



window.mainloop()