import tkinter

window = tkinter.Tk()
window.title("soo ori First GUI Program idk")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="New Text")

def button_clicked():
    my_label.config(text="Button got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()

