import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    my_label.config(text=input.get())

#Label
my_label = tkinter.Label(text = "I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=18)
print(input.get())
input.grid(column=2, row=2)

window.mainloop()

