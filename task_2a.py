import os
import re

def validate_name(dictionary):
    new_dict = []
    for word in dictionary:
        word = re.compile(fr'{word}', re.IGNORECASE)
        new_dict.append(word)
    return new_dict

def searcher(text, reg):
    result_list = []
    for r in reg:
        result_list.append(r.search(text))
    return result_list

list_of_words = ['Hans', 'Gott', 'Es war einmal', 'langsam']
ignorcase_list = validate_name(list_of_words)

dir_path = r'C:\Users\Acer\OneDrive\Рабочий стол\uibk\vu data analytics ii\simplified_german_farytales'

for file in os.listdir(dir_path):
    filename = os.path.join(dir_path, file)
    with open(filename, 'r', encoding='utf8') as file:

        t = file.read()
        result_list = searcher(t, ignorcase_list)
        for result in result_list:
            if result:
                print(f'{filename}: {result.group()}')



