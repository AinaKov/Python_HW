import open_file
import file_preview
import search_element
import exchange
import delete_string
import re_numbering

open_file.name_file

while True:
    point = int(input('\nВыберите действие с файлом: \n1 - Полный просмотр файла\n2 - Поиск по файлу\n3 - Редактирование файла\n4 - Удаление строчки\n5 - Удаление элемента\n6 - Обновить id\n0 - Выйти из программы\n\n--> '))

    if point == 0:
        break

    elif point == 1:
        print(file_preview.preview())

    elif point == 2:
        search_text = input('Введите искомый текст: ')
        string_number = search_element.find_string_number(search_text)
        print(f'Строки, которые содержат "{search_text}":\n{string_number}')
            
    elif point == 3:
        red_line = int(input('Введите номер редактируемой строки: '))
        num_of_line = open_file.number_of_lines()

        if red_line <= num_of_line:
            old_word = input('Введите исходный текст: ')
            new_word = input('Введите новый текст: ')
            exchange.editing_replacement(red_line, old_word, new_word)
        else:
            print('В файле нет такой строки')
            
    elif point == 4:
        num_del = int(input('Введите номер удаляемой строки: '))
        num_of_line = open_file.number_of_lines()

        if num_del <= num_of_line:
            delete_string.del_str(num_del)
        else:
            print('В файле нет такой строки')       

    elif point == 5:
        redact_line = int(input('Введите номер редактируемой строки: '))
        num_of_line = open_file.number_of_lines()

        if redact_line <= num_of_line:
            old_word = input('Введите текст, который необходимо удалить: ')
            new_word = ''
            exchange.editing_replacement(redact_line, old_word, new_word)
        else:
            print('В файле нет такой строки') 
            
    elif point == 6:
        re_numbering.re_numb()
        re_numbering.re_numb()
