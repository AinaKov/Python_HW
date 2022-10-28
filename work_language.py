import function


def language(name_f_lan, name_f_stu):
    num_stud = int(input('\nВведите id ученика: '))
            
    num_of_line = function.number_of_lines(name_f_stu)
    answer = []
    if num_stud <= num_of_line:
        with open(name_f_stu, "r") as file:
            for num_line, line in enumerate(file):
                if num_stud == num_line:
                    edit_string = line
                    class_stu = edit_string.split(';')[5]
                    
        with open(name_f_lan, "r") as file_2:
            for num_line, line in enumerate(file_2):
                if class_stu in line:
                    answer.append(edit_string.split(';')[0] + ' ' + edit_string.split(';')[1] + ' ' + edit_string.split(';')[2] + ' ' + edit_string.split(';')[5] + ' - ' + line.split(';')[1] + '\n')
                    answer_str = ''.join(answer)
        print('\n', answer_str)

    else:
        print('\nВ файле нет такой строки\n')    
