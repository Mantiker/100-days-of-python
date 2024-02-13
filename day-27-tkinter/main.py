import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# Labels
equal_desciption_label = tkinter.Label(text="is equal to", font=("Arial", 16))
equal_desciption_label.grid(column=0, row=1)

result_km_label = tkinter.Label(text="0", font=("Arial", 16, "bold"))
result_km_label.grid(column=1, row=1)

mile_desciption_label = tkinter.Label(text="Miles", font=("Arial", 16))
mile_desciption_label.grid(column=2, row=0)

km_desciption_label = tkinter.Label(text="Km", font=("Arial", 16))
km_desciption_label.grid(column=2, row=1)

# Entry
input = tkinter.Entry(width=5, font=("Arial", 16))
input.insert(tkinter.END, "0")
input.grid(column=1, row=0)

# Button
def button_clicked():
    result_km_label.config(text=str(float(input.get()) * 1.61))

convert_button = tkinter.Button(text="Calculate", command=button_clicked, font=("Arial", 16))
convert_button.grid(column=1, row=2)


window.mainloop()