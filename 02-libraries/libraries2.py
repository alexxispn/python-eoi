import datetime

my_birthday = datetime.date(1998, 11, 21)


def get_first_day_of_month():
    today = datetime.date.today()
    return today.replace(day=1)


def is_my_birthday(birthday):
    today = datetime.date.today()
    if birthday.month == today.month and birthday.day == today.day:
        return f'Happy birthday, {today.year - birthday.year} years old!'
    birthday = birthday.replace(year=today.year)
    if birthday > today:
        return f'Your birthday is in {birthday - today}'
    return f'Your birthday was {today - birthday} ago'


print(is_my_birthday(my_birthday))
