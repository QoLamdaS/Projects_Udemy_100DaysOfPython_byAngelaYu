import tkinter

window = tkinter.Tk()
window.title("Miles-to-Kilometers Converter App")
window.config(padx=20, pady=20)
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=km)
result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
