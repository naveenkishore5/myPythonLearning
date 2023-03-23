from tkinter import *

window = Tk()
window.title('Naveen tkinter')
window.minsize(width=500, height=300)


# Label

mylabel = Label(text='Hi Naveen', font=('Arial', 24, 'bold'))
mylabel.pack()


# Button

def button_clicked():
    new_text = entry.get()
    mylabel.config(text=new_text)


button = Button(text='click me', command=button_clicked)
button.pack()


# Entry

entry = Entry(width=20)
entry.pack()
print(entry.get())






window.mainloop()



