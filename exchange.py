import open_file


def editing_replacement(search, old_word, new_word):
    with open(open_file.full_n_f, "r") as file:
        
        for num_line, line in enumerate(file):
            
                if search - 1 == num_line:
                    if old_word in line:
                        edit_string = line
                        print('Было: ', edit_string.replace(',', ' '))
                        new_string = edit_string.replace(old_word, new_word)
                        print('Стало: ', new_string.replace(',', ' '))
                    else:
                        mess = f'{old_word} в строчке {search} - нет'
                        print(mess)
                        return mess
                        
        
    with open(open_file.full_n_f, "r") as file:
        lines = file.readlines()

    with open(open_file.full_n_f, 'w') as f:

        for line in lines:

            if edit_string !=  line:
                f.write(line)

            elif edit_string == line:
                f.write(new_string)
