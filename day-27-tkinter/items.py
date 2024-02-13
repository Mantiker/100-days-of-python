import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

my_label["text"] = "text"
my_label.config(text="new text")

# Button

def button_clicked():
    my_label.config(text=input.get())

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()


# Entry
input = tkinter.Entry(width=10)
input.insert(tkinter.END, "some text")
input.pack()

# Textbox
textbox = tkinter.Text(width=30, height=5)
textbox.focus()
textbox.insert(tkinter.END, "multi-line text")
textbox.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# CheckButton
def checkbutton_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is ON?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radio Buttons
def radio_used():
    print(radio_state.get())
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

# List box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()