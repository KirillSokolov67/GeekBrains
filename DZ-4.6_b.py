from itertools import cycle

print("Итератор, повторяющий элементы некоторого списка, определённого заранее: ")
a = 0
for value in cycle([4, 3, 2, 4, 7, 10]):
    if a > 10:
        break
    print(value)
    a += 1