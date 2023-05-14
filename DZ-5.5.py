my_file = open('text_file_4.txt', 'w', encoding='utf-8')
text = input('Введите целое число: ')
my_file.write(text)
my_file.close()

my_file = open('text_file_4.txt', 'r', encoding='utf-8')
content = my_file.read()
print('Сумма всех чисел: ', sum(map(int, content.split())))
my_file.close()