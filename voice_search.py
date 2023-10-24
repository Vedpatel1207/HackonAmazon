from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import threading, time, subprocess

flag = True
anim = ['.', '..', '...']
def update():
    pt = 0
    while flag:
        result.delete(1.0, END)
        result.insert(INSERT, '\nListening', 'center')
        result.insert(INSERT, anim[pt])
        pt = (pt + 1) % 3
        time.sleep(1)

def recognize_speech():
    global flag
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio)
            flag = False
            result.delete(1.0, END)
            result.insert(INSERT, 'Recognized text:\n', 'center')
            result.insert(INSERT, recognized_text, 'center')
            f = open('data_search.txt', 'w')
            f.write(recognized_text)
            f.close()
            subprocess.run(['python', 'search_data.py'])
        except sr.UnknownValueError:
            flag = False
            result.delete(1.0, END)
            result.insert(INSERT, 'Could not understand audio')
        except sr.RequestError as e:
            flag = False
            result.delete(1.0, END)
            result.insert(INSERT, f'Could not request results; {e}')

def listen():
    result.delete(1.0, END)
    
    speech_thread = threading.Thread(target = recognize_speech)
    speech_thread.start()
    
    update_thread = threading.Thread(target = update)
    update_thread.start()
    

root = Tk()
root.geometry('500x400')
root.title('Voice Search')
root.config(background = 'white')
root.resizable(False, False)

image_height = 60
image_width = 180

logo_image = Image.open('amazon_logo2.png')

logo_image = logo_image.resize((image_width, image_height), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)


header = Frame(root, background = 'black', width = 500, height = 80)
logo = Label(root, image = logo_image, border = 0)
logo.place(x = 153, y = 10)
header.place(x = 0, y = 0)

result = Text(root, bg = 'white', border = 3, width = 44, font = 18, height = 3)
result.tag_configure('center', justify = 'center')
result.insert(END, '\n(Press Button to Start Speaking)', 'center')
result.place(x = 5, y = 105)

image_width = 190
image_height = 190

mic_on = Image.open('on.png')
mic_on = mic_on.resize((image_width, image_height), Image.Resampling.LANCZOS)
mic_on = ImageTk.PhotoImage(mic_on)

mic_button = Button(root, image = mic_on, height = 180, width = 180, command = listen, border = 0)
mic_button.place(x = 150, y = 195)

root.mainloop()