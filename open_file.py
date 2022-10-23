import re


name_file = input('Введите наименование файла из папки "folder" (формат csv): ')

full_n_f = f'folder\\{name_file}.csv'

def number_of_lines():
    el = len(re.findall(r"[\n']+?", open(full_n_f).read()))
    return el
