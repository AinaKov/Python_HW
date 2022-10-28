import re
import csv
import UI

def number_of_lines(full_n_f):
    el = len(re.findall(r"[\n']+?", open(full_n_f).read()))
    return el

def preview(full_n_f):
    database = ''

    with open(full_n_f, 'r') as file:
        lines = csv.reader(file)

        for line in lines:
            my_string = ' '.join(line).replace(';', ' ') + '\n'
            database = database + my_string

        return(database)

def show_line(full_n_f, n):
    with open(full_n_f, "r") as file:
        
        for num_line, line in enumerate(file):
            
                if n == num_line:
                    edit_string = line
                    print('\nСтрока: ', edit_string.replace(';', ' '))

def added_data(full_n_f, el):
    with open(full_n_f, 'a') as file:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        sex = input('Введите пол (муж/жен): ')
        date = input('Введите дату рождения: ')
        num_clas = input('Введите класс: ')
        num_tel = input('Введите номер телефона родителя: ')
        num_tel_2 = input('Введите дополнительный номер телефона родителя: ')   
        el = str(el + 1 ) 
        person_string = el + ";" + name + ";" + surname + ";" + sex + ";" + date + ";" + num_clas + ";" + num_tel + ";" + num_tel_2 + '\n'
        file.write(person_string)
        print()
        print("Новая строка: ", person_string.replace(';', ' '))

def new_data():
    with open('students.csv', 'w') as file:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        sex = input('Введите пол (муж/жен): ')
        date = input('Введите дату рождения: ')
        num_clas = input('Введите класс: ')
        num_tel = input('Введите номер телефона родителя: ')
        num_tel_2 = input('Введите дополнительный номер телефона родителя: ')   
        person_string = "1" + ";" + name + ";" + surname + ";" + sex + ";" + date + ";" + num_clas + ";" + num_tel + ";" + num_tel_2 + '\n'
        file.write(person_string)
        print()
        print("Новая строка: ", person_string.replace(';', ' '))

def find_string_number(full_n_f, search):
    numers = []
    new_list = []
    with open(full_n_f, 'r') as file:
        for num_line, line in enumerate(file):

            if search in line:
                numers.append(num_line)
                new_list.append(line)

        if(len(numers)>0):
            print(UI.header_list)
            return(''.join(new_list).replace(';', ' '))
        else:
            return(f'Ни одной строки, содержащей "{search}" не нашлось')

def editing_replacement(full_n_f, search, old_word, new_word):
    with open(full_n_f, "r") as file:
        
        for num_line, line in enumerate(file):
            
                if search == num_line:
                    if old_word in line:
                        edit_string = line
                        new_string = edit_string.replace(old_word, new_word)
                        print('\nИзмененная строка: ', new_string.replace(';', ' '))
                    else:
                        mess = f'{old_word} в строчке {search} - нет'
                        print(mess)
                        return mess
                        
        
    with open(full_n_f, "r") as file:
        lines = file.readlines()

    with open(full_n_f, 'w') as f:

        for line in lines:

            if edit_string !=  line:
                f.write(line)

            elif edit_string == line:
                f.write(new_string)

def del_str(full_n_f, num):
    with open(full_n_f, "r") as file:
        
        for num_line, line in enumerate(file):
            
                if num == num_line:
                    edit_string = line
                    print('\nУдалена строка:\n', edit_string.replace(';', ' '))
        
    with open(full_n_f, "r") as file:
        lines = file.readlines()

    with open(full_n_f, 'w') as f:

        for line in lines:

            if edit_string != line:
                f.write(line)
            elif edit_string == line:
                f.write('\n')

def re_numb(full_n_f):
    with open(full_n_f, "r") as file:
        lines = file.readlines()

    with open(full_n_f, 'w') as f:
        num = 0
        for line in lines:
            if len(line)>0:
                new_string = line.replace(line.split(';')[0], str(num))
                f.write(new_string)
                num = int(num) + 1

def find_string_class(full_n_f, search):
    numers = []
    new_list = []
    with open(full_n_f, 'r') as file:
        for num_line, line in enumerate(file):

            if search in line:
                numers.append(num_line)
                new_list.append(line.split(';')[0] + ' ' + line.split(';')[1] + ' ' + line.split(';')[2] + '\n')

        return(''.join(new_list))

def print_string_class(full_n_f, search):
    numers = []
    new_list = []
    with open(full_n_f, 'r') as file:
        for num_line, line in enumerate(file):

            if search in line:
                numers.append(num_line)
                new_list.append(line.split(';')[0] + ';' + line.split(';')[1] + ';' + line.split(';')[2] + '\n')

        return(''.join(new_list))
