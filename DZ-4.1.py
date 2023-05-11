from sys import argv

print("Имя скрипта: ", argv[0])
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Ставка в час: ",  argv[1])
print("Выработка в часах: ", argv[2])
print("Премия: ", argv[3])

print("Зарплата одного сотрудника: ", (float(argv[2]) * float(argv[1])) + float(argv[3]))

