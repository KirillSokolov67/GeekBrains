def summa(numbers):
    numbers = numbers.split()
    b = []
    for i in numbers:
        b.append((int(i)))
    return sum(b)

s = 0
while 1:
    numbers = input("Введите строку чисел разделенным пробелом: ")
    if numbers.endswith('*'):
        numbers = numbers[:-1]
        s += summa(numbers)
        print("Сумма чисел: ", s)
        break
    s += summa(numbers)
    print("Сумма чисел: ", s)
