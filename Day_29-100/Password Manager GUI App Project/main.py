import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("THE PassWord Manager")
window.config(padx=50, pady=50)

canva = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="Day_29-100\\Password Manager GUI App Project\\logo.png")
canva.create_image(100, 100, image=logo_img)
canva.grid(column=1, row=0)



window.mainloop()


