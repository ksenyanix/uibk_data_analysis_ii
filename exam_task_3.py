'''
You can find three English texts by famous authors in the data folder: “The Picture of Dorian
Gray” by Oscar Wilde; “Adventures of Huckleberry Finn” by Mark Twain, and “The hound of
the Baskervilles” by Sir Arthur Doyle.
A friend wants to know how many different words each author used in each book. By
“different words” he refers to the ground form of a word. To illustrate what he means, he uses
the following paragraph as example:
    This is a sentence. There are many sentences.
This paragraph has 8 words, but only 6 different words:
(“this”, “be”, “a”, “sentence”. “there”, “be”*, “many”, “sentence”*)
Words marked with * appear twice.
Please write a program that is able to calculate the number of different words in each book.
'''

import os
import re

def content(file):
    with open('exam/' + file, 'r', encoding='utf8') as file:
        data = file.read()
    return data

raw_books = []
dirs = os.listdir('exam')
for file in dirs:
    file_to_string = content(file)
    raw_books.append(re.findall(r"[\w]+|[^\s\w]", file_to_string))
    
#[[], [], []]

def only_words(books):
    books_punc = [] #all books
    for book in books:
        book_punc = [] #every book
        for word in book:
            w = re.sub(r'[\b\d+\b\W+]', '', word) #replace everything with '' except words
            book_punc.append(w)
        books_punc.append(book_punc)
    return books_punc
books_punc = only_words(raw_books)


#remove ''
def remove_string(books_punc):
    books = []
    for book_punc in books_punc:
        book = []
        for word in book_punc:
            if word != '':
                book.append(word)
        books.append(book)
    return books

books = remove_string(books_punc)

#to get unique values
def get_unique(books):
    books_unique = []
    for book in books:
        book_unique = []
        for word in book:
            if word not in book_unique:
                book_unique.append(word)
        books_unique.append(book_unique)
    return books_unique

books_unique = get_unique(books)


for book_unique in books_unique:
    print(f'Number of unique words = {len(book_unique)}')
            
