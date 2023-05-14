with open('new_file.txt', mode='a', encoding='utf-8') as file:
    while True:
        text = input('Напишите текст: ')
        file.write(text + '\n')
        if not text:
            break