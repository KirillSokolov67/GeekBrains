class MyErrorZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def err():
    try:
        user_num_1 = int(input('Введите число: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise MyErrorZero("Делить на ноль нельзя!")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except MyErrorZero as err:
        return err


print(f"Результат деления: {err()} ")
