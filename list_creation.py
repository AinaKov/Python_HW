import wheel_of_random as wr
import os
import csv


def list_creation (n):
    result_list = 'school'
    person_string = []

    if not os.path.exists(result_list):
        os.mkdir(result_list)

    with open(f'{result_list}\\{n}_person.csv', 'w', newline='') as file:
        for i in range(n):
            person_string = [i + 1] + wr.wheel_of_random()
            writer = csv.writer(file)
            writer.writerow(person_string)
