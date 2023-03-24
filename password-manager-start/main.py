from tkinter import *
from tkinter import messagebox
import random
import paperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f',' g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    number_letters = [random.choice(numbers) for _ in range(nr_numbers)]
    symbol_letters = [random.choice(symbols) for _ in range(nr_symbols)]
    password = password_letters + number_letters + symbol_letters
    random.shuffle(password)
    password = ''.join(password)
    password_input.insert(0, password)
    paperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(web) or len(password) == 0:
        messagebox.showinfo(title='Warning', message='Web and Messagebox should not be empty')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'These are the details entered: \nEmail: {email}'
                                   f'\nPassword: {password} \n Is that okay?')
        if is_ok:
            f = open('file.txt', 'a')
            f.write(f'{web} | {email} | {password}\n')
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# canvas widget to add lock image to the GUI
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Website Label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

# Email/Username Label
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

# Password Label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Website input widget
website_input = Entry(width=38)
website_input.grid(column=1, row=1, columnspan=2)

# Email input
email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'naveen@gmail.com')

# Password input
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Generate button
generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(column=2, row=3)

# Add button
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()