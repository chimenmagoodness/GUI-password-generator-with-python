from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

window = Tk()
# window.minsize(width=400, height=400)
window.title("Password Generator")
window.config(padx=50, pady=50)


# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(5, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(6, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 12))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def check():
    pass_input = password_input.get()
    if len(pass_input) != 0:
        password_input.delete(0, END)
        generate_password()

    else:
        generate_password()


def add_password():
    save_website = web_input.get()
    save_email = email_username_input.get()
    save_password = password_input.get()
    date_to_save = f"{save_website} | {save_email} | {save_password} \n"

    if len(save_website) and len(save_password) > 1:
        is_ok = messagebox.askokcancel(title=save_website, message=f"These are the details entered: \nEmail: {save_email} \nPassword: {save_password} \nIs it ok to save ?")

        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(date_to_save)
                web_input.delete(0, END)
                password_input.delete(0, END)

    else:
        # messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
        # messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")


canvas = Canvas(width=300, height=300)
my_logo = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=my_logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1, pady=5)

web_input = Entry(width=39)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2, pady=5)

email_username_input = Entry(width=39)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "Switnexxtra@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=check)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=34, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
