import open_file

def find_string_number(search):
    numers = []
    new_list = []
    with open(open_file.full_n_f, 'r') as file:
        for num_line, line in enumerate(file):

            if search in line:
                numers.append(num_line)
                new_list.append(line)

        if(len(numers)>0):
            return(''.join(new_list).replace(',', ' '))
        else:
            return(f'Ни одной строки, содержащей "{search}" не нашлось')
