import open_file

def re_numb():
    with open(open_file.full_n_f, "r") as file:
        lines = file.readlines()

    with open(open_file.full_n_f, 'w') as f:
        num = 1
        for line in lines:
            if len(line)>0:
                new_string = line.replace(line.split(',')[0], str(num))
                f.write(new_string)
                num = int(num) + 1
            