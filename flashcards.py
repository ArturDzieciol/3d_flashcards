from tkinter import *
from random import randint
import pandas as pd
import openpyxl

root = Tk()
root.title('Chinese Language 3d flashcards')
root.geometry('550x550')

choose_direction_label = Label(root, text='Choose flashcards direction:', font=('Helvetica', 10)).pack(pady=10)

def hanzi_english():
    pass

def hanzi_pinyin():
    pass

choice_frame = Frame(root)
choice_frame.pack(pady=20)

hanzi_english_button = Button(choice_frame, text='汉字 to English', command=hanzi_english)
hanzi_english_button.grid(row=0, column=0, padx=20)

hanzi_pinyin_button = Button(choice_frame, text='汉字 to Pinyin', command=hanzi_pinyin)
hanzi_pinyin_button.grid(row=0, column=1, padx=20)

# load the words file

words = pd.read_excel('chinese_words.xlsx')

# get a count of our word list
count = len(words)


def next():
    global hinter, hint_count
    # clear the screen
    answer_label.config(text='')
    my_entry.delete(0, END)
    hint_label.config(text='')
    # reset hint variables
    hinter = ''
    hint_count = 0

    # create random selection
    global random_word # make this variable visible across entire program
    random_word = randint(0, count-1)
    # update label with Chinese word
    chinese_hanzi_word.config(text=words.iloc[random_word][0])

def answer():
    if my_entry.get().lower() == words.iloc[random_word][2].lower():
        answer_label.config(text=f'Correct! {words.iloc[random_word][0]} is {words.iloc[random_word][2]}')
    else:
        answer_label.config(text=f'Incorrect! {words.iloc[random_word][0]} is not {my_entry.get()}')

# keep track of the hints
hinter = ''
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words.iloc[random_word][2]):
        hinter = hinter + words.iloc[random_word][2][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1

chinese_hanzi_word = Label(root, text='', font=('Helvetica', 36))
chinese_hanzi_word.pack(pady=50)

answer_label = Label(root, text='')
answer_label.pack(pady=20)
my_entry = Entry(root, font=('Helvetica', 18))
my_entry.pack(pady=20)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text='Answer', command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text='Next', command=next)
next_button.grid(row=0, column=1, padx=20)

hint_button = Button(button_frame, text='Hint', command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create hint label
hint_label = Label(root, text='')
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()