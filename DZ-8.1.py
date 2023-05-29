class Data:

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'Дата верная'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


print(Data.valid(28, 5, 2023))
print(Data.valid(11, 13, 2000))
print(Data.valid(0, 11, 1000))
print(Data.valid(1, 11, 2222))
