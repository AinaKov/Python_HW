import open_file
import csv

def preview ():
    database = ''

    with open(open_file.full_n_f, 'r') as file:
        lines = csv.reader(file)

        for line in lines:
            myString = ' '.join(line).replace(',', ' ') + '\n'
            database = database + myString

        return(database)
