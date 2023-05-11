from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

for el in factorial_gen(6):
    print(el)