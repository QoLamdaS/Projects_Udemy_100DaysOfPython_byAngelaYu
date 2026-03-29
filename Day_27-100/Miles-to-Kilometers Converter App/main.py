import tkinter

window = tkinter.Tk()
window.title("Miles-to-Kilometers Converter App")
window.config(padx=20, pady=20)
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    
