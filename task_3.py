'''
● Create routines for getting these information:
○ Location of the file (done)
○ Content of the file as a String (done)
○ File size (done)
○ Last modification time (done)
○ Words (by splitting at spaces and punctuations) (done)
● Use your routines to get words from all the text files in
“random_chosen_imdb_comments.zip”.
● Create a dictionary that has the words as key and a List (Vector) of filenames in the
value section.
○ NB: Since all the comments are written in English, the case should not matter...
'''

import os
import time
import re

def location_of_files(folder):
    dirs = os.listdir(folder)
    return dirs

def content(file):
    with open('simplified_german_farytales/' + file, 'r', encoding='utf8') as file:
        data = file.read()
    return data

def file_size(path):
    size = os.path.getsize('simplified_german_farytales/' + path)
    return size
    
def modification_time(path):
    date = time.ctime(os.path.getmtime(path))
    return date

def splitting(string):
    string = re.findall(r"[\w]+|[^\s\w]", string)
    return string


words1 = []
dirs = location_of_files('simplified_german_farytales')
for file in dirs:
    file_to_string = content(file)
    words1.append(splitting(file_to_string))
    
# unite the list
words = []
for sublist in words1:
    words.extend(sublist)

# function to get unique values
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

unique_words_edit = unique(words)

# remove punctuation and numbers
def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~1234567890•'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string
 
unique_words_edit = [remove_punc(i) for i in unique_words_edit]


# remove empty strings
unique_words = []
for string in unique_words_edit:
    if (string != ""):
        unique_words.append(string)
        
# create dictionary with unique words
dic = {}

for word in unique_words:
    dic.update({word: []})

# check if word in a text, if so, add to the dictionary name of file
dirs = location_of_files('simplified_german_farytales')
for file in dirs:
    file_to_string = content(file)
    for key in dic.keys():
        if key in file_to_string:
            dic[key].append(file)
            
print(dic)
    
