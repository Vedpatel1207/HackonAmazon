from tkinter import *
from PIL import Image, ImageTk
import subprocess

def verify(usernm, passwd):
    return True

def open_search_window():
    if not verify(username.get(), password.get()):
        return
    root.destroy()
    if search_type.get() == 'Text':
        subprocess.run(['python', 'text_search.py'])
    else:
        subprocess.run(['python', 'voice_search.py'])

root = Tk()
root.geometry('400x500')
root.title('Amazon Hackon Prototype')
root.config(bg = 'white')
root.resizable(False, False)

sign_in_label = Label(root, text = 'Sign In', font = ('Lucida', 30), bg = 'white')
sign_in_label.place(x = 13, y = 10)

logo_image = Image.open('amazon_logo.png')
image_width = 180
image_height = 45

logo_image = logo_image.resize((image_width, image_height), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)


logo = Label(root, image = logo_image, border = 0)
logo.place(x = 175, y = 13)

username_label = Label(root, text = 'Email or mobile phone number', font = ('arial', 18), bg = 'White')
username_label.place(x = 23, y = 90)

username = StringVar()
username_input = Entry(root, textvariable = username, highlightthickness = 1, highlightbackground = 'black', width = 30, font = 20)
username_input.place(x = 27, y = 125)

password_label = Label(root, text = 'Password', font = ('arial', 18), bg = 'White')
password_label.place(x = 23, y = 175)

password = StringVar()
password_input = Entry(root, textvariable = password, highlightthickness = 1, highlightbackground = 'black', width = 30, font = 20)
password_input.place(x = 27, y = 210)

search_options = ['Text', 'Voice']

search_label = Label(root, text = 'Search by: ', bg = 'white', font = 13)
search_label.place(x = 93, y = 290)

search_type = StringVar()
search_type.set(search_options[0])
search_type_field = OptionMenu(root, search_type, *search_options)
search_type_field.config(width=10, border=1)
search_type_field.place(x = 203, y = 292)

login_button = Button(root, text = 'Sign In', background = 'Orange', font = ('Monotext', 15), width = 15, command = open_search_window)
login_button.place(x = 103, y = 350)

root.mainloop()