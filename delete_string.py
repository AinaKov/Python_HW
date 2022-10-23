import open_file

def del_str(num):
    with open(open_file.full_n_f, "r") as file:
        
        for num_line, line in enumerate(file):
            
                if num - 1 == num_line:
                    edit_string = line
                    print('Удалена строка:\n', edit_string.replace(',', ' '))
        
    with open(open_file.full_n_f, "r") as file:
        lines = file.readlines()

    with open(open_file.full_n_f, 'w') as f:

        for line in lines:

            if edit_string != line:
                f.write(line)
            elif edit_string == line:
                f.write('\n')
