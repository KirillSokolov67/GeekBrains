from functools import reduce

list = [i for i in range(100, 1001, 2)]

print(list)

new_list = reduce(lambda num, num2: num * num2, list)
print(f"Результат: {new_list}")