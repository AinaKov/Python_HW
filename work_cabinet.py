import function
import UI


def work_cab(name_f, name_f_pers):
    
    while True:
        point_cab = input(UI.menu_cab)
        if point_cab == '0':
            break
        elif point_cab == '1':
            print(UI.parameters)
            num_cab = str(input('Номер кабинета: '))
            day = input('День недели: ')
            num_less = str(input('Номер урока: '))
            num_class = input('Класс: ')
            
            i_data = []
            if not num_cab:
                i_data.append('0')
            if not day:
                i_data.append('1')
            if not num_less:
                i_data.append('2')
            if not num_class:
                i_data.append('3')

            el_answer = []
            student_list = []

            with open(name_f, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if num_cab in line.split(';')[0] and day in line.split(';')[1] and num_less in line.split(';')[2] and num_class in line.split(';')[3]:
                        for i in range(len(i_data)):
                            j = int(i_data[i])
                            el_answer.append(line.split(';')[j].replace('\n', ''))
                            answer = '-'.join(el_answer)
                            if j == 3:
                                student_list.append(line.split(';')[j].replace('\n', ''))
                        el_answer.append('\n')

            print('\nОтвет на запрос:\n', answer)
            
            point_2_cab = int(input('\nПоказать список студентов?\n1 - да\n0 - нет\n\n--> '))
            if point_2_cab == 1:
                for i in range(len(student_list)):
                        search_text = student_list[i]
                        string_number = function.find_string_class(name_f_pers, search_text, ' ')
                        print(f'\nУченики "{search_text}" класса:\n{string_number}')
                        

            point_3_cab = int(input('\nВывести список в отдельный файл?\n1 - да\n0 - нет\n\n--> '))
            if point_3_cab == 1:
                with open('new_list.csv', 'w') as f:
                    for i in range(len(student_list)):
                        search_text = student_list[i]
                        string_number = function.find_string_class(name_f_pers, search_text, ';')
                        f.write(f'\nУченики "{search_text}" класса:\n{string_number}')
                    
                print('Результат в файле - new_list.csv')
        
        elif point_cab == '!':
            print(UI.instr_cabinet)

        else:
            print('Введите 1 / 0 / !')
  