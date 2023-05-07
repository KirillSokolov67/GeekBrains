def my_func(arg1, arg2, arg3):
    if arg1 <= arg2 and arg1 <= arg3:
        return arg2 + arg3
    elif arg2 <= arg3:
        return arg1 + arg3
    else:
        return arg1 + arg2

arg1 = int(input('Укажите первый аргумент: '))
arg2 = int(input('Укажите второй аргумент: '))
arg3 = int(input('Укажите третий аргумент: '))
my_sum = my_func(arg1, arg2, arg3)
print('Максимальная сумма 2-ух аргументов равна', my_sum)