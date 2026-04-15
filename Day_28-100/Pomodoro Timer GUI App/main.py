import tkinter

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Tomat timer")
window.config(padx=100, pady=50, bg=YELLOW)

canva = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="Day_28-100\\Pomodoro Timer GUI App\\tomato.png")
canva.create_image(100, 112, image=tomato_image)
canva.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

checkmarks_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()

