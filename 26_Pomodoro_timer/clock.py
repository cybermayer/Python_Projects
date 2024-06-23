
import tkinter
from PIL import Image, ImageTk
import time 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.02
LONG_BREAK_MIN = 0.02
reps = 0
full_period = 0
nth = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer(break_in_progress=True):
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    if break_in_progress == True:
        label.config(text="POMODORO TIMER", font=("Bauhaus 93", 24, "bold"), bg="blue", fg="red")
        label.place(x=60, y=35)
    elif break_in_progress == False:
        label.config(text="That's enough for today", font=("Bauhaus 93", 24, "bold"), bg="blue", fg="red")
        label.place(x=20, y=35)
    global reps
    reps = 0
    global nth
    nth = 0
    for _ in range(12):
        nth +=1
        check = tkinter.Label(text="✔", font=("Bauhaus 93", 12, "bold"), fg="blue",bg="blue")
        UNIT = 20
        align = UNIT*nth
        line = 300
        if nth >4 and nth <=8:
            align -=80
            line+=20
        elif nth >8 and nth < 12:
            align -=160
            line+=40 
        check.place(x=140+align, y=line)
    nth = 0
    
# ---------------------------- SECTION COUNTER ------------------------------- #

def nth_tomato(nth):
    check = tkinter.Label(text="✔", font=("Bauhaus 93", 12, "bold"), fg="white",bg="blue")
    UNIT = 20
    align = UNIT*nth
    line = 300
    if nth >4 and nth <=8:
        align -=80
        line+=20
    elif nth >8 and nth <12:
        align -=160
        line+=40
    if nth == 12:
        reset_timer(break_in_progress=False)   
        align = 50
        line = 300
        check = tkinter.Label(text="✔", font=("Bauhaus 93", 30, "bold"), fg="white",bg="blue")
    check.place(x=140+align, y=line)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps%8==0:
        label.config(text="LONG BREAK")
        label.place(x=97, y=35)
        global nth
        nth +=1
        nth_tomato(nth)
        count_down(LONG_BREAK_MIN*60)
    elif reps%2==1:
        label.config(text="WORK SECTION")
        label.place(x=85, y=35)
        count_down(WORK_MIN*60)
    elif reps%2==0:
        label.config(text="SHORT BREAK")
        label.place(x=97, y=35)
        nth +=1
        nth_tomato(nth)
        count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = math.floor(count/60)
    if min<10:
        min=f"0{min}"
    sec = count%60 
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count >= 1:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
    
        



# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.geometry("400x400")
window.title("POMODORO APP")
window.config(bg="blue")





canvas = tkinter.Canvas(width=200, height=223)
img = tkinter.PhotoImage(file=r"tomato.png")
canvas.create_image(100, 80, image=img)
timer_text = canvas.create_text(100, 100, text="00:00", font=("Courier", 22, "bold"), fill="white")
canvas.config(bg="blue", highlightthickness=0)
canvas.pack(expand=True)




label = tkinter.Label(text="POMODORO TIMER", font=("Bauhaus 93", 24, "bold"), bg="blue", fg="red")
label.place(x=60, y=35)


start_button = tkinter.Button(text="START", bg="lime", command=start_timer)
start_button.place(x=75, y=300)

reset_button = tkinter.Button(text="RESET", bg="darkgoldenrod", command=reset_timer)
reset_button.place(x=280, y=300)



window.mainloop()