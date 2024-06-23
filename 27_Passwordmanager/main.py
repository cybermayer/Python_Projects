import tkinter 
from PIL import Image, ImageTk  
import pwgen  # import password generator
from tkinter import messagebox  
import json 

pwword = pwgen.Password()  # instantiate the password generator object

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def call_pw_gen() -> None:

    """

    Generate a new password and update the password field and clipboard.

    """
    global actual_pw
    # Generate password using parameters from entry fields
    actual_pw = pwword.generate(letter_field.get(), number_field.get(), special_field.get())
    password_field.delete(0, tkinter.END)  # Clear the current password field
    password_field.insert(0, actual_pw)  # Insert the new password into the field
    password_field.clipboard_clear()  # Clear clipboard
    password_field.clipboard_append(actual_pw)  # Copy new password to clipboard
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    """

    Save the entered website, ID, and password to a JSON file.

    """
    website = website_field.get()
    id = id_field.get()
    pswd = password_field.get()
    new_logs = {website: {"id": id, "password": pswd}}

    # Check if any required field is empty
    if len(website_field.get()) == 0 or len(id_field.get()) == 0 or len(password_field.get()) == 0:
        messagebox.showinfo(title="ERROR", message="All fields marked with * are mandatory to fill!")
        ready_to_save = False
    else:
        ready_to_save = True

    if ready_to_save:
        try:
            # Try to read existing data from the JSON file
            with open(r"passwords.json", "r") as logs_json:
                stored_logs = json.load(logs_json)
                stored_logs.update(new_logs)  # Update with new entry
        except FileNotFoundError:
            # If file not found, create a new one
            with open(r"passwords.json", "w") as logs_json:
                json.dump(new_logs, logs_json, indent=4)
        else:
            # Write updated data back to the file
            with open(r"passwords.json", "w") as logs_json:
                json.dump(stored_logs, logs_json, indent=4)

        # Clear the entry fields
        password_field.delete(0, tkinter.END)
        id_field.delete(0, tkinter.END)
        website_field.delete(0, tkinter.END)
        messagebox.showinfo(title="Successfully saved.", message="The login information has been successfully added to the repository!")

# ---------------------------- SEARCH MECHANISM  ------------------------------- #

def search():

    """

    Search for a website's login information in the JSON file and display it.

    """
    looking_for = website_field.get()
    if looking_for == "Admin":
        messagebox.showinfo(title="WELCOME IN THE ADMINMODE!", message="The ADMIN MODE has been activated!\nThe ADMIN has logged in to the system.\n")
    elif looking_for != "":
        try:
            # Try to read existing data from the JSON file
            with open(r"passwords.json", "r") as logs_json:
                stored_logs = json.load(logs_json)
                sitelogs = stored_logs[looking_for]  # Get the site's login info
                id = sitelogs["id"]
                pw = sitelogs["password"]
                messagebox.showinfo(title="LOG-INFOS", message=f"Email/Username:   {id}\n \nThe password has been copied to the clipboard.")

                # Copy the password to clipboard
                window.clipboard_clear()
                window.clipboard_append(pw)
        except KeyError:
            # If the website is not found in the file
            messagebox.showinfo(title="MISSING", message=f"No information stored for {looking_for} in the repository")
        finally:
            # Clear the entry fields
            password_field.delete(0, tkinter.END)
            id_field.delete(0, tkinter.END)
            website_field.delete(0, tkinter.END)
    else:
        messagebox.showinfo(title="ERROR", message="All fields marked with ** are mandatory to fill!")

# ---------------------------- UI SETUP ------------------------------- #

# Set up the main application window
window = tkinter.Tk()
window.geometry("580x620")  # Set window size
window.config(bg="white", highlightthickness=0, padx=20, pady=20)  # Set window background color and padding
window.title("PW-MANAGER")  # Set window title

# Load images
img = tkinter.PhotoImage(file=r"lock.png")
img2 = tkinter.PhotoImage(file=r"hand.png")

# Create and place the main canvas with an image
canvas = tkinter.Canvas(width=320, height=350, bg="white")
canvas.create_image(160, 175, image=img)
canvas.config(highlightthickness=0)
canvas.grid(column=1, row=0)

# Create and place the second canvas with another image
canvas2 = tkinter.Canvas(width=202, height=202, bg="white")
canvas2.create_image(101, 110, image=img2)
canvas2.config(highlightthickness=0)
canvas2.grid(column=0, row=0)

# Create and place the entry fields and labels
website = tkinter.Label(text="                         Website**                      : ", bg="white")
website.grid(column=0, row=2)
website_field = tkinter.Entry(width=45, highlightthickness=1, border=3)
website_field.focus()
website_field.grid(column=1, row=2, columnspan=2, pady=3)

id = tkinter.Label(text="                       Username*                     : ", bg="white")
id.grid(column=0, row=3)
id_field = tkinter.Entry(width=45, highlightthickness=1, border=3)
id_field.grid(column=1, row=3, columnspan=2, pady=3)

password = tkinter.Label(text="                        Password*                     : ", bg="white")
password.grid(column=0, row=4)
password_field = tkinter.Entry(width=45, highlightthickness=1, border=3, show="*")
password_field.grid(column=1, row=4, columnspan=2, pady=3)

# Create and place the fields for password generation parameters
letter_label = tkinter.Label(text="Letters: ", bg="white")
letter_label.place(x=220, y=450)
letter_field = tkinter.Entry(width=3, highlightthickness=1, border=3)
letter_field.insert(0, "8")
letter_field.place(x=265, y=450)

number_label = tkinter.Label(text="Numbers: ", bg="white")
number_label.place(x=305, y=450)
number_field = tkinter.Entry(width=3, highlightthickness=1, border=3)
number_field.insert(0, "4")
number_field.place(x=365, y=450)

special_label = tkinter.Label(text="Specials: ", bg="white")
special_label.place(x=405, y=450)
special_field = tkinter.Entry(width=3, highlightthickness=1, border=3)
special_field.insert(0, "4")
special_field.place(x=460, y=450)

# Create and place the buttons for generating password, adding to repository, and searching
generate_button = tkinter.Button(text="Generate new password", width=25, height=1, command=call_pw_gen, highlightthickness=1)
generate_button.place(x=10, y=450)

add_button = tkinter.Button(text="Add to repository", width=35, height=3, command=save_password)
add_button.place(x=233, y=490)

search_button = tkinter.Button(text="Search", width=35, command=search)
search_button.place(x=233, y=315)

# Run the Tkinter main loop
window.mainloop()
