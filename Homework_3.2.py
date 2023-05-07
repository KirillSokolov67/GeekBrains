def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'{name},{lastname}, {year_of_birth}, {city}, {email}, {phone}')

personal_data(
    name = input("Назовите свое имя: "),
    lastname = input("Укажите свою фамилию: "),
    year_of_birth = input("Какой ваш год рождения: "),
    city = input("Город проживания: "),
    email = input("Email: "),
    phone = input("Номер телефона: "),
)