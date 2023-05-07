def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка ')


print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))