# birthday/utils.py 
# Импортируем модуль для работы с датами.
from datetime import date


def calculate_birthday_countdown(birthday):
    # Сохраняем текущую дату в переменную today.
    today = date.today()
    this_year_birthday = get_birthday_for_year(birthday, today.year)
    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        next_birthday = this_year_birthday

    # Считаем разницу между следующим днём рождения и сегодняшним днём в днях.
    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    try:
        # Пробуем заменить год в дате рождения на переданный в функцию.
        calculated_birthday = birthday.replace(year=year)
    # Если возникла ошибка, значит, день рождения 29 февраля
    # и подставляемый год не является високосным.
    except ValueError:
        # В этом случае устанавливаем ДР 1 марта.
        calculated_birthday = date(year=year, month=3, day=1)
    return calculated_birthday