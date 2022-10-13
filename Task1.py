#Напишите программу, удаляющую из текста все слова, содержащие "абв".

data = open('file.txt', 'r', encoding='utf-8')
lst = data.read().split()
print('Исходный текст: ', ' '.join(lst)) # вывожу для наглядности

lst_abv = [wrd for wrd in lst if 'а' in wrd if 'б' in wrd if 'в' in wrd]
new_lst = [wrd for wrd in lst if wrd not in lst_abv]

print('Новый текст: ', ' '.join(new_lst))

# так как я в прошлый раз решала задание таким способом, он снова первым пришел в голову.
# максимум что нового смогла для себя изобрести - это поработать с фильтром

def filter_abv(string_to_check):
    if string_to_check in lst_abv:
        return False
    else:
        return True

out_filter = list(filter(filter_abv, lst))

print('Отфильтрованный текст: ', ' '.join(out_filter))