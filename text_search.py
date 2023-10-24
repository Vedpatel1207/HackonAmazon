from tkinter import *
from PIL import Image, ImageTk
import subprocess

def search_text():
    f = open('data_search.txt', 'w')
    f.write(search.get())
    f.close()
    root.destroy()
    subprocess.run(['python', 'search_data.py'])

root = Tk()
root.geometry("385x270")
root.config(background = 'white')
root.resizable(False, False)

image_height = 60
image_width = 180

logo_image = Image.open('amazon_logo2.png')

logo_image = logo_image.resize((image_width, image_height), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)


header = Frame(root, background = 'black', width = 385, height = 80)
logo = Label(root, image = logo_image, border = 0)
logo.place(x = 103, y = 10)
header.place(x = 0, y = 0)

search_label = Label(root, text = 'Enter text to search', font = ('arial', 18), bg = 'White')
search_label.place(x = 23, y = 115)

search = StringVar()
search_input = Entry(root, textvariable = search, highlightthickness = 1, highlightbackground = 'black', width = 30, font = 20)
search_input.place(x = 27, y = 150)

search_button = Button(root, text = 'Search', font = ('Lucida', 15, 'bold'), border = 1, background = 'Orange', command = search_text)
search_button.place(x = 138, y = 200)

root.mainloop()