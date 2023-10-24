from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import numpy.random as rd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies_dataset.csv")
movie_list = []
ps = PorterStemmer()
def stem(text):
    y=[]
    
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

for index,row in df.iterrows():
    df.loc[index, 'tags'] = stem(row['tags'])
cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    global movie_list
    lang_list = ['Hindi', 'English', 'Tamil','Telugu', 'Marathi']
    movie_lists = df[df['title'].str.contains(movie)]
    if len(movie_lists):  
        movie_idx= movie_lists.index[0]
        distances = similarity[movie_idx]
        movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    
        hr = rd.randint(1, 3)
        mi = rd.randint(0, 59)
        se = rd.randint(0, 59)
        ll = rd.choice(lang_list, 2)
        movie_list.append([movie_lists.iloc[0]['title'], str(hr).zfill(2)+":"+str(mi).zfill(2)+":"+str(se).zfill(2), ll[0]+", "+ll[1]])
        for i in movies_list:
            hr = rd.randint(1, 3)
            mi = rd.randint(0, 59)
            se = rd.randint(0, 59)
            ll = rd.choice(lang_list, 2)
            movie_list.append([df.iloc[i[0]].title, str(hr).zfill(2)+":"+str(mi).zfill(2)+":"+str(se).zfill(2), ll[0]+", "+ll[1]])
    else:
        return 'No movies found. Please check your input'

data = ''    
with open('data_search.txt') as f:
    data += f.readline()
recommend(data)

root = Tk()
root.geometry('800x700')
root.config(background = 'black')
root.title('Search Results')
root.resizable(False, False)

logo_frame = Frame(root, background = 'black')
image_height = 60
image_width = 180

logo_image = Image.open('amazon_logo2.png')

logo_image = logo_image.resize((image_width, image_height), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)

logo = Label(logo_frame, image = logo_image, border = 0)
logo.pack()
logo_frame.pack(anchor = 'n', fill = 'x', expand = True)

result_label = Label(root, text = f'Search Results for: {data}', font = ('Lucida', 18, 'bold'), background = 'black', fg = 'white')
result_label.place(x = 10, y = 70)

movie_label = Label(root, text = 'Name', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
movie_label.place(x = 110, y = 130)

duration_label = Label(root, text = 'Duration', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
duration_label.place(x = 350, y = 130)

language_label = Label(root, text = 'Language', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
language_label.place(x = 602, y = 130)

movie_frame = Frame(root, height = 210, width = 800, background = 'black')



movie_listbox = Listbox(movie_frame, background = 'black', fg = 'white', height = 8, width = 22, border = 0, font = 20)
movie_listbox.configure(justify = 'center')
movie_listbox.place(x = 20, y = 10)


duration_listbox = Listbox(movie_frame, background = 'black', fg = 'white', height = 8, width = 22, border = 0, font = 20)
duration_listbox.configure(justify = 'center')
duration_listbox.place(x = 275, y = 10)

language_listbox = Listbox(movie_frame, background = 'black', fg = 'white', height = 8, width = 22, border = 0, font = 20)
language_listbox.configure(justify = 'center')
language_listbox.place(x = 530, y = 10)

for i in range(len(movie_list)):
    movie_listbox.insert(END, movie_list[i][0])
    duration_listbox.insert(END, movie_list[i][1])
    language_listbox.insert(END, movie_list[i][2])

movie_frame.place(x = 0, y = 160)


plan_frame = Frame(root, background = 'black', height = 210, width = 800)

name_label = Label(root, text = 'Movie Plan', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
name_label.place(x = 140, y = 410)

m1_label = Label(root, text = '1 month', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
m1_label.place(x = 407, y = 410)

m3_label = Label(root, text = '3 month', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
m3_label.place(x = 504, y = 410)

m6_label = Label(root, text = '6 month', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
m6_label.place(x = 601, y = 410)

y1_label = Label(root, text = ' 1 year', font = ('Arial', 14, 'bold'), background = 'black', fg = 'white')
y1_label.place(x = 698, y = 410)

name_list = Listbox(plan_frame, background = 'black', fg = 'white', height = 7, width = 35, border = 0, font = 20)
name_list.configure(justify = 'center')
name_list.place(x = 10, y = 8)

m1_list = Listbox(plan_frame, background = 'black', fg = 'white', height = 7, width = 8, border = 0, font = 20)
m1_list.configure(justify = 'center')
m1_list.place(x = 405, y = 8)

m3_list = Listbox(plan_frame, background = 'black', fg = 'white', height = 7, width = 8, border = 0, font = 20)
m3_list.configure(justify = 'center')
m3_list.place(x = 501, y = 8)

m6_list = Listbox(plan_frame, background = 'black', fg = 'white', height = 7, width = 8, border = 0, font = 20)
m6_list.configure(justify = 'center')
m6_list.place(x = 597, y = 8)

y1_list = Listbox(plan_frame, background = 'black', fg = 'white', height = 7, width = 8, border = 0, font = 20)
y1_list.configure(justify = 'center')
y1_list.place(x = 693, y = 8)

# buy_label = Label(root, background = 'black', )

plan_list = [
    ['Thriller Movies', '149', '400', '550', '700'],
    ['Sci-Fi Movies', '149', '400', '550', '700'],
    ['Comedy Movies', '139', '380', '500', '650'],
    ['Horror Movies', '159', '420', '600', '750'],
    ['Romantic Comedy Movies', '200', '550', '650', '800'],
    ['Animated Movies', '100', '250', '400', '600'],
    ['Documentry Movies', '100', '250', '400', '600'],
]

for item in plan_list:
    name_list.insert(END, item[0])
    m1_list.insert(END, item[1])
    m3_list.insert(END, item[2])
    m6_list.insert(END, item[3])
    y1_list.insert(END, item[4])

plan_frame.place(x = 0, y = 440)



root.mainloop()