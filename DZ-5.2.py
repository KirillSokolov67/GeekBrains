my_file = open('text_file_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')

my_file = open('text_file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
        new_l = content[i].split()
        print(f'Количество строк в файле {len(content)}. В {i + 1} данной строке {len(new_l)} слов(о)')

my_file = open('text_file_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')

my_file.close()