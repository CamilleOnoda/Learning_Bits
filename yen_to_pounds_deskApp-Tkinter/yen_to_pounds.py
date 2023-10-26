from tkinter import *

window = Tk()
window.title("Pounds to Yen converter")
window.minsize(width=350, height=200)

def yen_to_pound():
    yen = float(yen_input.get())
    pounds = yen * 0.0055
    amount_pounds_label.config(text=f"{pounds}")


yen_input = Entry()
yen_input.grid(column=1, row=0)

yen_label = Label(text="Yens")
yen_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

amount_pounds_label = Label(text="0")
amount_pounds_label.grid(column=1, row=1)

pound_label = Label(text="pounds")
pound_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=yen_to_pound)
calculate_button.grid(column=1, row=2)


window.mainloop()
