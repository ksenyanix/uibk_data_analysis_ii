import os
import re
import unicodedata



diacritics = ['[àáâãäåèéêëìíîïòóôõöùúûüýÿßñ]']

#dir_path = r'C:\Users\Acer\OneDrive\Рабочий стол\uibk\vu data analytics ii\random_chosen_imdb_comments'

for root, directories, files in os.walk('random_chosen_imdb_comments'):
    for diacritic in diacritics:
        for file in files:
            filename = os.path.join(root, file)
            with open(filename, 'r', encoding='utf8') as file:
                t = file.read()
                result = re.search(diacritic, t)
                if result:
                    print(f'{file}: {result.group()}')

