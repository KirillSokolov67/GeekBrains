from itertools import count, cycle

print("Введите целое число: ")
for item in count(20):
    if item > 100:
        break
    else:
        print(item)