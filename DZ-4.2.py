start_list = []
new_list = [int(i) for i in input("Введите список чисел: ").split()]

for i in range(1, len(new_list)):
    if new_list[i] > new_list[i-1]:
        (start_list.append(new_list[i]))

print("Исходный список: ", new_list)
print("Значения которые больше предыдущего : ", start_list)