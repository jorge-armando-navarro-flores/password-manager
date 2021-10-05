from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} "
                                                      f"\nPassword: {password} \nIs ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                new_data = f"{website} | {user} | {password}\n"
                data.write(new_data)
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)




#Entries
website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_input = Entry(width=45)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "user@email.com")

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

#Buttons

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
