import os.path
import function
import work_cabinet
import work_language
import UI

f_stu = UI.name_file_stu
f_cab = UI.name_file_cab
f_lan = UI.name_file_lan

print(UI.welcome())

while True:

    point = int(input(UI.menu))

    if point == 0:
        print(UI.bay())
        break

    elif point == 1:
        print(function.preview(f_stu))

    elif point == 2:
        search_text = input('\nВведите искомый текст: ')
        string_number = function.find_string_number(f_stu, search_text)
        print(string_number)
            
    elif point == 3:
        red_line = int(input('\nВведите номер редактируемой строки: '))
        num_of_line = function.number_of_lines(f_stu)

        if red_line <= num_of_line:
            function.show_line(f_stu, red_line)
            old_word = input('Введите исходный текст: ')

            if " " in old_word:
                old_word = old_word.replace(' ', ';')

            new_word = input('Введите новый текст: ')
            
            if " " in new_word:
                new_word = new_word.replace(' ', ';')

            function.editing_replacement(f_stu, red_line, old_word, new_word)
        else:
            print('\nВ файле нет такой строки')
            
    elif point == 4:
        num_del = int(input('\nВведите номер удаляемой строки: '))
        
        num_of_line = function.number_of_lines(f_stu)

        if num_del <= num_of_line:
            function.show_line(f_stu, num_del)
            n = int(input('Удалить - 1, не удалять - 0: '))

            if n == 1:
                function.del_str(f_stu, num_del)

        else:
            print('\nВ файле нет такой строки\n')       

    elif point == 5:
        redact_line = int(input('\nВведите номер редактируемой строки: \n'))
        num_of_line = function.number_of_lines(f_stu)

        if redact_line <= num_of_line:
            function.show_line(f_stu, redact_line)
            old_word = input('Введите текст, который необходимо удалить: ')
            new_word = ''
            function.editing_replacement(f_stu, redact_line, old_word, new_word)

        else:
            print('В файле нет такой строки') 
            
    elif point == 6:
        if os.path.exists(f_stu):
            num_of_line = function.number_of_lines(f_stu)
            function.added_data(f_stu, num_of_line)
        else:
            function.new_data()

    elif point == 7:
        function.re_numb(f_stu)
        function.re_numb(f_stu)

    elif point == 8:
        work_cabinet.work_cab(f_cab, f_stu)

    elif point == 9:
        work_language.language(f_lan, f_stu)
