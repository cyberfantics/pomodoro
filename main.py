import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(reset)
    canvas.itemconfig(text, text="00:00")
    check.config(text='Timer', fg="Orange", bg=YELLOW,
                 font=(FONT_NAME, 17, "bold"))
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_time():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    s_break = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(l_break)
        check.config(text="Long break", fg=RED, font=(FONT_NAME, 17, "bold"))
    if reps % 2 == 0:
        count_down(s_break)
        check.config(text="Short Break", fg=PINK, font=(FONT_NAME, 17, "bold"))
    else:
        count_down(work_min)
        check.config(text="Work", fg=GREEN, font=(FONT_NAME, 17, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global reset
        reset = window.after(1000, count_down, count - 1)
    else:
        start_time()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pandamora")

name = Label()
name.config(text="Pandamora", fg="Orange", bg=YELLOW, font=(FONT_NAME, 35))
name.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
canvas.grid(column=1, row=1)

text = canvas.create_text(100, 130, text="00:00",
                          fill="white", font=(FONT_NAME, 35, "bold"))

start = Button(text="Start", bg=YELLOW, width=4,
               highlightthickness=0, command=start_time)
start.grid(column=0, row=3)

reset = Button(text="Reset", bg=YELLOW, width=4,
               highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=3)

check = Label(text='Timer', fg="Orange", bg=YELLOW,
              font=(FONT_NAME, 17, "bold"))
check.grid(column=1, row=4)
window.mainloop()
