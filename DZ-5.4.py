rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_file_3.txt', 'r', encoding='utf-8') as file_1:
    for i in file_1:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_file_3_new.txt', 'w',encoding='utf-8') as file_2:
    file_2.writelines(new_file)