
import tkinter
from PIL import Image,ImageTk
import time 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

in_period = False

def start():
    global period
    period = 1
    global in_period
    in_period = True



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def countdown(minute, secund):
    min = minute
    sec = secund
    sec -= 1
    if sec == -1:
        sec = 59
    if sec == 59:
        min -= 1
    remain_time = {"m": min,
                   "s": sec}
    return remain_time 

def displaytime(remain_time):
    if remain_time["m"] >= 10:
        min_part = f"{str(remain_time['m'])}"
    elif remain_time["m"] <10:
        min_part = f"0{str(remain_time['m'])}" 

    if remain_time["s"] == 60:
        sec_part = "00"
    elif remain_time["s"] <10:
        sec_part = f"0{str(remain_time['s'])}"
    elif remain_time["s"] >= 10 and remain_time["s"] < 60:
        sec_part = str(remain_time["s"])   
    time_on_clock = f"{min_part}:{sec_part}"
    return time_on_clock


# ---------------------------- TOMATO COUNTER ------------------------------- # 
def nth_tomato(nth):
    check = tkinter.Label(text="✔", font=("Bauhaus 93", 12, "bold"), fg="white",bg="blue")
    UNIT = 20
    align = UNIT*nth
    check.place(x=140+align, y=300)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.geometry("400x400")
window.title("POMODORO APP")
window.config(bg="blue")

canvas = tkinter.Canvas(width=200, height=223)
img = tkinter.PhotoImage(file=r"tomato.png")
canvas.create_image(100, 80, image=img)
timey = canvas.create_text(100, 100, text="00:00", font=("Courier", 22, "bold"), fill="white")
canvas.config(bg="blue", highlightthickness=0)
canvas.pack(expand=True)


label = tkinter.Label(text="POMODORO TIMER", font=("Bauhaus 93", 24, "bold"), bg="blue", fg="red")
label.place(x=60, y=35)


start_button = tkinter.Button(text="START", bg="lime", command=start)
start_button.place(x=75, y=300)

reset_button = tkinter.Button(text="RESET", bg="darkgoldenrod", command=start)
reset_button.place(x=280, y=300)

while in_period == True:
    if period % 2 ==1 < 8:
        minute = 25
        secund = 1
        actual_period = True
    elif period % 2 ==0 < 8:
        nthpom +=1
        minute = 5
        second= 1
        actual_period = True
    if period == 8:
        nthpom +=1
        minute = 40
        second = 1
        actual_period = True
    while actual_period == True:        
        remain_time = countdown(minute, secund)
        minute = remain_time["m"]
        secund = remain_time["s"]
        time_on_clock = displaytime(remain_time)
        canvas.itemconfig(timey, text=time_on_clock)
        if minute == 0 and secund == 0:
            period +=1
            actual_period = False
            if period==9:
                nthpom = 0
                period = 1
        time.sleep(1)





window.mainloop()


