import tkinter

window = tkinter.Tk()
window.title("soo First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()

