my_file = open('list_of_employees.txt', 'r', encoding='utf-8')
content = my_file.readlines()

summary = 0
names = []

for line in content:
    line_split = line.split()
    summary += float(line_split[1])
    if float(line_split[1]) < 20000.00:
        names.append(line_split[0])
my_file.close()

print('Имена сотрудников: ', ', ' .join(names))
print('Средний доход сотрудников: ', summary/len(content))