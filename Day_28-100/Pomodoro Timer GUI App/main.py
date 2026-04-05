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

canva = tkinter.Canvas(width=200, height=224)
tomato_image = tkinter.PhotoImage(file="Day_28-100\\Pomodoro Timer GUI App\\tomato.png")
canva.create_image(100, 112, image=tomato_image)
canva.pack()



window.mainloop()

