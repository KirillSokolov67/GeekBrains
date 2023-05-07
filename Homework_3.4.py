def my_func( x, y):
    result = 1
    for a in range(abs(y)):
        result = result * x
    return 1 / result

x = float(input('Введите значение "x": '))
y = int(input('Введите значение "y": '))

result_my_func = my_func(x, y)
print('Вот что получилось: ', result_my_func)