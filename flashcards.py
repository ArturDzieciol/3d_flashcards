from tkinter import *
from random import randint

root = Tk()
root.title('Chinese Language 3d flashcards')
root.geometry('550x410')

words = [
    (('你好'), ('Hello')),
    (('谢谢'), ('Thank you')),
    (('再见'), ('Goodbye'))
]

# get a count of our word list
count = len(words)

chinese_hanzi_word = Label(root, text='', font=('Helvetica', 36))
chinese_hanzi_word.pack(pady=50)

answer_label = Label(root, text='')
answer_label.pack(pady=20)
my_entry = Entry(root, font=('Helvetica', 18))
my_entry.pack(pady=20)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text='Answer')
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text='Next')
next_button.grid(row=0, column=1, padx=20)

hint_button = Button(button_frame, text='Hint')
hint_button.grid(row=0, column=2, padx=20)

# Create hint label
hint_label = Label(root, text='')
hint_label.pack(pady=20)

root.mainloop()